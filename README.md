# AirMCP

Configuring Gemini to use local version of AirMCP

```json
{
  "theme": "Dracula",
  "selectedAuthType": "gemini-api-key",
  "preferredEditor": "vscode",
  "mcpServers": {
      "Air": {
        "command": "uv",
        "args": [
          "run",
          "--with",
          "fastmcp",
          "fastmcp",
          "run",
          "/Users/drg/projects/air-repos/AirMCP/main.py"
        ],
        "timeout": 5000
      }
  }
}
```

Configuring Gemini to use the hosted version of AirMCP:

```json
{
  "theme": "Dracula",
  "selectedAuthType": "gemini-api-key",
  "preferredEditor": "vscode",
  "mcpServers": {
    "Air": {
        "httpUrl": "https://airmcp.fastapicloud.dev/mcp"
    }
  }
}
```