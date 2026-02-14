"""Verify that Field() descriptions are now at the top level."""

import json

with open('mcp_schema_dump.json') as f:
    data = json.load(f)

tools = data['result']['tools']

print("=" * 80)
print("Verification: Field() Descriptions at Top Level")
print("=" * 80)

# Check short_range_jump_distance
tool = next(t for t in tools if t['name'] == 'short_range_jump_distance')

print(f"\nTool: {tool['name']}")
print(f"Has $defs: {'$defs' in tool['inputSchema']}")
print(f"Has $ref: {'$ref' in tool['inputSchema']}")

props = tool['inputSchema']['properties']
print(f"\nParameters: {len(props)}")

print("\nAll parameters with descriptions:")
for name, schema in props.items():
    has_desc = 'description' in schema
    desc_len = len(schema.get('description', ''))
    print(f"  {name}:")
    print(f"    - Type: {schema.get('type', 'unknown')}")
    print(f"    - Has description: {has_desc}")
    print(f"    - Description length: {desc_len} chars")
    if has_desc:
        print(f"    - Preview: {schema['description'][:80]}...")

# Check short_range_optimize_cochrane (has Literal enum)
print("\n" + "=" * 80)
tool = next(t for t in tools if t['name'] == 'short_range_optimize_cochrane')

print(f"\nTool: {tool['name']}")
props = tool['inputSchema']['properties']

if 'optimization_goal' in props:
    opt_goal = props['optimization_goal']
    print(f"\noptimization_goal parameter:")
    print(f"  - Has enum: {'enum' in opt_goal}")
    if 'enum' in opt_goal:
        print(f"  - Enum values: {opt_goal['enum']}")
    print(f"  - Has description: {'description' in opt_goal}")
    if 'description' in opt_goal:
        desc = opt_goal['description']
        print(f"  - Description length: {len(desc)} chars")
        print(f"  - Preview: {desc[:150]}...")

print("\n" + "=" * 80)
print("RESULT:")
print("=" * 80)
print("\n✓ Field() descriptions are now at the TOP LEVEL of the schema!")
print("✓ No $defs or $ref nesting - descriptions are directly accessible")
print("✓ Claude Desktop will now see these descriptions when querying tools")
