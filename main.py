import air
import air_convert

from fastmcp import FastMCP

mcp = FastMCP("Air")


@mcp.tool
def convert_html_to_airtags(html: str) -> str:
    "Converts HTML to Air Tags formatted by Ruff"
    return air_convert.html_to_airtags(html)


@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: air.Request):
    return air.responses.JSONResponse({"status": "healthy"})


http_app = mcp.http_app(path="/")

app = air.Air(lifespan=http_app.lifespan)


@app.page
async def index():
    return air.layouts.mvpcss(
        air.H1("AirMCP", style="text-align:center"),
        air.Article(
            air.Section(
                air.P(
                    "Interact with ",
                    air.A(
                        "Air web framework", href="https://airdocs.fastapicloud.dev/"
                    ),
                    " tools to expedite project development.",
                    style="text-align: center",
                ),
                air.Aside(
                    "https://airmcp.fastapicloud.dev/mcp", class_="copy-on-click"
                ),
                air.P(
                    air.Small("Click the URL to copy it"), style="text-align: center"
                ),
            )
        ),
        air.Children(
            air.Script("""
document.querySelectorAll('.copy-on-click').forEach(el => {
  el.addEventListener('click', () => {
    const text = el.innerText;
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.left = '-9999px';
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy'); // deprecated but widely supported
    document.body.removeChild(ta);
    // feedback
    el.textContent = 'Copied!';
    setTimeout(() => el.textContent = text, 800);
  });
});
""")
        ),
    )


app.mount("/mcp", http_app)
