import asyncio
import sys
import os

# Add parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clients.llm_with_mcp import get_github_context, generate_with_context, post_to_linkedin

async def run_example():
    # Example 1: Get GitHub repository context
    print("Fetching context from a GitHub repository...")
    github_data = await get_github_context("RakeshBR1999", "mcp-server", "README.md")
    print(f"Received GitHub context: {github_data}\n")

    # Example 2: Generate content using LLM with the GitHub context
    prompt = "Explain this repository in simple terms"
    print(f"Generating LLM response for prompt: '{prompt}'")
    llm_response = await generate_with_context(prompt, github_data)
    print(f"LLM Response: {llm_response}\n")

    # Example 3: Post to LinkedIn (commented out as it requires authentication)
    """
    print("Posting to LinkedIn...")
    linkedin_result = await post_to_linkedin("YOUR_TOKEN", "Check out this amazing code explanation!")
    print(f"LinkedIn posting result: {linkedin_result}")
    """

if __name__ == "__main__":
    asyncio.run(run_example())