# USS Blackwell Red Matter Core MCP Server

A Python-based Model Context Protocol server that exposes Red Matter dimensional fold calculation functions for the USS Blackwell fanfiction universe.

## Overview

The USS Blackwell (NX-8091-B) is equipped with a weaponized red matter core that folds subspace for dimensional jumps. This MCP server provides tools for calculating long-range jump distances and required field strengths using the Blackwell Drive equation, with proper safety boundaries and efficiency zone handling.

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

### Setup

1. Clone the repository or download the source code

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Server

Start the MCP server with stdio transport:

```bash
python server.py
```

For debug mode with inspector and documentation endpoints:

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

Add to your Claude Desktop MCP configuration:

```json
{
  "mcpServers": {
    "uss-blackwell": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "transport": "stdio"
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
