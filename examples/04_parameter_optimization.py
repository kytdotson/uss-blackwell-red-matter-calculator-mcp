"""
Example 4: Parameter Optimization

This example demonstrates optimizing tactical jump parameters for different
operational goals. The USS Blackwell needs to find optimal Cochrane field
settings and adjust phase offset and subspace resonance for maximum efficiency,
safety, or range.

Scenario:
- Mission requires 100 km tactical jump
- Available charge time: 3.0 minutes
- Need to optimize Cochrane field for best efficiency
- Explore different phase offset and resonance settings
- Compare optimization strategies
"""

from tools.short_range import (
    short_range_optimize_cochrane,
    short_range_field_strength,
    short_range_jump_distance
)


def parameter_optimization_example():
    """Demonstrate parameter optimization for different goals."""
    
    print("=" * 80)
    print("EXAMPLE 4: PARAMETER OPTIMIZATION")
    print("=" * 80)
    print()
    
    print("SCENARIO: Optimize parameters for 100 km tactical jump")
    print()
    
    # Mission parameters
    target_distance = 100000.0  # meters (100 km)
    charge_time = 3.0  # minutes
    
    print(f"Mission requirements:")
    print(f"  Target distance: {target_distance/1000:.1f} km")
    print(f"  Available charge time: {charge_time} minutes")
    print()
    
    # Test different parameter combinations
    print("=" * 80)
    print("PART 1: COCHRANE FIELD OPTIMIZATION")
    print("=" * 80)
    print()
    
    # Standard parameters
    phase_offset = 0.75
    subspace_resonance = 47.23
    
    print(f"Base parameters:")
    print(f"  Phase offset: {phase_offset}")
    print(f"  Subspace resonance: {subspace_resonance} THz")
    print()
    
    # Optimize for efficiency
    print("-" * 80)
    print("OPTIMIZATION GOAL: EFFICIENCY")
    print("-" * 80)
    
    result = short_range_optimize_cochrane(
        target_distance_meters=target_distance,
        charge_time_minutes=charge_time,
        phase_offset=phase_offset,
        subspace_resonance=subspace_resonance,
        optimization_goal="efficiency"
    )
    
    if result["success"]:
        print(f"✓ Optimal Cochrane field: {result['optimal_cochrane_field']:.2f} millicochranes")
        print()
        print(f"Safe zones found: {len(result['safe_zones'])}")
        for i, zone in enumerate(result['safe_zones'][:3], 1):  # Show top 3
            print(f"\n  Zone {i}:")
            print(f"    Range: {zone['range_start']:.0f} - {zone['range_end']:.0f} millicochranes")
            print(f"    Average efficiency: {zone['average_efficiency']:.4f}")
            print(f"    Recommended value: {zone['recommended_value']:.2f}")
            if zone['required_field_magellans']:
                print(f"    Required field: {zone['required_field_magellans']:.2f} Magellans")
        print()
        
        if result['recommendations']:
            print("RECOMMENDATIONS:")
            for rec in result['recommendations']:
                print(f"  • {rec}")
            print()
    else:
        print(f"✗ ERROR: {result['error']}")
    
    # Optimize for safety
    print("-" * 80)
    print("OPTIMIZATION GOAL: SAFETY")
    print("-" * 80)
    
    result = short_range_optimize_cochrane(
        target_distance_meters=target_distance,
        charge_time_minutes=charge_time,
        phase_offset=phase_offset,
        subspace_resonance=subspace_resonance,
        optimization_goal="safety"
    )
    
    if result["success"]:
        print(f"✓ Optimal Cochrane field: {result['optimal_cochrane_field']:.2f} millicochranes")
        print(f"  (Prioritizes stable operation over maximum efficiency)")
        print()
    
    # Optimize for range
    print("-" * 80)
    print("OPTIMIZATION GOAL: RANGE")
    print("-" * 80)
    
    result = short_range_optimize_cochrane(
        charge_time_minutes=charge_time,
        phase_offset=phase_offset,
        subspace_resonance=subspace_resonance,
        optimization_goal="range"
    )
    
    if result["success"]:
        print(f"✓ Optimal Cochrane field: {result['optimal_cochrane_field']:.2f} millicochranes")
        print()
        print("Maximum achievable distances by zone:")
        for i, zone in enumerate(result['safe_zones'][:3], 1):
            if zone['achievable_distance_meters']:
                dist_km = zone['achievable_distance_meters'] / 1000
                print(f"  Zone {i}: {dist_km:.2f} km at C={zone['recommended_value']:.0f}")
        print()
    
    # Part 2: Phase offset and resonance exploration
    print("=" * 80)
    print("PART 2: PHASE OFFSET AND RESONANCE EXPLORATION")
    print("=" * 80)
    print()
    
    cochrane_field = 350.0  # Use standard value
    
    # Test different phase offsets
    print("-" * 80)
    print("PHASE OFFSET COMPARISON")
    print("-" * 80)
    print()
    
    phase_offsets = [0.50, 0.65, 0.75, 0.85, 0.95]
    
    print("Phase | Distance (km) | Field (Mg) | Criticality")
    print("-" * 60)
    
    for phi in phase_offsets:
        result = short_range_field_strength(
            target_distance_meters=target_distance,
            charge_time_minutes=charge_time,
            cochrane_field=cochrane_field,
            phase_offset=phi,
            subspace_resonance=subspace_resonance
        )
        
        if result["success"]:
            field = result['field_strength_magellans']
            crit = result['criticality']['total']
            print(f"{phi:5.2f} | {target_distance/1000:13.2f} | {field:10.2f} | {crit:.6f}")
    
    print()
    print("→ Phase offset 0.75 provides optimal stability")
    print()
    
    # Test different subspace resonances
    print("-" * 80)
    print("SUBSPACE RESONANCE COMPARISON")
    print("-" * 80)
    print()
    
    resonances = [25.0, 47.23, 56.5, 72.0, 95.0]  # Optimal and null zones
    
    print("Resonance (THz) | Distance (km) | Field (Mg) | Status")
    print("-" * 70)
    
    for R in resonances:
        result = short_range_field_strength(
            target_distance_meters=target_distance,
            charge_time_minutes=charge_time,
            cochrane_field=cochrane_field,
            phase_offset=phase_offset,
            subspace_resonance=R
        )
        
        if result["success"]:
            field = result['field_strength_magellans']
            feasible = "✓" if result['feasibility']['achievable'] else "✗"
            print(f"{R:15.2f} | {target_distance/1000:13.2f} | {field:10.2f} | {feasible}")
        else:
            print(f"{R:15.2f} | {'N/A':>13} | {'N/A':>10} | ✗")
    
    print()
    print("→ Resonances near 25, 47, 72, 95 THz are optimal zones")
    print("→ Resonance near 56.5 THz is a null zone (avoid)")
    print()
    
    # Part 3: Comprehensive comparison
    print("=" * 80)
    print("PART 3: COMPREHENSIVE PARAMETER COMPARISON")
    print("=" * 80)
    print()
    
    configurations = [
        {"name": "Standard", "C": 350, "phi": 0.75, "R": 47.23},
        {"name": "High Efficiency", "C": 450, "phi": 0.75, "R": 47.23},
        {"name": "Low Power", "C": 250, "phi": 0.75, "R": 47.23},
        {"name": "Alt Resonance", "C": 350, "phi": 0.75, "R": 72.0},
        {"name": "Suboptimal Phase", "C": 350, "phi": 0.50, "R": 47.23},
    ]
    
    print("Configuration      | Field (Mg) | Criticality | Feasible")
    print("-" * 70)
    
    for config in configurations:
        result = short_range_field_strength(
            target_distance_meters=target_distance,
            charge_time_minutes=charge_time,
            cochrane_field=config['C'],
            phase_offset=config['phi'],
            subspace_resonance=config['R']
        )
        
        if result["success"]:
            field = result['field_strength_magellans']
            crit = result['criticality']['total']
            feasible = "✓" if result['feasibility']['achievable'] else "✗"
            print(f"{config['name']:18} | {field:10.2f} | {crit:11.6f} | {feasible:^8}")
        else:
            print(f"{config['name']:18} | {'N/A':>10} | {'N/A':>11} | ✗")
    
    print()
    
    # Final recommendations
    print("=" * 80)
    print("OPTIMIZATION RECOMMENDATIONS")
    print("=" * 80)
    print()
    print("For maximum efficiency:")
    print("  • Use Cochrane field in optimal zones (typically 300-500 or 700-850)")
    print("  • Maintain phase offset at 0.75 for best stability")
    print("  • Select subspace resonance in optimal zones (~25, ~47, ~72, ~95 THz)")
    print("  • Avoid resonance null zones (~0, ~56.5, ~113 THz)")
    print()
    print("For maximum safety:")
    print("  • Use lower Cochrane fields (200-400 millicochranes)")
    print("  • Keep phase offset at 0.75")
    print("  • Use well-tested resonance frequencies (47.23 THz standard)")
    print("  • Monitor criticality closely during operations")
    print()
    print("For maximum range:")
    print("  • Use higher Cochrane fields (600-850 millicochranes)")
    print("  • Optimize resonance for peak modulation")
    print("  • Accept higher criticality risk")
    print("  • Ensure adequate charge time (3+ minutes)")
    print()
    print("=" * 80)


if __name__ == "__main__":
    parameter_optimization_example()
