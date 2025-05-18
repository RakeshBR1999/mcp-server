from mcp import Client
import anthropic

# Initialize MCP clients
github_client = Client(server_url="http://localhost:8081")
linkedin_client = Client(server_url="http://localhost:8082")

# Initialize Anthropic client
claude = anthropic.Anthropic(api_key="YOUR_API_KEY")

# Function to get GitHub context
async def get_github_context(repo_owner, repo_name, path):
    github_context = await github_client.resource("repository", 
                                                 repo_owner=repo_owner,
                                                 repo_name=repo_name,
                                                 path=path)
    return github_context

# Function to use LLM with context
async def generate_with_context(prompt, github_context):
    response = claude.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": f"GitHub context: {github_context}\n\nPrompt: {prompt}"
            }
        ]
    )
    return response.content[0].text

# Function to post to LinkedIn
async def post_to_linkedin(access_token, content):
    result = await linkedin_client.tool("post_to_linkedin",
                                       access_token=access_token,
                                       content=content)
    return result

# Example usage (would need to be wrapped in an async function or run with asyncio)
# github_data = await get_github_context("username", "repo-name", "path/to/file.py")
# llm_response = await generate_with_context("Explain this code", github_data)
# linkedin_result = await post_to_linkedin("YOUR_TOKEN", "Check out this amazing code explanation!")