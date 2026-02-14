"""
Example 1: Basic Tactical Jump

This example demonstrates a simple tactical jump calculation for a short-range
maneuver within a stellar system. The USS Blackwell needs to reposition 50,000
meters (50 km) to avoid debris while maintaining combat readiness.

Scenario:
- Target distance: 50,000 meters (50 km)
- Charge time: 2.0 minutes (standard tactical charge)
- Cochrane field: 350 millicochranes (standard setting)
- Phase offset: 0.75 (optimal stability)
- Subspace resonance: 47.23 THz (optimal zone)
- No previous jumps (fresh energization)
"""

from tools.short_range import short_range_jump_distance, short_range_field_strength


def basic_tactical_jump_example():
    """Demonstrate a basic tactical jump calculation."""
    
    print("=" * 80)
    print("EXAMPLE 1: BASIC TACTICAL JUMP")
    print("=" * 80)
    print()
    
    # Scenario parameters
    charge_time = 2.0  # minutes
    cochrane_field = 350.0  # millicochranes
    phase_offset = 0.75  # optimal
    subspace_resonance = 47.23  # THz, optimal zone
    
    print("SCENARIO: Emergency debris avoidance maneuver")
    print(f"  Charge time: {charge_time} minutes")
    print(f"  Cochrane field: {cochrane_field} millicochranes")
    print(f"  Phase offset: {phase_offset}")
    print(f"  Subspace resonance: {subspace_resonance} THz")
    print()
    
    # Forward calculation: What distance can we achieve?
    print("-" * 80)
    print("FORWARD CALCULATION: Achievable distance")
    print("-" * 80)
    
    result = short_range_jump_distance(
        charge_time_minutes=charge_time,
        cochrane_field=cochrane_field,
        phase_offset=phase_offset,
        subspace_resonance=subspace_resonance
    )
    
    if result["success"]:
        print(f"✓ Distance achievable: {result['distance_formatted']}")
        print(f"  Field strength: {result['field_strength_magellans']:.2f} Magellans")
        print(f"  Charge density: {result['charge_density']:.4f}")
        print()
        print("Modulation factors:")
        print(f"  Cochrane efficiency: {result['modulation_factors']['cochrane_efficiency']:.4f}")
        print(f"  Resonance modulation: {result['modulation_factors']['resonance_modulation']:.4f}")
        print(f"  Phase-resonance coupling: {result['modulation_factors']['phase_resonance_coupling']:.4f}")
        print()
        print(f"Criticality status: {result['criticality']['level']}")
        print(f"  Total: {result['criticality']['total']:.6f}")
        print(f"  Status: {result['criticality']['status_message']}")
        print()
        if result['warnings']:
            print("⚠ WARNINGS:")
            for warning in result['warnings']:
                print(f"  - {warning}")
            print()
    else:
        print(f"✗ ERROR: {result['error']}")
        return
    
    # Inverse calculation: What field strength do we need for 50 km?
    print("-" * 80)
    print("INVERSE CALCULATION: Required field for 50 km jump")
    print("-" * 80)
    
    target_distance = 50000.0  # meters (50 km)
    
    result = short_range_field_strength(
        target_distance_meters=target_distance,
        charge_time_minutes=charge_time,
        cochrane_field=cochrane_field,
        phase_offset=phase_offset,
        subspace_resonance=subspace_resonance
    )
    
    if result["success"]:
        print(f"✓ Required field strength: {result['field_strength_formatted']}")
        print(f"  Target distance: {result['target_distance_formatted']}")
        print()
        print("Feasibility assessment:")
        print(f"  Achievable: {result['feasibility']['achievable']}")
        print(f"  Field within limits: {result['feasibility']['field_within_limits']}")
        print(f"  Criticality acceptable: {result['feasibility']['criticality_acceptable']}")
        print()
        print(f"Criticality after jump: {result['criticality']['level']}")
        print(f"  Total: {result['criticality']['total']:.6f}")
        print()
        if result['recommendations']:
            print("RECOMMENDATIONS:")
            for rec in result['recommendations']:
                print(f"  • {rec}")
            print()
    else:
        print(f"✗ ERROR: {result['error']}")
        return
    
    print("=" * 80)
    print("CONCLUSION:")
    print("  The tactical jump is feasible with standard parameters.")
    print("  Criticality remains in NOMINAL range.")
    print("  No parameter adjustments required.")
    print("=" * 80)


if __name__ == "__main__":
    basic_tactical_jump_example()
