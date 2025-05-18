import sys
import os

# Add parent directory to path so we can import mcp module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mcp import Server, Resource
import aiohttp

server = Server(name="github-code-context", 
                description="Provides code context from GitHub repos")

@server.resource(name="repository")
async def github_resource(repo_owner: str, repo_name: str, path: str = ""):
    # Create a GitHub API URL
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{path}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return {
                    "content": data.get("content", ""),
                    "path": data.get("path", ""),
                    "type": data.get("type", "")
                }
            return {"error": f"Failed to fetch GitHub content: {response.status}"}

if __name__ == "__main__":
    server.run(port=8081)