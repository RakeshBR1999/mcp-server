import sys, os, asyncio
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mcp import Client
import anthropic

# Initialize MCP clients
github_client   = Client(server_url="http://localhost:8081")
linkedin_client = Client(server_url="http://localhost:8082")

# Initialize Anthropic client
claude = anthropic.Anthropic(api_key="YOUR_API_KEY")

async def get_github_context(repo_owner, repo_name, path):
    return await github_client.resource(
        "repository",
        repo_owner=repo_owner,
        repo_name=repo_name,
        path=path
    )

async def generate_with_context(prompt, github_context):
    resp = claude.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        messages=[{
            "role": "user",
            "content": f"GitHub context: {github_context}\n\nPrompt: {prompt}"
        }]
    )
    # Depending on SDK version, you may need resp.get("completion") or similar
    return resp.content[0].text

async def post_to_linkedin(access_token, content):
    return await linkedin_client.tool(
        "post_to_linkedin",
        access_token=access_token,
        content=content
    )

async def main():
    # 1) Fetch some GitHub context
    github_data = await get_github_context(
        "username", "repo-name", "path/to/file.py"
    )
    print("🔍 GitHub context fetched:", github_data)

    # 2) Generate explanation via Claude
    explanation = await generate_with_context(
        "Explain this code", github_data
    )
    print("\n💡 LLM explanation:\n", explanation)

    # 3) (Optional) Post to LinkedIn
    linkedin_result = await post_to_linkedin(
        "YOUR_TOKEN",
        f"Check out this code explanation:\n\n{explanation}"
    )
    print("\n✅ LinkedIn post result:", linkedin_result)

if __name__ == "__main__":
    # Run the async main
    asyncio.run(main())
