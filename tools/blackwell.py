"""
USS Blackwell MCP Server - General server description tool.

This module provides the blackwell_describe tool which returns metadata
about the USS Blackwell Red Matter Core MCP Server.
"""


def blackwell_describe() -> dict:
    """
    Describe the USS Blackwell Red Matter Core MCP Server.
    
    Returns metadata about the server including its name, vessel designation,
    narrative description, available tool categories, and registered tools.
    
    Returns:
        dict: Server metadata with the following fields:
            - server_name (str): The MCP server name
            - vessel (str): The vessel designation
            - description (str): Full narrative description
            - available_tool_categories (list[str]): List of tool categories
            - available_tools (list[str]): List of all registered tool names
            - success (bool): Always True
    """
    return {
        "server_name": "uss-blackwell-mcp",
        "vessel": "USS Blackwell NX-8091-B",
        "description": (
            "The USS Blackwell NX-8091-B, an experimental rapid-response medical cruiser — "
            "its most closely guarded secret is a weaponized red matter core, originally "
            "developed at Nikolaev's Crucible and repurposed by Starfleet to fold the fabric "
            "of subspace, allowing the ship to cross vast distances in an instant — a "
            "superweapon turned rescue vehicle. This MCP server was developed by Kyt Dotson, "
            "science fiction author, to allow LLMs to quickly perform calculations involving "
            "the red matter core in the Star Trek fanfiction universe — including long range "
            "and short range jumps, translating objects within the red matter field, and "
            "performing other strange miracles to execute the Blackwell's mission to save lives."
        ),
        "author": "Kyt Dotson",
        "links": {
            "fanfiction_series": "https://archiveofourown.org/series/1512200",
            "twitter": "http://x.com/kytsune",
            "bluesky": "https://bsky.app/profile/kytsune.bsky.social"
        },
        "available_tool_categories": ["long_range", "short_range"],
        "available_tools": [],  # Will be populated dynamically later
        "success": True
    }
