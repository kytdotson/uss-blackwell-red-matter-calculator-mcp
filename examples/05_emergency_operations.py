"""
Example 5: Emergency Operations

This example demonstrates emergency tactical jump scenarios where the USS
Blackwell must operate outside normal safety parameters. These situations
require rapid risk assessment and decision-making under extreme time pressure.

Scenarios:
1. Minimal charge time jump (emergency evasion)
2. High criticality operations (extended combat)
3. Danger zone navigation (suboptimal resonance)
4. Maximum range emergency jump
5. Go/no-go decision making
"""

from tools.short_range import (
    short_range_jump_distance,
    short_range_field_strength,
    short_range_criticality,
    short_range_optimize_cochrane
)


def emergency_operations_example():
    """Demonstrate emergency tactical jump scenarios and risk assessment."""
    
    print("=" * 80)
    print("EXAMPLE 5: EMERGENCY OPERATIONS")
    print("=" * 80)
    print()
    
    # Scenario 1: Minimal charge time
    print("=" * 80)
    print("SCENARIO 1: EMERGENCY EVASION - MINIMAL CHARGE TIME")
    print("=" * 80)
    print()
    
    print("SITUATION: Incoming weapons fire - immediate jump required")
    print("  Available charge time: 0.5 minutes (30 seconds)")
    print("  Need to clear blast radius: 10 km minimum")
    print()
    
    minimal_charge = 0.5  # minutes
    min_safe_distance = 10000.0  # meters
    
    result = short_range_jump_distance(
        charge_time_minutes=minimal_charge,
        cochrane_field=350.0,
        phase_offset=0.75,
        subspace_resonance=47.23
    )
    
    if result["success"]:
        distance_km = result['distance_meters'] / 1000
        print(f"Achievable distance: {distance_km:.2f} km")
        print(f"Minimum required: {min_safe_distance/1000:.2f} km")
        print()
        
        if result['distance_meters'] >= min_safe_distance:
            print("✓ JUMP FEASIBLE - Sufficient distance achievable")
        else:
            print("✗ JUMP INSUFFICIENT - Distance below minimum safe")
            print(f"  Shortfall: {(min_safe_distance - result['distance_meters'])/1000:.2f} km")
        print()
        
        print(f"Criticality: {result['criticality']['level']}")
        print(f"  Total: {result['criticality']['total']:.6f}")
        print()
        
        if result['warnings']:
            print("⚠ WARNINGS:")
            for warning in result['warnings']:
                print(f"  - {warning}")
            print()
        
        print("DECISION: ", end="")
        if result['distance_meters'] >= min_safe_distance:
            print("EXECUTE JUMP - Risk acceptable given threat")
        else:
            print("INCREASE CHARGE TIME or BOOST COCHRANE FIELD")
    
    print()
    
    # Scenario 2: High criticality operations
    print("=" * 80)
    print("SCENARIO 2: EXTENDED COMBAT - HIGH CRITICALITY")
    print("=" * 80)
    print()
    
    print("SITUATION: Core energized for 10 minutes, 5 jumps performed")
    print("  Need one more tactical jump to complete mission")
    print("  Assess risk of additional jump")
    print()
    
    extended_time = 10.0
    extended_jumps = 5
    
    result = short_range_criticality(
        energization_time_minutes=extended_time,
        jump_count=extended_jumps,
        magellan_field=500.0,
        cochrane_field=350.0,
        phase_offset=0.75,
        subspace_resonance=47.23
    )
    
    if result["success"]:
        crit = result['criticality']
        print(f"Current criticality: {crit['total']:.6f} ({crit['level']})")
        print(f"  Red matter: {crit['red_matter_component']:.6f}")
        print(f"  Warp core: {crit['warp_core_component']:.6f}")
        print()
        
        print("Threshold status:")
        for name, data in result['thresholds'].items():
            if data['reached']:
                print(f"  {name.upper()}: ✗ REACHED")
            elif data['time_to_minutes'] and data['time_to_minutes'] < 5:
                print(f"  {name.upper()}: ⚠ {data['time_to_minutes']:.1f} minutes away")
            else:
                print(f"  {name.upper()}: ✓ Safe")
        print()
        
        print(f"Jumps remaining estimate: {result['operational_context']['jumps_remaining_estimate']}")
        print()
        
        if result['recommendations']:
            print("RECOMMENDATIONS:")
            for rec in result['recommendations']:
                print(f"  • {rec}")
            print()
        
        # Assess one more jump
        print("Risk assessment for one additional jump:")
        next_jump_result = short_range_criticality(
            energization_time_minutes=extended_time + 2.0,  # Assume 2 min charge
            jump_count=extended_jumps + 1,
            magellan_field=500.0,
            cochrane_field=350.0,
            phase_offset=0.75,
            subspace_resonance=47.23
        )
        
        if next_jump_result["success"]:
            next_crit = next_jump_result['criticality']['total']
            print(f"  Projected criticality: {next_crit:.6f}")
            print(f"  Increase: {(next_crit - crit['total']):.6f}")
            print()
            
            if next_crit < 0.35:
                print("DECISION: JUMP AUTHORIZED - Criticality remains below EJECTION threshold")
            elif next_crit < 0.75:
                print("DECISION: JUMP CAUTION - Tertiary core ejection will be required")
            else:
                print("DECISION: JUMP DENIED - Risk of primary core failure too high")
    
    print()
    
    # Scenario 3: Danger zone navigation
    print("=" * 80)
    print("SCENARIO 3: SUBSPACE INTERFERENCE - DANGER ZONE")
    print("=" * 80)
    print()
    
    print("SITUATION: Local subspace disruption forces non-optimal resonance")
    print("  Forced resonance: 56.0 THz (near null zone)")
    print("  Need 30 km jump for mission completion")
    print()
    
    danger_resonance = 56.0  # Near null zone at 56.5
    target_distance = 30000.0  # meters
    
    result = short_range_field_strength(
        target_distance_meters=target_distance,
        charge_time_minutes=2.0,
        cochrane_field=350.0,
        phase_offset=0.75,
        subspace_resonance=danger_resonance
    )
    
    if result["success"]:
        print(f"Required field: {result['field_strength_formatted']}")
        print(f"Feasibility:")
        print(f"  Achievable: {result['feasibility']['achievable']}")
        print(f"  Field within limits: {result['feasibility']['field_within_limits']}")
        print()
        
        if result['danger_zones']:
            print("⚠ DANGER ZONES DETECTED:")
            for danger in result['danger_zones']:
                print(f"  - {danger}")
            print()
        
        if result['recommendations']:
            print("RECOMMENDATIONS:")
            for rec in result['recommendations']:
                print(f"  • {rec}")
            print()
        
        # Try to optimize
        print("Attempting Cochrane optimization to compensate:")
        opt_result = short_range_optimize_cochrane(
            target_distance_meters=target_distance,
            charge_time_minutes=2.0,
            phase_offset=0.75,
            subspace_resonance=danger_resonance,
            optimization_goal="efficiency"
        )
        
        if opt_result["success"] and opt_result['safe_zones']:
            print(f"  Optimal Cochrane: {opt_result['optimal_cochrane_field']:.2f} millicochranes")
            print(f"  Safe zones available: {len(opt_result['safe_zones'])}")
            print()
            print("DECISION: JUMP POSSIBLE with Cochrane optimization")
        else:
            print("  No safe Cochrane zones found")
            print()
            print("DECISION: RECOMMEND DELAY until resonance improves")
    else:
        print(f"✗ ERROR: {result['error']}")
        print()
        print("DECISION: JUMP NOT FEASIBLE - Abort mission or wait for conditions")
    
    print()
    
    # Scenario 4: Maximum range emergency
    print("=" * 80)
    print("SCENARIO 4: MAXIMUM RANGE EMERGENCY JUMP")
    print("=" * 80)
    print()
    
    print("SITUATION: Medical emergency - need maximum tactical range")
    print("  Available charge time: 5.0 minutes")
    print("  Willing to accept elevated criticality")
    print()
    
    # Find optimal parameters for maximum range
    result = short_range_optimize_cochrane(
        charge_time_minutes=5.0,
        phase_offset=0.75,
        subspace_resonance=47.23,
        optimization_goal="range"
    )
    
    if result["success"]:
        print(f"Optimal configuration:")
        print(f"  Cochrane field: {result['optimal_cochrane_field']:.2f} millicochranes")
        print()
        
        if result['safe_zones']:
            best_zone = result['safe_zones'][0]
            max_distance = best_zone['achievable_distance_meters']
            print(f"Maximum achievable distance: {max_distance/1000:.2f} km ({max_distance/1000/149597.871:.4f} AU)")
            print(f"  Using Cochrane: {best_zone['recommended_value']:.2f}")
            print(f"  Zone efficiency: {best_zone['average_efficiency']:.4f}")
            print()
            
            # Check criticality at this configuration
            crit_result = short_range_jump_distance(
                charge_time_minutes=5.0,
                cochrane_field=best_zone['recommended_value'],
                phase_offset=0.75,
                subspace_resonance=47.23
            )
            
            if crit_result["success"]:
                print(f"Criticality assessment:")
                print(f"  Level: {crit_result['criticality']['level']}")
                print(f"  Total: {crit_result['criticality']['total']:.6f}")
                print()
                
                if crit_result['criticality']['total'] < 0.15:
                    print("DECISION: MAXIMUM RANGE JUMP AUTHORIZED")
                    print(f"  Execute at C={best_zone['recommended_value']:.0f}, distance={max_distance/1000:.2f} km")
                else:
                    print("DECISION: MAXIMUM RANGE JUMP REQUIRES COMMAND OVERRIDE")
                    print("  Elevated criticality - medical emergency justification required")
    
    print()
    
    # Scenario 5: Go/No-Go decision matrix
    print("=" * 80)
    print("SCENARIO 5: GO/NO-GO DECISION MATRIX")
    print("=" * 80)
    print()
    
    print("SITUATION: Rapid assessment of multiple emergency options")
    print()
    
    scenarios = [
        {
            "name": "Quick Dodge",
            "distance": 5000,
            "charge": 0.3,
            "C": 350,
            "threat": "Immediate weapons fire"
        },
        {
            "name": "Standard Evasion",
            "distance": 25000,
            "charge": 1.5,
            "C": 350,
            "threat": "Incoming torpedoes"
        },
        {
            "name": "Extended Reposition",
            "distance": 100000,
            "charge": 3.0,
            "C": 450,
            "threat": "Area denial weapon"
        },
        {
            "name": "Maximum Emergency",
            "distance": 500000,
            "charge": 5.0,
            "C": 700,
            "threat": "Stellar event"
        },
    ]
    
    print("Scenario            | Distance | Charge | Feasible | Criticality | Decision")
    print("-" * 90)
    
    for scenario in scenarios:
        result = short_range_field_strength(
            target_distance_meters=scenario['distance'],
            charge_time_minutes=scenario['charge'],
            cochrane_field=scenario['C'],
            phase_offset=0.75,
            subspace_resonance=47.23
        )
        
        if result["success"]:
            feasible = "✓" if result['feasibility']['achievable'] else "✗"
            crit = result['criticality']['total']
            
            if not result['feasibility']['achievable']:
                decision = "NO-GO"
            elif crit < 0.15:
                decision = "GO"
            elif crit < 0.35:
                decision = "CAUTION"
            else:
                decision = "OVERRIDE"
            
            print(f"{scenario['name']:19} | {scenario['distance']/1000:6.1f}km | "
                  f"{scenario['charge']:4.1f}m | {feasible:^8} | {crit:11.6f} | {decision}")
        else:
            print(f"{scenario['name']:19} | {scenario['distance']/1000:6.1f}km | "
                  f"{scenario['charge']:4.1f}m | ✗        | {'N/A':>11} | NO-GO")
    
    print()
    print("Decision criteria:")
    print("  GO: Feasible and criticality < 0.15 (NOMINAL)")
    print("  CAUTION: Feasible but criticality 0.15-0.35 (WARNING)")
    print("  OVERRIDE: Feasible but criticality > 0.35 (requires command authorization)")
    print("  NO-GO: Not feasible with given parameters")
    print()
    
    print("=" * 80)
    print("EMERGENCY OPERATIONS SUMMARY")
    print("=" * 80)
    print()
    print("Key principles for emergency tactical jumps:")
    print()
    print("1. RAPID ASSESSMENT")
    print("   • Calculate feasibility immediately")
    print("   • Assess criticality risk")
    print("   • Identify parameter constraints")
    print()
    print("2. RISK ACCEPTANCE")
    print("   • Minimal charge times increase field requirements")
    print("   • Extended operations elevate criticality exponentially")
    print("   • Danger zones may be unavoidable in emergencies")
    print()
    print("3. OPTIMIZATION UNDER PRESSURE")
    print("   • Use Cochrane optimization for best available options")
    print("   • Accept suboptimal parameters if necessary")
    print("   • Balance mission success against system safety")
    print()
    print("4. CLEAR GO/NO-GO CRITERIA")
    print("   • Feasibility: Can the jump be executed?")
    print("   • Safety: Is criticality acceptable?")
    print("   • Authority: Does situation justify override?")
    print()
    print("5. POST-EMERGENCY PROCEDURES")
    print("   • De-energize core as soon as tactically feasible")
    print("   • Allow quantum scarring recovery time")
    print("   • Assess system integrity before next operation")
    print()
    print("=" * 80)


if __name__ == "__main__":
    emergency_operations_example()
