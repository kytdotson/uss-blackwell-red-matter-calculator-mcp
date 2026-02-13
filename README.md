# USS Blackwell Red Matter Core MCP Server

A Python-based Model Context Protocol server that exposes Red Matter dimensional fold calculation functions for the USS Blackwell fanfiction universe.

## Overview

The USS Blackwell (NX-8091-B) is equipped with a weaponized red matter core that folds subspace for dimensional jumps. This MCP server provides tools for calculating long-range jump distances and required field strengths using the Blackwell Drive equation, with proper safety boundaries and efficiency zone handling.

## Resources

Original JavaScript and HTML calculation pages are [available online](https://crystalia.net/kitsune/blackwell/red_matter_calculator.html).

Fanfiction universe available on Archive of Our Own (AO3) at [Star Trek: Blackwell by Kyt Dotson](https://archiveofourown.org/series/1512200).

## Features

- **Forward Calculation**: Calculate jump distance from field strength
- **Inverse Calculation**: Calculate required field strength for target distance
- **Safety Classification**: Automatic safety status assessment
- **Efficiency Zones**: Handles standard, optimal, and diminishing efficiency ranges
- **Newton-Raphson Solver**: Numerical inverse calculation with convergence guarantees

## Installation

### Requirements

- Python 3.10 or higher
- pip package manager

### Current Option: Install from source

1. Clone the repository or download the source code

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Server

**For running from source:**
```bash
python server.py
```

**For debug mode with inspector and documentation endpoints:**
```bash
python server.py --debug
```

### Available Tools

The server exposes 4 MCP tools:

1. **blackwell_describe**: Get server information and available tools
2. **long_range_describe**: Get detailed documentation on the long-range jump system
3. **long_range_jump_distance**: Calculate jump distance from field strength
4. **long_range_field_strength**: Calculate required field strength for target distance

### Example Usage with Claude Desktop

Add to your Claude Desktop MCP configuration (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS or `%APPDATA%\Claude\claude_desktop_config.json` on Windows):

**If running from source:**
```json
{
  "mcpServers": {
    "uss-blackwell": {
      "command": "C:\\Users\\Kyt\\uss-blackwell-red-matter-calculator-mcp\\start_server.bat"
    }
  }
}
```

## Mathematical Background

### The Blackwell Drive Equation

```
D = K × ln(M − M₀) × √(M / Mₓ) × ξ(M)
```

Where:
- **D**: Jump distance (light-years)
- **M**: Field strength (Magellans)
- **M₀**: Safety threshold (200 Magellans)
- **Mₓ**: Critical resonance point (1847 Magellans)
- **K**: Dimensional constant (12.7)
- **ξ(M)**: Efficiency factor (piecewise function)

### Efficiency Zones

- **Standard** (M < 1,000): ξ = 1.0
- **Optimal** (1,000 ≤ M < 10,000): ξ = 1.2
- **Diminishing** (M ≥ 10,000): ξ = 0.8

### Safety Boundaries

- **CRITICAL_FAILURE**: M ≤ 200
- **EXTREMELY_DANGEROUS**: 200 < M < 500
- **CAUTION_ADVISED**: 500 ≤ M < 1,000
- **WITHIN_SAFE_PARAMETERS**: 1,000 ≤ M ≤ 2,000,000
- **EXCEEDS_SAFE_LIMITS**: 2,000,000 < M ≤ 3,000,000
- **CATASTROPHIC_OVERLOAD_RISK**: M > 3,000,000

## Testing

### Run Unit Tests

```bash
pytest tests/ -v
```

### Run Property-Based Tests

```bash
pytest tests/test_properties.py -v --hypothesis-show-statistics
```

### Generate Coverage Report

```bash
pytest --cov=calculator --cov=tools --cov-report=html
```

## Project Structure

```
uss-blackwell-mcp-server/
├── calculator/              # Pure mathematical functions
│   ├── __init__.py
│   ├── constants.py        # Physical constants and parameters
│   ├── equations.py        # Forward/inverse calculations
│   └── safety.py           # Safety classification
├── tools/                   # MCP tool wrappers
│   ├── __init__.py
│   ├── blackwell.py        # Server description tool
│   └── long_range.py       # Long-range calculation tools
├── tests/                   # Test suite
│   ├── __init__.py
│   ├── test_equations.py   # Unit tests for equations
│   ├── test_safety.py      # Unit tests for safety
│   ├── test_tools.py       # Unit tests for MCP tools
│   └── test_properties.py  # Property-based tests
├── server.py               # MCP server entry point
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## License

This is a fanfiction project for entertainment purposes.

## Credits

Based on the USS Blackwell fanfiction universe.
# USS Blackwell NX-8091-B — Red Matter Core Calculator
### `uss-blackwell-red-matter-core-calculator-mcp`

An MCP server for the USS Blackwell NX-8091-B — exposes red matter core calculations for LLMs, including long-range dimensional fold jump distance and field strength tools for a Star Trek fanfiction universe.

> *The USS Blackwell, an experimental rapid-response medical cruiser — its most closely guarded secret is a weaponized red matter core, originally developed at Nikolaev's Crucible and repurposed by Starfleet to fold the fabric of subspace, allowing the ship to cross vast distances in an instant — a superweapon turned rescue vehicle.*
>
> — Kyt Dotson, *USS Blackwell* series

---

## Overview

This MCP server implements the Red Matter Dimensional Fold Drive equations from the *USS Blackwell* Star Trek fanfiction universe, allowing LLMs to perform accurate, consistent calculations across any scene or story involving the Blackwell's jump drive. Field strength, jump distance, safety thresholds, and efficiency zones are all enforced mathematically so the numbers stay canon-consistent no matter which tool call produces them.

**Built with** [`mcp-use`](https://mcp-use.com) · Python 3.10+

---

## The Equation

The core dimensional fold equation governing all long-range jump calculations:

```
D  =  K × ln(M − M₀) × √(M / Mₓ) × ξ(M)
```

| Symbol | Meaning | Value |
|---|---|---|
| `D` | Jump distance (light-years) | Output |
| `M` | Field strength (Magellans) | Input |
| `M₀` | Safety threshold | 200 Magellans |
| `Mₓ` | Critical resonance point | 1,847 Magellans |
| `K` | Dimensional constant | 12.7 |
| `ξ(M)` | Efficiency factor | 1.0 / 1.2 / 0.8 (piecewise) |

**The Magellan** is the scalar unit of red matter field output strength, ordinarily measured as M per m³ of subspace flexure density [F:j,i,k], but for jump calculations it is measured directly at the core.

---

## Available Tools

| Tool | Description |
|---|---|
| `blackwell_describe` | Server narrative, lore, and capability overview |
| `long_range_describe` | Magellan unit definition, equation reference, efficiency zones, and safety boundaries |
| `long_range_jump_distance` | Calculate jump distance (light-years) from a given field strength (Magellans) |
| `long_range_field_strength` | Calculate required field strength (Magellans) for a target jump distance (light-years) |

Additional calculation categories are planned (`short_range`, `core_output`, `near_field`, `subspace`, `displacement`) and will be added as the server grows.

---

## Installation

```bash
pip install mcp-use
```

Clone the repository:

```bash
git clone https://github.com/your-username/uss-blackwell-red-matter-core-calculator-mcp.git
cd uss-blackwell-red-matter-core-calculator-mcp
pip install -r requirements.txt
```

---

## Running the Server

**stdio** (for MCP clients such as Claude Desktop):
```bash
python server.py
```

**HTTP** (for web clients and local testing):
```python
# In server.py, swap the run call to:
server.run(transport="streamable-http", host="0.0.0.0", port=8000, debug=True)
```

With `debug=True` the following endpoints are available at `http://localhost:8000`:

- `/inspector` — live tool explorer and test UI
- `/docs` — auto-generated interactive API documentation
- `/openmcp.json` — server discovery metadata

---

## Quick Examples

**How far can the Blackwell jump at 1 kiloMagellan?**
```
Tool: long_range_jump_distance
Input: { "field_strength_magellans": 1000 }
Output: ~87 light-years  (ξ = 1.0, WITHIN_SAFE_PARAMETERS)
```

**What field strength is needed to reach DS9 from Earth (~40 light-years)?**
```
Tool: long_range_field_strength
Input: { "target_distance_light_years": 40 }
Output: ~583 Magellans  (ξ = 1.0, CAUTION_ADVISED)
```

**Maximum safe cross-quadrant jump:**
```
Tool: long_range_jump_distance
Input: { "field_strength_magellans": 2000000 }
Output: ~47,000 light-years  (ξ = 0.8, WITHIN_SAFE_PARAMETERS)
```

---

## Safety Zones

| Status | Field Strength Range | Notes |
|---|---|---|
| `CRITICAL_FAILURE` | ≤ 200 Mg | Equation undefined — hard error |
| `EXTREMELY_DANGEROUS` | 201–499 Mg | Result returned with warning |
| `CAUTION_ADVISED` | 500–999 Mg | Operational but suboptimal |
| `WITHIN_SAFE_PARAMETERS` | 1,000–2,000,000 Mg | Normal operating range |
| `EXCEEDS_SAFE_LIMITS` | 2,000,001–3,000,000 Mg | Manual override required |
| `CATASTROPHIC_OVERLOAD_RISK` | > 3,000,000 Mg | Refused — no calculation returned |

---

## Project Structure

```
uss-blackwell-red-matter-core-calculator-mcp/
├── server.py                  # Entry point
├── calculator/
│   ├── constants.py           # All named constants
│   ├── equations.py           # Pure math — no MCP imports
│   └── safety.py              # Status enum and classification logic
├── tools/
│   ├── blackwell.py           # blackwell_describe
│   └── long_range.py          # long_range_* tools
├── tests/
│   ├── test_equations.py
│   └── test_tools.py
├── requirements.txt
└── README.md
```

---

## About

Part of the *USS Blackwell* Star Trek fanfiction universe by **Kyt Dotson**. The Blackwell is an experimental rapid-response medical cruiser whose weaponized red matter core — originally developed at Nikolaev's Crucible — was repurposed by Starfleet as a dimensional fold drive, turning a superweapon into a rescue vehicle capable of crossing quadrants in an instant.

This MCP server was developed to allow LLMs to perform consistent, canon-accurate calculations within that universe.

---

*Specification and implementation by Kyt Dotson · Not affiliated with Paramount or the official Star Trek franchise*
