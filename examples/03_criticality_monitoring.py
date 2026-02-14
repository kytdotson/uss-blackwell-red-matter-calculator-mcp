"""
Example 3: Criticality Monitoring

This example demonstrates continuous criticality monitoring during extended
tactical operations. The USS Blackwell has been conducting tactical jumps
over an extended period and needs to assess when core de-energization is
required.

Scenario:
- Core has been energized for 8 minutes
- 3 tactical jumps have been performed
- Monitoring criticality progression
- Estimating time to critical thresholds
- Planning safe operational window
"""

from tools.short_range import short_range_criticality


def criticality_monitoring_example():
    """Demonstrate criticality monitoring and threshold tracking."""
    
    print("=" * 80)
    print("EXAMPLE 3: CRITICALITY MONITORING")
    print("=" * 80)
    print()
    
    print("SCENARIO: Extended tactical operations - criticality assessment")
    print()
    
    # Operational parameters
    cochrane_field = 350.0
    phase_offset = 0.75
    subspace_resonance = 47.23
    magellan_field = 500.0  # Typical tactical field strength
    
    print(f"System parameters:")
    print(f"  Cochrane field: {cochrane_field} millicochranes")
    print(f"  Phase offset: {phase_offset}")
    print(f"  Subspace resonance: {subspace_resonance} THz")
    print(f"  Magellan field: {magellan_field} Magellans")
    print()
    
    # Monitor criticality at different operational states
    monitoring_points = [
        {"time": 2.0, "jumps": 1, "description": "After first jump"},
        {"time": 5.0, "jumps": 2, "description": "After second jump"},
        {"time": 8.0, "jumps": 3, "description": "After third jump"},
        {"time": 10.0, "jumps": 4, "description": "Projected: fourth jump"},
        {"time": 12.0, "jumps": 5, "description": "Projected: fifth jump"},
    ]
    
    print("-" * 80)
    print("CRITICALITY PROGRESSION")
    print("-" * 80)
    print()
    
    for point in monitoring_points:
        print(f"{point['description']} (t={point['time']} min, n={point['jumps']})")
        print("-" * 40)
        
        result = short_range_criticality(
            energization_time_minutes=point['time'],
            jump_count=point['jumps'],
            magellan_field=magellan_field,
            cochrane_field=cochrane_field,
            phase_offset=phase_offset,
            subspace_resonance=subspace_resonance
        )
        
        if not result["success"]:
            print(f"✗ ERROR: {result['error']}")
            continue
        
        crit = result['criticality']
        print(f"  Total criticality: {crit['total']:.6f}")
        print(f"    Red matter: {crit['red_matter_component']:.6f}")
        print(f"    Warp core: {crit['warp_core_component']:.6f}")
        print(f"    Interaction: {crit['interaction_factor']:.4f}")
        print(f"  Level: {crit['level']}")
        print(f"  Status: {crit['status_message']}")
        print()
        
        # Show threshold proximity
        thresholds = result['thresholds']
        print("  Threshold status:")
        for name, data in thresholds.items():
            if data['reached']:
                print(f"    {name.upper()}: ✗ REACHED")
            elif data['time_to_minutes'] is not None:
                print(f"    {name.upper()}: {data['time_to_minutes']:.2f} minutes away")
            else:
                print(f"    {name.upper()}: Safe")
        print()
        
        # Operational context
        ops = result['operational_context']
        print(f"  Jumps remaining (estimate): {ops['jumps_remaining_estimate']}")
        print()
        
        # Show warnings
        if result['warnings']:
            print("  ⚠ WARNINGS:")
            for warning in result['warnings']:
                print(f"    - {warning}")
            print()
        
        # Show recommendations
        if result['recommendations']:
            print("  RECOMMENDATIONS:")
            for rec in result['recommendations']:
                print(f"    • {rec}")
            print()
        
        print()
    
    # Detailed analysis at current state (8 minutes, 3 jumps)
    print("=" * 80)
    print("DETAILED ANALYSIS: CURRENT STATE")
    print("=" * 80)
    print()
    
    current_time = 8.0
    current_jumps = 3
    
    result = short_range_criticality(
        energization_time_minutes=current_time,
        jump_count=current_jumps,
        magellan_field=magellan_field,
        cochrane_field=cochrane_field,
        phase_offset=phase_offset,
        subspace_resonance=subspace_resonance
    )
    
    if result["success"]:
        print(f"Current operational state:")
        print(f"  Energization time: {current_time} minutes")
        print(f"  Jumps performed: {current_jumps}")
        print(f"  Total criticality: {result['criticality']['total']:.6f}")
        print(f"  Criticality level: {result['criticality']['level']}")
        print()
        
        print("Time to critical thresholds:")
        for name, data in result['thresholds'].items():
            if not data['reached'] and data['time_to_minutes'] is not None:
                print(f"  {name.upper()}: {data['time_to_minutes']:.2f} minutes")
                print(f"    (at t={current_time + data['time_to_minutes']:.2f} minutes)")
        print()
        
        # Calculate safe operational window
        warning_threshold = result['thresholds']['warning']
        if not warning_threshold['reached'] and warning_threshold['time_to_minutes']:
            safe_window = warning_threshold['time_to_minutes']
            print(f"Safe operational window: {safe_window:.2f} minutes")
            print(f"  Can perform approximately {result['operational_context']['jumps_remaining_estimate']} more jumps")
            print(f"  Recommend de-energization before t={current_time + safe_window:.2f} minutes")
        else:
            print("⚠ WARNING threshold reached or imminent")
            print("  Recommend immediate core de-energization")
        print()
    
    # Simulate criticality growth over time
    print("=" * 80)
    print("CRITICALITY GROWTH PROJECTION")
    print("=" * 80)
    print()
    
    print("Time (min) | Jumps | Criticality | Level")
    print("-" * 50)
    
    for t in range(0, 16, 2):
        jumps = min(t // 2, 7)  # Assume one jump every 2 minutes
        
        result = short_range_criticality(
            energization_time_minutes=float(t),
            jump_count=jumps,
            magellan_field=magellan_field,
            cochrane_field=cochrane_field,
            phase_offset=phase_offset,
            subspace_resonance=subspace_resonance
        )
        
        if result["success"]:
            crit_val = result['criticality']['total']
            level = result['criticality']['level']
            print(f"{t:10.1f} | {jumps:5d} | {crit_val:11.6f} | {level}")
    
    print()
    print("=" * 80)
    print("CONCLUSION:")
    print("  Criticality increases exponentially with time and jump count.")
    print("  Current state (8 min, 3 jumps) is in NOMINAL range.")
    print("  WARNING threshold will be reached in approximately 4-5 minutes.")
    print("  Recommend planning core de-energization within safe window.")
    print("  Maximum safe operation: ~12 minutes or 5-6 jumps.")
    print("=" * 80)


if __name__ == "__main__":
    criticality_monitoring_example()
