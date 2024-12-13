import asyncio
import click
from mcp.client.session import ClientSession
from mcp.client.sse import sse_client


@click.command()
@click.option("--port", default=8000, help="Port to listen on for SSE")
@click.option("--host", default="0.0.0.0", help="Host to listen on for SSE")



def main(port: int, host: str):
    try:
        # Run the client logic
        asyncio.run(client_logic(host, port))
    finally:
        # Terminate the server process
        print("Server terminated.")


async def client_logic(host: str, port: int):
    print(f"Connecting to http://{host}:{port}/sse")
    async with sse_client(url=f"http://{host}:{port}/sse") as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            print(tools)

            # Call the fetch tool
            result = await session.call_tool("fetch", {"url": "https://example.com"})
            print(result)


if __name__ == "__main__":
    main()