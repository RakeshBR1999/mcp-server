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