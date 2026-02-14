"""
Dump the actual MCP schema to a file so we can see exactly what's being sent.
"""

import json
import subprocess
import sys
import os


env = os.environ.copy()
env["MCP_USE_ANONYMIZED_TELEMETRY"] = "false"
env["MCP_TRANSPORT"] = "stdio"

process = subprocess.Popen(
    [sys.executable, "server.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1,
    env=env
)

try:
    # Initialize
    init_req = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "test", "version": "1.0"}
        }
    }) + "\n"
    process.stdin.write(init_req)
    process.stdin.flush()
    
    # Read init response
    while True:
        line = process.stdout.readline()
        if line.strip().startswith('{'):
            break
    
    # List tools
    tools_req = json.dumps({
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/list"
    }) + "\n"
    process.stdin.write(tools_req)
    process.stdin.flush()
    
    # Read tools response
    while True:
        line = process.stdout.readline()
        if line.strip().startswith('{'):
            response = json.loads(line)
            break
    
    # Save to file
    with open("mcp_schema_dump.json", "w") as f:
        json.dump(response, f, indent=2)
    
    print("Schema dumped to mcp_schema_dump.json")
    
    # Show summary
    tools = response["result"]["tools"]
    tool = next((t for t in tools if t["name"] == "long_range_jump_distance"), None)
    
    if tool:
        print(f"\nTool: {tool['name']}")
        schema = tool["inputSchema"]
        
        # Show structure
        print(f"Schema has $defs: {'$defs' in schema}")
        print(f"Schema has $ref: {'$ref' in schema}")
        
        if "$defs" in schema:
            for model_name, model_def in schema["$defs"].items():
                print(f"\nModel: {model_name}")
                if "properties" in model_def:
                    for prop_name, prop_schema in model_def["properties"].items():
                        has_desc = "description" in prop_schema
                        print(f"  {prop_name}: {prop_schema.get('type')} - Has description: {has_desc}")

finally:
    process.terminate()
    process.wait()
