import air
from starlette.requests import Request
from starlette.responses import JSONResponse

from fastmcp import FastMCP

mcp = FastMCP("MyServer")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello, {name}!"



mcp = FastMCP("MyServer")

@mcp.tool
def add(a: int, b: int) -> int:
    'Add two ints together.'
    return a+b

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request):
    return JSONResponse({"status": "healthy"})

http_app = mcp.http_app(path="/")

app = air.Air(lifespan=http_app.lifespan)

@app.page
async def index():
    return air.layouts.mvpcss(
        air.H1('Hello'),
        air.P(
            air.A('MCP', href='/mcp')
        )
    )

app.mount('/mcp', http_app)