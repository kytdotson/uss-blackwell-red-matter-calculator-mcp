# Short-Range Tactical Jump Examples

This directory contains comprehensive usage examples for the USS Blackwell short-range tactical jump calculation system. Each example demonstrates different operational scenarios and use cases.

## Running the Examples

### Run All Examples

To run all examples in sequence:

```bash
python examples/run_all_examples.py
```

This will execute each example with pauses between them for review.

### Run Individual Examples

Each example can also be run directly with Python:

```bash
python examples/01_basic_tactical_jump.py
python examples/02_sequential_jump_planning.py
python examples/03_criticality_monitoring.py
python examples/04_parameter_optimization.py
python examples/05_emergency_operations.py
```

**Note:** Ensure the MCP server dependencies are installed:
```bash
pip install -r requirements.txt
```

## Example Overview

### 1. Basic Tactical Jump (`01_basic_tactical_jump.py`)

**Purpose:** Demonstrates fundamental tactical jump calculations

**Scenarios:**
- Forward calculation: What distance can we achieve with given charge time?
- Inverse calculation: What field strength do we need for a target distance?
- Basic parameter usage and result interpretation

**Key Concepts:**
- Charge density integration
- Modulation factors (Cochrane efficiency, resonance modulation, phase coupling)
- Criticality assessment for single jumps
- Standard operational parameters

**Use Case:** Emergency debris avoidance maneuver requiring 50 km repositioning

---

### 2. Sequential Jump Planning (`02_sequential_jump_planning.py`)

**Purpose:** Demonstrates planning multiple tactical jumps with criticality tracking

**Scenarios:**
- Combat evasion requiring 4 consecutive jumps
- Cumulative criticality buildup monitoring
- Sequence feasibility assessment
- Identifying critical jump (first unsafe)

**Key Concepts:**
- Jump sequence analysis
- Exponential criticality growth
- Time-to-threshold estimation
- Safe operational windows
- Recovery time planning

**Use Case:** Combat scenario requiring multiple repositioning maneuvers

---

### 3. Criticality Monitoring (`03_criticality_monitoring.py`)

**Purpose:** Demonstrates continuous criticality monitoring during extended operations

**Scenarios:**
- Tracking criticality progression over time
- Monitoring threshold proximity
- Estimating jumps remaining
- Planning safe de-energization windows

**Key Concepts:**
- Red matter criticality component
- Warp core stress component
- Interaction factors
- Criticality thresholds (WARNING, EJECTION, FAILURE, CATASTROPHIC)
- Exponential growth projection

**Use Case:** Extended tactical operations with 8 minutes energization and 3 jumps performed

---

### 4. Parameter Optimization (`04_parameter_optimization.py`)

**Purpose:** Demonstrates optimizing tactical jump parameters for different goals

**Scenarios:**
- Cochrane field optimization (efficiency, safety, range)
- Phase offset comparison
- Subspace resonance exploration
- Comprehensive parameter comparison

**Key Concepts:**
- Safe Cochrane zones
- Optimal vs. null resonance zones
- Phase offset stability effects
- Efficiency vs. safety vs. range tradeoffs
- Danger zone avoidance

**Use Case:** Optimizing parameters for 100 km tactical jump with 3-minute charge time

---

### 5. Emergency Operations (`05_emergency_operations.py`)

**Purpose:** Demonstrates emergency scenarios requiring rapid risk assessment

**Scenarios:**
1. Minimal charge time jump (30 seconds)
2. High criticality operations (extended combat)
3. Danger zone navigation (suboptimal resonance)
4. Maximum range emergency jump
5. Go/no-go decision matrix

**Key Concepts:**
- Rapid feasibility assessment
- Risk acceptance criteria
- Emergency parameter optimization
- Command override thresholds
- Post-emergency procedures

**Use Case:** Multiple emergency scenarios requiring immediate tactical decisions

---

## Common Parameters

All examples use these standard parameters unless otherwise specified:

- **Cochrane field:** 350 millicochranes (standard tactical setting)
- **Phase offset:** 0.75 (optimal stability)
- **Subspace resonance:** 47.23 THz (optimal zone)
- **Charge time:** 1.5-3.0 minutes (typical tactical range)

## Understanding the Output

### Distance Formatting
- Meters: < 1 km
- Kilometers: 1 km - 1 AU
- Astronomical Units (AU): > 1 AU

### Criticality Levels
- **NOMINAL:** < 0.15 (safe operations)
- **WARNING:** 0.15 - 0.35 (monitor closely)
- **CRITICAL:** 0.35 - 0.75 (ejection required)
- **FAILURE_IMMINENT:** 0.75 - 0.95 (emergency shutdown)
- **CATASTROPHIC:** > 0.95 (evacuate immediately)

### Modulation Factors
- **Cochrane efficiency (η):** Warp field coupling effectiveness
- **Resonance modulation (Ψ):** Local subspace frequency effects
- **Phase-resonance coupling (Ω):** Interaction between phase and resonance

### Feasibility Assessment
- **Achievable:** Can the jump be executed with given parameters?
- **Field within limits:** Is required field strength within operational range?
- **Criticality acceptable:** Is risk level acceptable for operation?

## Integration with MCP Server

These examples use the same tool functions exposed by the MCP server:

- `short_range_describe()` - System documentation
- `short_range_jump_distance()` - Forward calculation
- `short_range_field_strength()` - Inverse calculation
- `short_range_criticality()` - Risk assessment
- `short_range_sequential_jumps()` - Multi-jump planning
- `short_range_optimize_cochrane()` - Parameter optimization

When using these tools through an MCP client (like Claude Desktop), the same calculations and logic apply.

## Narrative Context

These examples are designed for the USS Blackwell Star Trek fanfiction universe. The tactical jump system uses:

- **Red matter core:** Primary energy source with exponential criticality buildup
- **Warp core:** Secondary power contribution with field rise time
- **Cochrane guide field:** Warp field coupling for efficiency
- **Phase offset:** Quantum phase alignment (0.75 optimal)
- **Subspace resonance:** Local subspace frequency tuning

The system enables precision maneuvers within stellar systems (meters to 30 AU) but requires careful management of cumulative quantum scarring effects.

## Further Reading

- **Requirements:** `.kiro/specs/short-range-tactical-jumps/requirements.md`
- **Design:** `.kiro/specs/short-range-tactical-jumps/design.md`
- **Implementation:** `calculator/tactical.py` and `tools/short_range.py`
- **Tests:** `tests/test_tactical_*.py` and `tests/test_short_range_tools.py`

## Contributing

When adding new examples:

1. Follow the existing naming convention (`##_descriptive_name.py`)
2. Include comprehensive docstring explaining the scenario
3. Use clear section headers and output formatting
4. Demonstrate both success and edge cases
5. Provide narrative context for the scenario
6. Include conclusion summary with key takeaways
7. Update this README with the new example

---

*Examples created for the USS Blackwell tactical jump system*  
*Part of the USS Blackwell Star Trek fanfiction universe by Kyt Dotson*
