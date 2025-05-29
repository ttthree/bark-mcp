# bark-mcp

## What is Bark
[Bark](https://github.com/Finb/bark-server) is a notification server for iOS. It provides a simple HTTP API to send notifications to iOS devices.

## What is MCP
[Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) is an open protocol that standardizes how applications provide context to Large Language Models (LLMs).

## MVP scope
A MCP server that talks to Bark to send notifications to iOS devices.
Only 1 tool: notify(title, content, url) where title and url are optional.
Required environment variables: Bark server URL, Bark API key
Implement as stdio MCP server, command line: uvx bark-mcp

## Design consideration
A pip package named bark-mcp which includes the MCP server that can be started with command line: uvx bark-mcp

Python with FastAPI; Leverage FastMCP package.