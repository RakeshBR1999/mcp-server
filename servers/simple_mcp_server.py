import sys
import os

# Add parent directory to path so we can import mcp module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mcp import Server, Resource

# Initialize server
server = Server(name="my-first-mcp-server", 
                description="A simple MCP server")

# Define a resource
@server.resource(name="greeting")
async def greeting_resource():
    return "Hello from MCP!"

# Start the server
if __name__ == "__main__":
    server.run(port=8080)