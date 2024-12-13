# /// script
# dependencies = [
#   "mcp"
#   "httpx"
# ]
# ///
from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio
import mcp.types as types
import httpx

# Create a server instance
server = Server("example-server")

# Add prompt capabilities
# @server.list_prompts()
# async def handle_list_prompts() -> list[types.Prompt]:
#     return [
#         types.Prompt(
#             name="example-prompt",
#             description="An example prompt template",
#             arguments=[
#                 types.PromptArgument(
#                     name="arg1",
#                     description="Example argument",
#                     required=True
#                 )
#             ]
#         )
#     ]

# @server.get_prompt()
# async def handle_get_prompt(
#     name: str,
#     arguments: dict[str, str] | None
# ) -> types.GetPromptResult:
#     if name != "example-prompt":
#         raise ValueError(f"Unknown prompt: {name}")

#     return types.GetPromptResult(
#         description="Example prompt",
#         messages=[
#             types.PromptMessage(
#                 role="user",
#                 content=types.TextContent(
#                     type="text",
#                     text="Example prompt text"
#                 )
#             )
#         ]
#     )

# List available tools
@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="fetch",
            description="Fetches a website and returns its content",
            inputSchema={
                "type": "object",
                    "required": ["url"],
                    "properties": {
                        "url": {
                            "type": "string",
                            "description": "URL to fetch",
                        }
                    },
                },
        )
    ]

# Call a tool
@server.call_tool()
async def fetch_tool(
        name: str, arguments: dict
    ) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
        if name != "fetch":
            raise ValueError(f"Unknown tool: {name}")
        if "url" not in arguments:
            raise ValueError("Missing required argument 'url'")
        return await fetch_website(arguments["url"])

async def fetch_website(
    url: str,
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    headers = {
        "User-Agent": "MCP Test Server (github.com/modelcontextprotocol/python-sdk)"
    }
    async with httpx.AsyncClient(follow_redirects=True, headers=headers) as client:
        response = await client.get(url)
        response.raise_for_status()
        return [types.TextContent(type="text", text=response.text)]


async def run():
    # Run the server as STDIO
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="mcp-website-fetcher",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                )
            )
        )

if __name__ == "__main__":
    import asyncio
    asyncio.run(run())