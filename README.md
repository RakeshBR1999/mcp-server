# Model Context Protocol (MCP) Implementation Examples

This repository contains example implementations of the Model Context Protocol (MCP), a standardized way to provide context to Large Language Models (LLMs).

## What is MCP?

Model Context Protocol (MCP) is an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications - it provides a standardized way to connect AI models to different data sources and tools.

## Contents

This repository includes:

- `simple_mcp_server.py`: A basic MCP server implementation
- `github_mcp_server.py`: An MCP server that provides code context from GitHub repositories
- `linkedin_mcp_server.py`: An MCP server that enables LinkedIn integration
- `llm_with_mcp.py`: Example code for connecting an LLM to MCP servers

## Getting Started

### Prerequisites

- Python 3.8+
- Required Python packages (install with pip):


### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/mcp-server.git
cd mcp-server
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running a Simple MCP Server

```bash
python simple_mcp_server.py
```

This will start a basic MCP server on `http://localhost:8000`.

### GitHub Integration

To run the GitHub MCP server:

```bash
# Set your GitHub token as an environment variable
export GITHUB_TOKEN=your_github_token_here

# Run the server
python github_mcp_server.py
```

### LinkedIn Integration

To run the LinkedIn MCP server:

```bash
# Set your LinkedIn credentials
export LINKEDIN_CLIENT_ID=your_client_id
export LINKEDIN_CLIENT_SECRET=your_client_secret

# Run the server
python linkedin_mcp_server.py
```

### Connecting an LLM to MCP Servers

```bash
python llm_with_mcp.py
```

See the code for examples of how to configure your LLM to use different MCP servers.

## Configuration

You can configure the servers using environment variables or by modifying the configuration files:

- `config/simple_mcp_config.json`: Configuration for the simple MCP server
- `config/github_config.json`: Configuration for the GitHub MCP server
- `config/linkedin_config.json`: Configuration for the LinkedIn MCP server

### Configuration File Details

#### Simple MCP Server Configuration
The `config/simple_mcp_config.json` file contains settings for the basic MCP server:

```json
{
    "server": {
        "host": "0.0.0.0",
        "port": 8000,
        "debug": false
    },
    "retrieval": {
        "max_context_length": 4000,
        "max_results": 5,
        "similarity_threshold": 0.7
    },
    "logging": {
        "level": "INFO",
        "file": "logs/simple_mcp_server.log"
    }
}
```

#### GitHub MCP Server Configuration
The `config/github_config.json` file configures the GitHub integration:

```json
{
    "server": {
        "host": "0.0.0.0",
        "port": 8001,
        "debug": false
    },
    "github": {
        "token": "",
        "max_repos": 5,
        "max_files_per_repo": 20,
        "include_private_repos": false
    },
    "retrieval": {
        "max_context_length": 4000,
        "max_results": 5,
        "similarity_threshold": 0.7
    },
    "logging": {
        "level": "INFO",
        "file": "logs/github_mcp_server.log"
    }
}
```

#### LinkedIn MCP Server Configuration
The `config/linkedin_config.json` file configures the LinkedIn integration:

```json
{
    "server": {
        "host": "0.0.0.0",
        "port": 8002,
        "debug": false
    },
    "linkedin": {
        "client_id": "",
        "client_secret": "",
        "redirect_uri": "http://localhost:8002/auth/callback",
        "scope": "r_liteprofile r_emailaddress"
    },
    "retrieval": {
        "max_context_length": 2000,
        "max_results": 3
    },
    "logging": {
        "level": "INFO",
        "file": "logs/linkedin_mcp_server.log"
    }
}
```

### Using Environment Variables

You can also configure the servers using environment variables:

```bash
# Simple MCP Server
export MCP_SERVER_PORT=8000
export MCP_MAX_CONTEXT_LENGTH=4000

# GitHub MCP Server
export GITHUB_TOKEN=your_github_token_here
export GITHUB_MCP_SERVER_PORT=8001

# LinkedIn MCP Server
export LINKEDIN_CLIENT_ID=your_client_id
export LINKEDIN_CLIENT_SECRET=your_client_secret
export LINKEDIN_MCP_SERVER_PORT=8002
```

## API Documentation

Each MCP server implements the following endpoints:

- `POST /retrieve`: Retrieves context based on the input query
- `GET /health`: Health check endpoint
- `GET /info`: Returns information about the server capabilities

For detailed API documentation, see the [MCP Specification](https://example.com/mcp-spec).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
