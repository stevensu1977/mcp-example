# MCP-Example

A demonstration project implementing the Model Context Protocol (MCP), showcasing client-server communication with various functionalities including web content fetching and system monitoring.

## Features

- Web content fetching and parsing
- System information monitoring
- Real-time server-sent events (SSE) communication
- MCP protocol implementation
- Resource management and tool execution

## Requirements

- Python 3.10+ 
- Dependencies (install via pip):
  - httpx
  - beautifulsoup4
  - uvicorn
  - psutil
  - mcp-sdk

## Installation

1. Clone the repository:
```bash
git clone https://github.com/stevensu1977/mcp-example.git
cd mcp-example.git
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the SSE server:
```bash
#There have two types server , sse and stdio
python sse/exampe_server.py
```
The server will start on http://localhost:8000

2. In a separate terminal, run the SSE client:
```bash
python sse/exampe_client.py
```

```bash
(.venv) ➜  mcp-example git:(main) ✗ python sse/example_client.py
Connecting to http://0.0.0.0:8000/sse
nextCursor=None tools=[Tool(name='fetch', description='Fetches a website and returns its content', inputSchema={'type': 'object', 'required': ['url'], 'properties': {'url': {'type': 'string', 'description': 'URL to fetch'}}})]
content=[TextContent(type='text', text='<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title>\n\n    <meta charset="utf-8" />\n    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />\n    <meta name="viewport" content="width=device-width, initial-scale=1" />\n    <style type="text/css">\n    body {\n        background-color: #f0f0f2;\n        margin: 0;\n        padding: 0;\n        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;\n        \n    }\n    div {\n        width: 600px;\n        margin: 5em auto;\n        padding: 2em;\n        background-color: #fdfdff;\n        border-radius: 0.5em;\n        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);\n    }\n    a:link, a:visited {\n        color: #38488f;\n        text-decoration: none;\n    }\n    @media (max-width: 700px) {\n        div {\n            margin: 0 auto;\n            width: auto;\n        }\n    }\n    </style>    \n</head>\n\n<body>\n<div>\n    <h1>Example Domain</h1>\n    <p>This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission.</p>\n    <p><a href="https://www.iana.org/domains/example">More information...</a></p>\n</div>\n</body>\n</html>\n')] isError=False
```



The client will connect to the server and demonstrate various functionalities including:

- Fetching external web content

## Protocol Implementation

This project implements the Model Context Protocol (MCP), providing a framework for:
- Server-Sent Events (SSE) based communication
- Resource management
- Tool execution
- Client-server interaction

## License

See the [LICENSE](LICENSE) file for details.