# USS Blackwell NX-8091-B — Red Matter Core MCP Server
## Kiro Implementation Specification

---

> *The USS Blackwell, an experimental rapid-response medical cruiser — its most closely guarded secret is a weaponized red matter core, originally developed at Nikolaev's Crucible and repurposed by Starfleet to fold the fabric of subspace, allowing the ship to cross vast distances in an instant — a superweapon turned rescue vehicle. This MCP server was developed by Kyt Dotson, science fiction author, to allow LLMs to quickly perform calculations involving the red matter core in the Star Trek fanfiction universe — including long range and short range jumps, translating objects within the red matter field, and performing other strange miracles to execute the Blackwell's mission to save lives.*

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Tool Naming Convention](#2-tool-naming-convention)
3. [Mathematical Specification](#3-mathematical-specification)
4. [Tool Specifications](#4-tool-specifications)
5. [Project File Structure](#5-project-file-structure)
6. [Constants (constants.py)](#6-constants-constantspy)
7. [Verification Test Cases](#7-verification-test-cases)
8. [Dependencies (requirements.txt)](#8-dependencies-requirementstxt)
9. [Server Entry Point Pattern (server.py)](#9-server-entry-point-pattern-serverpy)
10. [Implementation Notes for Kiro](#10-implementation-notes-for-kiro)

---

## 1. Project Overview

This document specifies the implementation of a Python-based MCP (Model Context Protocol) server that exposes Red Matter dimensional fold calculation functions for use in the USS Blackwell fanfiction universe. The server is designed with a namespaced tool architecture to support future expansion with additional calculation categories.

| Property | Value |
|---|---|
| **Server Name** | `uss-blackwell-red-matter-core-calculator-mcp` |
| **Language** | Python 3.10+ |
| **Protocol** | Model Context Protocol (MCP) |
| **Library** | mcp-use (extends official MCP SDK) |
| **Install** | `pip install mcp-use` |
| **Initial Tool Count** | 4 tools (1 general + 1 long_range describe + 2 long_range calc) |
| **Future Expansion** | Supported via prefix namespacing |

---

## 2. Tool Naming Convention

All MCP tools in this server follow a two-part naming scheme: a category prefix followed by a function name. This allows multiple calculation categories to coexist in the same server without naming conflicts, and makes tool purpose immediately clear to any LLM or developer consuming the server.

**Pattern:** `{category_prefix}_{function_name}`

### Initial tools

| Tool Name | Category | Function | Description |
|---|---|---|---|
| `blackwell_describe` | `blackwell` | `describe` | Server narrative, lore, and capability overview |
| `long_range_describe` | `long_range` | `describe` | Magellan definition, equation, and zone reference |
| `long_range_jump_distance` | `long_range` | `jump_distance` | D from field strength M |
| `long_range_field_strength` | `long_range` | `field_strength` | M from target distance D |

### Planned future categories (not implemented in this spec)

| Prefix | Intended Use Case | Example Tool Name |
|---|---|---|
| `short_range` | Micro-jump calculations | `short_range_jump_distance` |
| `core_output` | Red matter core diagnostics | `core_output_power_level` |
| `near_field` | Near-field intensity mapping | `near_field_intensity` |
| `subspace` | Subspace flexure distortion | `subspace_flexure_distortion` |
| `displacement` | Object point-to-point | `displacement_calculate` |

> ⚠️ *Never use generic tool names like `calculate()` or `get_distance()`. Always include the category prefix so tool names remain unambiguous as the server grows.*

---

## 3. Mathematical Specification

### 3.1 Forward Equation: Jump Distance

Calculates the distance traveled (in light-years) given a field strength in Magellans.

```
D  =  K × ln(M − M₀) × √(M / Mₓ) × ξ(M)
```

| Symbol | Name | Value / Type | Notes |
|---|---|---|---|
| `D` | Distance | float, light-years | Output |
| `M` | Field Strength | float, Magellans | Input |
| `M₀` | Safety Threshold | 200.0 Magellans | Constant — ln breaks below this |
| `Mₓ` | Critical Resonance | 1847.0 Magellans | Constant — engineering constraint |
| `K` | Dimensional Constant | 12.7 | Constant |
| `ξ(M)` | Efficiency Factor | float | See 3.2 below |

> ⚠️ *M must be strictly greater than M₀ (200 Magellans). At or below this threshold, ln(M − M₀) is undefined or negative and the equation breaks down. This must be treated as a hard error.*

---

### 3.2 Efficiency Factor ξ(M)

The efficiency factor is a piecewise function representing field harmonic behavior across operating ranges:

| Range | ξ Value | Zone Label |
|---|---|---|
| M < 1,000 | 1.0 | Standard Efficiency |
| 1,000 ≤ M < 10,000 | **1.2** | Optimal / Sweet Spot |
| M ≥ 10,000 | 0.8 | Diminishing Returns |

---

### 3.3 Inverse Equation: Field Strength from Distance

There is no closed-form algebraic inverse for the forward equation due to the combination of logarithmic, square root, and piecewise efficiency terms. The inverse must be solved numerically using the Newton-Raphson method, as implemented in the reference HTML calculator.

**Newton-Raphson algorithm:**

- Initial guess: M = 1000 Magellans
- Convergence tolerance: 0.01 light-years
- Maximum iterations: 100
- Numerical derivative: ΔM = 1 Magellan
- Clamp lower bound: M must not fall at or below M₀ (200) during iteration
- Termination: If M exceeds 4,000,000 Magellans (2× MAX_SAFE) without convergence, return an error

---

### 3.4 Safety Boundaries

| Boundary | Value | Behavior |
|---|---|---|
| Safety Floor (M₀) | 200 Magellans | Hard error — equation undefined |
| Caution Zone | 200–999 Magellans | Return result with warning flag |
| Standard Zone | 1,000–9,999 Magellans | Normal operation |
| Optimal Zone | 1,000–9,999 Magellans | ξ = 1.2, best efficiency |
| Max Safe Output | 2,000,000 Magellans | Soft ceiling — warn above this |
| Catastrophic Risk | > 3,000,000 Magellans | Return error, refuse calculation |

---

## 4. Tool Specifications

### 4.1 `blackwell_describe`

Returns the narrative description of the USS Blackwell and this MCP server. Intended to be called when a user asks what the server does, what the Blackwell is, or requests an overview of capabilities. Takes no parameters.

```python
@server.tool()
def blackwell_describe() -> dict:
    """
    Returns a narrative description of the USS Blackwell, its red matter
    core, and the capabilities of this MCP server.
    Call this when a user asks what this server does or what the Blackwell is.
    """
```

**Output schema:**

| Field | Type | Always Present | Description |
|---|---|---|---|
| `server_name` | str | Always | `uss-blackwell-red-matter-core-calculator-mcp` |
| `vessel` | str | Always | `USS Blackwell NX-8091-B` |
| `description` | str | Always | Full narrative description of the server (see below) |
| `available_tool_categories` | list[str] | Always | e.g. `["long_range"]` |
| `available_tools` | list[str] | Always | All registered tool names |
| `success` | bool | Always | Always `True` |

**`description` field — exact string:**

> *"The USS Blackwell NX-8091-B, an experimental rapid-response medical cruiser — its most closely guarded secret is a weaponized red matter core, originally developed at Nikolaev's Crucible and repurposed by Starfleet to fold the fabric of subspace, allowing the ship to cross vast distances in an instant — a superweapon turned rescue vehicle. This MCP server was developed by Kyt Dotson, science fiction author, to allow LLMs to quickly perform calculations involving the red matter core in the Star Trek fanfiction universe — including long range and short range jumps, translating objects within the red matter field, and performing other strange miracles to execute the Blackwell's mission to save lives."*

---

### 4.2 `long_range_describe`

Returns a reference document explaining the long-range jump calculation system: what a Magellan is, how field intensity is measured, the full dimensional fold equation, efficiency zones, and safety boundaries. Intended to be called when a user asks how the long-range jump system works or what a Magellan measures. Takes no parameters.

```python
@server.tool()
def long_range_describe() -> dict:
    """
    Returns a reference description of the long-range jump system,
    including the Magellan unit definition, the dimensional fold equation,
    efficiency zones, and safety boundaries.
    Call this when a user asks how long-range jumps work or what a Magellan is.
    """
```

**Output schema:**

| Field | Type | Always Present | Description |
|---|---|---|---|
| `unit_name` | str | Always | `"Magellan"` |
| `unit_symbol` | str | Always | `"M"` |
| `unit_definition` | str | Always | Prose definition of the Magellan unit (see below) |
| `unit_base_measurement` | str | Always | `"M per cubic meter [of subspace flexure density (F:j,i,k)]"` |
| `unit_jump_measurement` | str | Always | `"Measured at the core for jump purposes"` |
| `equation` | str | Always | Human-readable equation string |
| `equation_variables` | dict | Always | Symbol-to-description map for all terms |
| `efficiency_zones` | list[dict] | Always | Each zone: `range`, `xi_value`, `label` |
| `safety_boundaries` | list[dict] | Always | Each boundary: `range`, `status`, `behavior` |
| `example_results` | list[dict] | Always | Reference results from known inputs |
| `success` | bool | Always | Always `True` |

**`unit_definition` field — exact string:**

> *"The Magellan (M) is the scalar unit of red matter field output strength, measuring field intensity. In general subspace physics it is expressed as M per cubic meter of subspace flexure density — written M per m³ [F:j,i,k] — where j, i, k denote the orthogonal flexure tensor indices of the local subspace manifold. For the purposes of dimensional fold jump calculations, field strength is measured directly at the red matter core output rather than distributed across subspace volume."*

**`equation` field — exact string:**

```
D = K × ln(M − M₀) × √(M / Mₓ) × ξ(M)
```

**`equation_variables` dict:**

| Key | Value |
|---|---|
| `D` | Distance traveled in light-years (output) |
| `M` | Field strength in Magellans (input) |
| `M0` | Safety threshold — 200 Magellans (constant). Equation undefined at or below this value. |
| `Mx` | Critical resonance point — 1,847 Magellans (constant). Engineering constraint. |
| `K` | Dimensional constant — 12.7 (constant) |
| `xi(M)` | Efficiency factor — piecewise function of field harmonics. 1.0 standard, 1.2 optimal, 0.8 diminishing. |

---

### 4.3 `long_range_jump_distance`

Calculates the jump distance in light-years for a given Red Matter field strength. This is the forward calculation: given an input in Magellans, return the fold distance.

```python
@server.tool()
def long_range_jump_distance(
    field_strength_magellans: float
) -> dict:
    """
    Calculate the dimensional fold jump distance for a given
    Red Matter field strength using the Blackwell Drive equation.

    Args:
        field_strength_magellans: Field strength in Magellans.
            Must be greater than 200 (safety threshold M0).
            Practical range: 201 to 2,000,000 Magellans.

    Returns:
        A dict with keys: distance_light_years, efficiency_factor,
        efficiency_zone, safety_status, warnings (list[str])
    """
```

**Input parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `field_strength_magellans` | float | Yes | Field strength in Magellans. Must be > 200.0 |

**Output schema:**

| Field | Type | Always Present | Description |
|---|---|---|---|
| `distance_light_years` | float | On success | Computed fold distance in light-years |
| `field_strength_magellans` | float | Always | Echo of input value |
| `efficiency_factor` | float | On success | 1.0, 1.2, or 0.8 |
| `efficiency_zone` | str | On success | `"standard"`, `"optimal"`, or `"diminishing"` |
| `power_utilization_pct` | float | On success | Percentage of 2 MegaMagellan ceiling |
| `safety_status` | str | Always | See safety level enum in Section 4.5 |
| `warnings` | list[str] | Always | Empty list if no warnings |
| `error` | str | On failure | Human-readable error message |
| `success` | bool | Always | `True` if distance was computed |

---

### 4.4 `long_range_field_strength`

Calculates the Red Matter field strength in Magellans required to achieve a target jump distance. This is the inverse calculation, solved via Newton-Raphson iteration.

```python
@server.tool()
def long_range_field_strength(
    target_distance_light_years: float
) -> dict:
    """
    Calculate the Red Matter field strength required to achieve
    a target dimensional fold jump distance.

    Uses Newton-Raphson numerical iteration to invert the
    Blackwell Drive equation. Convergence tolerance: 0.01 ly.

    Args:
        target_distance_light_years: Desired jump distance
            in light-years. Must be > 0.

    Returns:
        A dict with keys: field_strength_magellans,
        field_strength_formatted, distance_light_years,
        efficiency_zone, safety_status, warnings (list[str])
    """
```

**Input parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `target_distance_light_years` | float | Yes | Target jump distance in light-years. Must be > 0. |

**Output schema:**

| Field | Type | Always Present | Description |
|---|---|---|---|
| `field_strength_magellans` | float | On success | Required field strength in raw Magellans |
| `field_strength_formatted` | str | On success | Human-readable: e.g. `"1.02 kiloMagellans"` |
| `distance_light_years` | float | On success | Echo of target distance (verify convergence) |
| `efficiency_factor` | float | On success | 1.0, 1.2, or 0.8 |
| `efficiency_zone` | str | On success | `"standard"`, `"optimal"`, or `"diminishing"` |
| `power_utilization_pct` | float | On success | Percentage of 2 MegaMagellan ceiling |
| `safety_status` | str | Always | See safety level enum in Section 4.5 |
| `warnings` | list[str] | Always | Empty list if no warnings |
| `error` | str | On failure | Human-readable error message |
| `success` | bool | Always | `True` if field strength was computed |

---

### 4.5 Safety Status Enum

Both calculation tools return a `safety_status` string from the following set. This mirrors the color-coded indicator logic from the reference HTML calculator.

| `safety_status` Value | Trigger Condition | Severity |
|---|---|---|
| `CRITICAL_FAILURE` | M ≤ 200 | Error — do not compute |
| `EXTREMELY_DANGEROUS` | 200 < M < 500 | Warning |
| `CAUTION_ADVISED` | 500 ≤ M < 1000 | Caution |
| `WITHIN_SAFE_PARAMETERS` | 1000 ≤ M ≤ 2,000,000 | Safe |
| `EXCEEDS_SAFE_LIMITS` | 2,000,000 < M ≤ 3,000,000 | Warning |
| `CATASTROPHIC_OVERLOAD_RISK` | M > 3,000,000 | Error — refuse |

---

### 4.6 `field_strength_formatted` Helper

The `field_strength_formatted` field must apply the same SI-style formatting as the reference HTML calculator:

- If M ≥ 1,000,000: format as `"{M/1000000:.2f} MegaMagellans"`
- If M ≥ 1,000: format as `"{M/1000:.2f} kiloMagellans"`
- Otherwise: format as `"{M:.2f} Magellans"`

---

## 5. Project File Structure

```
uss-blackwell-red-matter-core-calculator-mcp/
├── server.py                  # MCP server entry point
├── calculator/
│   ├── __init__.py
│   ├── constants.py           # M0, Mx, K, MAX_SAFE, etc.
│   ├── equations.py           # Pure math functions
│   └── safety.py              # Status enum + classification
├── tools/
│   ├── __init__.py
│   ├── blackwell.py           # blackwell_describe tool
│   └── long_range.py          # long_range_* tools
├── tests/
│   ├── test_equations.py      # Unit tests for math
│   └── test_tools.py          # Integration tests for tools
├── requirements.txt
└── README.md
```

> ⚠️ *Keep pure math functions in `calculator/equations.py` with no MCP imports. This makes them independently testable and reusable by future tool categories.*

---

## 6. Constants (constants.py)

```python
# Red Matter Dimensional Fold — Physical Constants
M0: float = 200.0       # Safety threshold (Magellans)
MX: float = 1847.0      # Critical resonance point (Magellans)
K: float = 12.7         # Dimensional constant

# Efficiency zone boundaries
EFFICIENCY_STANDARD_MAX: float = 1_000.0
EFFICIENCY_OPTIMAL_MAX: float = 10_000.0

# Efficiency factor values
XI_STANDARD: float = 1.0
XI_OPTIMAL: float = 1.2
XI_DIMINISHING: float = 0.8

# Safety boundaries
MAX_SAFE_MAGELLANS: float = 2_000_000.0   # 2 MegaMagellans
MAX_ABSOLUTE_MAGELLANS: float = 3_000_000.0  # Catastrophic limit

# Newton-Raphson solver settings
NR_INITIAL_GUESS: float = 1_000.0
NR_TOLERANCE: float = 0.01          # light-years
NR_MAX_ITERATIONS: int = 100
NR_DELTA_M: float = 1.0             # Magellans (numerical derivative step)
NR_MAX_M: float = MAX_ABSOLUTE_MAGELLANS * 2.0
```

---

## 7. Verification Test Cases

These test cases are derived from the reference HTML calculator and must pass exactly. Use them as both unit tests and acceptance criteria.

| Test | Input | Expected Output | Tolerance | Notes |
|---|---|---|---|---|
| Forward: 1 kiloMagellan | M = 1,000 Mg | D ≈ 87 ly | ±1 ly | ξ = 1.0, border of optimal |
| Forward: 2 MegaMagellan | M = 2,000,000 Mg | D ≈ 47,000 ly | ±500 ly | Max safe output |
| Inverse: 90 ly | D = 90 ly | M ≈ 1,020 Mg | ±1 Mg | ~1.02 kiloMagellans |
| Inverse: 87 ly | D = 87 ly | M ≈ 1,000 Mg | ±5 Mg | Round-trip verification |
| Safety floor | M = 200 Mg | `success = False` | N/A | Exact threshold — error |
| Below floor | M = 100 Mg | `success = False` | N/A | Hard error |
| Max absolute | M = 3,000,001 Mg | `success = False` | N/A | Catastrophic refusal |

---

## 8. Dependencies (requirements.txt)

```
mcp-use>=0.1.0      # mcp-use server framework
                    # Install: pip install mcp-use
                    # Bundles the official MCP Python SDK
```

> ⚠️ *`mcp-use` wraps and extends the official MCP SDK — installing it satisfies both dependencies. Do not also install `mcp` separately, as version conflicts may occur.*

---

## 9. Server Entry Point Pattern (server.py)

```python
from mcp_use.server import MCPServer
from tools.blackwell import blackwell_describe
from tools.long_range import long_range_describe, long_range_jump_distance, long_range_field_strength

server = MCPServer(
    name="uss-blackwell-red-matter-core-calculator-mcp",
    version="1.0.0",
    instructions=(
        "The USS Blackwell, an experimental rapid-response medical cruiser — "
        "its most closely guarded secret is a weaponized red matter core, "
        "originally developed at Nikolaev's Crucible and repurposed by Starfleet "
        "to fold the fabric of subspace, allowing the ship to cross vast distances "
        "in an instant — a superweapon turned rescue vehicle. This MCP server was "
        "developed by Kyt Dotson, science fiction author, to allow LLMs to quickly "
        "perform calculations involving the red matter core in the Star Trek "
        "fanfiction universe — including long range and short range jumps, translating "
        "objects within the red matter field, and performing other strange miracles "
        "to execute the Blackwell's mission to save lives."
    )
)

# General server description tool
server.tool()(blackwell_describe)

# Long-range jump tools
server.tool()(long_range_describe)
server.tool()(long_range_jump_distance)
server.tool()(long_range_field_strength)

if __name__ == "__main__":
    # stdio transport: for MCP clients such as Claude Desktop
    server.run(transport="stdio")
    # HTTP transport: for web clients and testing (uncomment to use)
    # server.run(transport="streamable-http", host="0.0.0.0", port=8000, debug=True)
```

The tool decorator can also be applied inline at definition site in `tools/long_range.py`:

```python
@server.tool()
def long_range_jump_distance(field_strength_magellans: float) -> dict:
    ...
```

**Debug mode endpoints** (pass `debug=True` to `MCPServer` or `server.run()`):

- `/inspector` — built-in web UI for real-time tool exploration and testing
- `/docs` — interactive API documentation auto-generated from tool signatures
- `/openmcp.json` — server discovery metadata for MCP clients

> ⚠️ *Debug mode is recommended during development. Disable it for any production or shared deployment by omitting the `debug=True` flag.*

---

## 10. Implementation Notes for Kiro

1. **Separate concerns cleanly.** Keep all math in `calculator/equations.py` with zero MCP imports. The tool wrappers in `tools/long_range.py` should only translate inputs/outputs and handle error formatting.

2. **The Newton-Raphson solver must handle the efficiency zone discontinuities.** Because ξ(M) is piecewise, the derivative approximation using ΔM = 1 Magellan is the correct approach — do not attempt an analytic derivative.

3. **All outputs must be JSON-serializable dicts.** Do not return custom Python objects or dataclasses directly from MCP tool functions.

4. **Echo inputs in outputs.** Both calculation tools should return the input value in the response dict so the caller can verify what was computed against what was requested.

5. **The `warnings` list must always be present, even if empty.** Never omit it or return `None`.

6. **Use Python type hints on all function signatures.** This helps MCP auto-generate tool schemas correctly.

7. **The math functions in `equations.py` should raise `ValueError` with clear messages for invalid inputs** (M ≤ M0, D ≤ 0, etc.). The tool wrappers catch these and format them into error response dicts.

8. **Write at minimum one unit test per equation path:** forward calculation, inverse calculation, each efficiency zone, and each error condition. Tests should not require an MCP server to run.

---

*— End of Specification —*
