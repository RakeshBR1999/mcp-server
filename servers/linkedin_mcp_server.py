from mcp import Server, Tool
import aiohttp

server = Server(name="linkedin-integration", 
                description="Allows LLMs to interact with LinkedIn data")

@server.tool(name="post_to_linkedin")
async def post_to_linkedin(access_token: str, content: str, visibility: str = "public"):
    """Posts content to LinkedIn with the provided credentials."""
    url = "https://api.linkedin.com/v2/ugcPosts"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    body = {
        "author": "urn:li:person:{PERSON_ID}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": content
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": visibility.upper()
        }
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=body) as response:
            if response.status == 201:
                return {"status": "success", "message": "Posted to LinkedIn successfully"}
            return {"status": "error", "message": f"Failed to post: {response.status}"}

if __name__ == "__main__":
    server.run(port=8082)