"""
Example 2: Sequential Jump Planning

This example demonstrates planning a sequence of tactical jumps during a combat
scenario. The USS Blackwell needs to perform multiple repositioning maneuvers
while tracking cumulative criticality buildup.

Scenario:
- Combat evasion requiring 4 tactical jumps
- Each jump: varying distances based on tactical needs
- Time between jumps: 3 seconds (minimal delay)
- Standard parameters with optimal settings
- Monitor criticality buildup across sequence
"""

from tools.short_range import short_range_sequential_jumps, short_range_criticality


def sequential_jump_planning_example():
    """Demonstrate sequential jump planning with criticality tracking."""
    
    print("=" * 80)
    print("EXAMPLE 2: SEQUENTIAL JUMP PLANNING")
    print("=" * 80)
    print()
    
    print("SCENARIO: Combat evasion - multiple tactical repositioning jumps")
    print()
    
    # Define jump sequence
    jump_sequence = [
        {"distance_meters": 25000, "charge_time_minutes": 1.5},  # Quick dodge
        {"distance_meters": 40000, "charge_time_minutes": 2.0},  # Reposition
        {"distance_meters": 15000, "charge_time_minutes": 1.0},  # Fine adjustment
        {"distance_meters": 60000, "charge_time_minutes": 2.5},  # Final position
    ]
    
    print("Planned jump sequence:")
    for i, jump in enumerate(jump_sequence, 1):
        print(f"  Jump {i}: {jump['distance_meters']:,} m ({jump['distance_meters']/1000:.1f} km) "
              f"- charge {jump['charge_time_minutes']} min")
    print()
    
    # Standard parameters
    cochrane_field = 350.0
    phase_offset = 0.75
    subspace_resonance = 47.23
    time_between_jumps = 3.0  # seconds
    
    print(f"Parameters:")
    print(f"  Cochrane field: {cochrane_field} millicochranes")
    print(f"  Phase offset: {phase_offset}")
    print(f"  Subspace resonance: {subspace_resonance} THz")
    print(f"  Time between jumps: {time_between_jumps} seconds")
    print()
    
    # Analyze the sequence
    print("-" * 80)
    print("SEQUENCE ANALYSIS")
    print("-" * 80)
    
    result = short_range_sequential_jumps(
        jump_sequence=jump_sequence,
        time_between_jumps_seconds=time_between_jumps,
        cochrane_field=cochrane_field,
        phase_offset=phase_offset,
        subspace_resonance=subspace_resonance
    )
    
    if not result["success"]:
        print(f"✗ ERROR: {result['error']}")
        return
    
    # Display sequence analysis
    analysis = result["sequence_analysis"]
    print(f"Total jumps requested: {analysis['total_jumps_requested']}")
    print(f"Jumps feasible: {analysis['jumps_feasible']}")
    print(f"Total energization time: {analysis['total_energization_time_minutes']:.2f} minutes")
    print(f"Sequence safe: {'YES' if analysis['sequence_safe'] else 'NO'}")
    
    if analysis['critical_jump_index'] is not None:
        print(f"⚠ Critical jump: #{analysis['critical_jump_index']} (first unsafe)")
    print()
    
    # Display individual jump results
    print("-" * 80)
    print("INDIVIDUAL JUMP RESULTS")
    print("-" * 80)
    
    for jump_result in result["jump_results"]:
        jump_num = jump_result["jump_number"]
        print(f"\nJump #{jump_num}:")
        print(f"  Distance: {jump_result['distance_meters']:,} m ({jump_result['distance_meters']/1000:.1f} km)")
        print(f"  Required field: {jump_result['field_strength_magellans']:.2f} Magellans")
        print(f"  Criticality after: {jump_result['criticality_after_jump']:.6f} ({jump_result['criticality_level']})")
        print(f"  Safe to proceed: {'YES' if jump_result['safe_to_proceed'] else 'NO'}")
        
        if jump_result['warnings']:
            print(f"  ⚠ Warnings:")
            for warning in jump_result['warnings']:
                print(f"    - {warning}")
    
    print()
    
    # Display final state
    print("-" * 80)
    print("FINAL STATE")
    print("-" * 80)
    
    final = result["final_state"]
    print(f"Total criticality: {final['total_criticality']:.6f}")
    print(f"Criticality level: {final['criticality_level']}")
    print(f"Core status: {final['core_status']}")
    
    if final['recovery_time_estimate_minutes']:
        print(f"Recovery time estimate: {final['recovery_time_estimate_minutes']:.1f} minutes")
    print()
    
    # Display recommendations
    if result['recommendations']:
        print("-" * 80)
        print("TACTICAL RECOMMENDATIONS")
        print("-" * 80)
        for rec in result['recommendations']:
            print(f"  • {rec}")
        print()
    
    # Additional criticality check at end of sequence
    print("-" * 80)
    print("DETAILED CRITICALITY ASSESSMENT")
    print("-" * 80)
    
    total_time = analysis['total_energization_time_minutes']
    total_jumps = analysis['jumps_feasible']
    
    # Use the field strength from the last jump
    last_field = result["jump_results"][-1]["field_strength_magellans"] if result["jump_results"] else 500.0
    
    crit_result = short_range_criticality(
        energization_time_minutes=total_time,
        jump_count=total_jumps,
        magellan_field=last_field,
        cochrane_field=cochrane_field,
        phase_offset=phase_offset,
        subspace_resonance=subspace_resonance
    )
    
    if crit_result["success"]:
        print(f"Total criticality: {crit_result['criticality']['total']:.6f}")
        print(f"  Red matter component: {crit_result['criticality']['red_matter_component']:.6f}")
        print(f"  Warp core component: {crit_result['criticality']['warp_core_component']:.6f}")
        print(f"  Interaction factor: {crit_result['criticality']['interaction_factor']:.4f}")
        print()
        
        print("Threshold status:")
        for threshold_name, threshold_data in crit_result['thresholds'].items():
            status = "REACHED" if threshold_data['reached'] else "Not reached"
            time_to = f" (in {threshold_data['time_to_minutes']:.1f} min)" if threshold_data['time_to_minutes'] else ""
            print(f"  {threshold_name.upper()}: {status}{time_to}")
        print()
        
        print(f"Jumps remaining estimate: {crit_result['operational_context']['jumps_remaining_estimate']}")
    
    print()
    print("=" * 80)
    print("CONCLUSION:")
    if analysis['sequence_safe']:
        print("  All jumps in sequence are feasible and safe.")
        print(f"  Criticality remains at {final['criticality_level']} level.")
        print("  Sequence can proceed as planned.")
    else:
        print(f"  ⚠ Sequence becomes unsafe at jump #{analysis['critical_jump_index']}.")
        print("  Recommend reducing jump count or increasing recovery time.")
        print("  Consider core de-energization after safe jumps.")
    print("=" * 80)


if __name__ == "__main__":
    sequential_jump_planning_example()
