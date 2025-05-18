import aiohttp
from typing import Any, Dict, Optional

class Client:
    def __init__(self, server_url: str):
        self.server_url = server_url.rstrip('/')
        
    async def resource(self, name: str, **params):
        """Call a resource on the MCP server."""
        url = f"{self.server_url}/resources/{name}"
        return await self._make_request(url, params)
    
    async def tool(self, name: str, **params):
        """Call a tool on the MCP server."""
        url = f"{self.server_url}/tools/{name}"
        return await self._make_request(url, params)
    
    async def info(self):
        """Get information about the MCP server."""
        url = f"{self.server_url}/info"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    error_text = await response.text()
                    raise Exception(f"MCP server error: {response.status} - {error_text}")
    
    async def _make_request(self, url: str, data: Dict[str, Any]):
        """Make a POST request to the MCP server."""
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    error_text = await response.text()
                    raise Exception(f"MCP server error: {response.status} - {error_text}")