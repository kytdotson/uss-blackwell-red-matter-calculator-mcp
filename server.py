"""
USS Blackwell Red Matter Core MCP Server

Entry point for the Model Context Protocol server that exposes dimensional fold
calculation tools for the USS Blackwell fanfiction universe.

This server provides tools for:
- Server and system description
- Long-range jump distance calculations
- Required field strength calculations

The server uses the mcp-use library and supports stdio transport for MCP clients
such as Claude Desktop (additionally modified for http-streaming transport).
"""

from mcp_use.server import MCPServer
from tools.blackwell import blackwell_describe
from tools.long_range import (
    long_range_describe,
    long_range_jump_distance,
    long_range_field_strength
)

# Full narrative description for the server instructions
NARRATIVE_DESCRIPTION = (
    "The USS Blackwell NX-8091-B, an experimental rapid-response medical cruiser — "
    "its most closely guarded secret is a weaponized red matter core, originally "
    "developed at Nikolaev's Crucible and repurposed by Starfleet to fold the fabric "
    "of subspace, allowing the ship to cross vast distances in an instant — a "
    "superweapon turned rescue vehicle. This MCP server was developed by Kyt Dotson, "
    "science fiction author, to allow LLMs to quickly perform calculations involving "
    "the red matter core in the Star Trek fanfiction universe — including long range "
    "and short range jumps, translating objects within the red matter field, and "
    "performing other strange miracles to execute the Blackwell's mission to save lives."
)

# Create MCP server instance
server = MCPServer(
    name="uss-blackwell-red-matter-core-calculator-mcp",
    version="1.0.0",
    instructions=NARRATIVE_DESCRIPTION,
    host="0.0.0.0",
    port="3000",
)

# Register all tools using the @server.tool() decorator
server.tool()(blackwell_describe)
server.tool()(long_range_describe)
server.tool()(long_range_jump_distance)
server.tool()(long_range_field_strength)

if __name__ == "__main__":
    # Run with stdio transport (for MCP clients)
    #server.run(transport="stdio")

    # Run with HTTP transport (for web clients)
    server.run(
    transport="streamable-http",
    reload=False,
    debug=False
    )
