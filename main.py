import air
from starlette.requests import Request
from starlette.responses import JSONResponse
import air_convert

from fastmcp import FastMCP

mcp = FastMCP("Air")

@mcp.tool
def convert_html_to_airtags(html: str) -> str:
    'Converts HTML to Air Tags formatted by Ruff'
    return air_convert.html_to_airtags(html)

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