# AirMCP

Configuring Gemini to use local version of AirMCP

```json
{
  "theme": "Dracula",
  "selectedAuthType": "gemini-api-key",
  "preferredEditor": "vscode",
  "mcpServers": {
      "AirMCP": {
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