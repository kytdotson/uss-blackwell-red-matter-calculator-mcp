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
from tools.short_range import (
    short_range_describe,
    short_range_jump_distance,
    short_range_field_strength,
    short_range_criticality,
    short_range_sequential_jumps,
    short_range_optimize_cochrane
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
    "interstellar jumps via dimensional folding and short range tactical jumps within "
    "stellar systems using quantum-scale subspace resonances (Rizan's Resonance Bridge "
    "Theory), translating objects within the red matter field, and performing other "
    "strange miracles to execute the Blackwell's mission to save lives."
)

# Create MCP server instance
server = MCPServer(
    name="uss-blackwell-mcp", #maybe name this uss-blackwell-mcp? way shorter!
    version="1.0.4-a1",
    instructions=NARRATIVE_DESCRIPTION,
    host="0.0.0.0",
    port="3000",
)

# Register all tools using the @server.tool() decorator
server.tool()(blackwell_describe)
server.tool()(long_range_describe)
server.tool()(long_range_jump_distance)
server.tool()(long_range_field_strength)
server.tool()(short_range_describe)
server.tool()(short_range_jump_distance)
server.tool()(short_range_field_strength)
server.tool()(short_range_criticality)
server.tool()(short_range_sequential_jumps)
server.tool()(short_range_optimize_cochrane)

if __name__ == "__main__":
    # Check environment variable for transport mode
    import os
    transport_mode = os.environ.get("MCP_TRANSPORT", "http")
    
    if transport_mode == "stdio":
        # Run with stdio transport (for MCP clients and testing)
        server.run(transport="stdio", debug=True)
    else:
        # Run with HTTP transport (for web clients)
        server.run(
            transport="streamable-http",
            reload=False,
            debug=False
        )
