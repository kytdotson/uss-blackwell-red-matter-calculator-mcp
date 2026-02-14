"""
USS Blackwell MCP Server - Long-range jump calculation tools.

This module provides tools for calculating long-range jump distances and
required field strengths using the Blackwell Drive equation.
"""

from tools.models.long_range_models import (
    LongRangeJumpDistanceArgs,
    LongRangeFieldStrengthArgs
)


def long_range_describe() -> dict:
    """
    Describe the long-range jump system and the Magellan unit.
    
    Returns comprehensive reference documentation about the red matter field
    measurement unit, the dimensional fold equation, efficiency zones, safety
    boundaries, and example calculation results.
    
    Returns:
        dict: System reference documentation with the following fields:
            - unit_name (str): Name of the field strength unit
            - unit_symbol (str): Symbol for the unit
            - unit_definition (str): Full definition of the Magellan unit
            - unit_base_measurement (str): Base measurement description
            - unit_jump_measurement (str): Jump measurement description
            - equation (str): The dimensional fold equation
            - equation_variables (dict): Descriptions of equation variables
            - efficiency_zones (list): List of efficiency zone specifications
            - safety_boundaries (list): List of safety boundary specifications
            - example_results (list): Known calculation results for verification
            - success (bool): Always True
    """
    return {
        "unit_name": "Magellan",
        "unit_symbol": "M",
        "unit_definition": (
            "The Magellan (symbol: M) is the unit of red matter field output strength, "
            "named after Ferdinand Magellan, the Portuguese explorer who led the first "
            "expedition to circumnavigate the Earth. In the context of the USS Blackwell's "
            "weaponized red matter core, one Magellan represents the field intensity "
            "required to flex one cubic meter of spacetime across subspace by one Planck length. The unit "
            "scales linearly with the core's power output and is measured at the core's "
            "outer containment field boundary."
        ),
        "unit_metric_prefixes": {
            "Magellans": "M (base unit, < 1,000)",
            "kiloMagellans": "kM (1,000 to 999,999)",
            "MegaMagellans": "MM (≥ 1,000,000)"
        },
        "unit_base_measurement": "M per cubic meter [of subspace flexure density (F:j,i,k)]",
        "unit_jump_measurement": "Measured at the core for jump purposes",
        "equation": "D = K × ln(M − M₀) × √(M / Mₓ) × ξ(M)",
        "equation_formal_name": "Dreiling-Nemêth Subspace Flexure Collapse Equation",
        "equation_informal_name": "Blackwell Drive Equation",
        "equation_variables": {
            "D": "Jump distance in light-years",
            "K": "Dimensional constant (12.7)",
            "M": "Field strength in Magellans",
            "M₀": "Safety threshold (200 Magellans)",
            "Mₓ": "Critical resonance point (1847 Magellans)",
            "ξ(M)": "Efficiency factor (piecewise function: 1.0, 1.2, or 0.8)"
        },
        "efficiency_zones": [
            {
                "range": "M < 1,000",
                "xi_value": 1.0,
                "label": "standard"
            },
            {
                "range": "1,000 ≤ M < 10,000",
                "xi_value": 1.2,
                "label": "optimal"
            },
            {
                "range": "M ≥ 10,000",
                "xi_value": 0.8,
                "label": "diminishing"
            }
        ],
        "safety_boundaries": [
            {
                "range": "M ≤ 200",
                "status": "CRITICAL_FAILURE",
                "behavior": "Equation undefined, core cannot sustain dimensional fold"
            },
            {
                "range": "200 < M < 500",
                "status": "EXTREMELY_DANGEROUS",
                "behavior": "Field strength critically low, high risk of fold collapse"
            },
            {
                "range": "500 ≤ M < 1,000",
                "status": "CAUTION_ADVISED",
                "behavior": "Below optimal operating range, reduced efficiency"
            },
            {
                "range": "1,000 ≤ M ≤ 2,000,000",
                "status": "WITHIN_SAFE_PARAMETERS",
                "behavior": "Normal operating range, all systems nominal"
            },
            {
                "range": "2,000,000 < M ≤ 3,000,000",
                "status": "EXCEEDS_SAFE_LIMITS",
                "behavior": "Beyond maximum safe output, risk of core destabilization"
            },
            {
                "range": "M > 3,000,000",
                "status": "CATASTROPHIC_OVERLOAD_RISK",
                "behavior": "Catastrophic overload imminent, immediate shutdown required"
            }
        ],
        "example_results": [
            {
                "field_strength_magellans": 1000.0,
                "distance_light_years": 87.0,
                "efficiency_zone": "standard",
                "notes": "Boundary between standard and optimal zones"
            },
            {
                "field_strength_magellans": 2000000.0,
                "distance_light_years": 47000.0,
                "efficiency_zone": "diminishing",
                "notes": "Maximum safe field strength"
            },
            {
                "target_distance_light_years": 90.0,
                "field_strength_magellans": 1020.0,
                "efficiency_zone": "optimal",
                "notes": "Inverse calculation example"
            },
            {
                "target_distance_light_years": 87.0,
                "field_strength_magellans": 1000.0,
                "efficiency_zone": "standard",
                "notes": "Round-trip verification case"
            }
        ],
        "success": True
    }


def long_range_jump_distance(args: LongRangeJumpDistanceArgs) -> dict:
    """
    Calculate jump distance for a given field strength.
    
    Performs forward calculation using the Blackwell Drive equation to determine
    how far the USS Blackwell can travel with the specified field strength.
    
    Args:
        args: LongRangeJumpDistanceArgs containing field_strength_magellans
        
    Returns:
        dict: Calculation results or error response
        
        Success response contains:
            - distance_light_years (float): Calculated jump distance
            - field_strength_magellans (float): Echo of input
            - efficiency_factor (float): Applied efficiency factor (1.0, 1.2, or 0.8)
            - efficiency_zone (str): Zone name ("standard", "optimal", or "diminishing")
            - power_utilization_pct (float): Percentage of max safe field strength
            - safety_status (str): Safety classification
            - warnings (list[str]): Warning messages (empty if safe)
            - success (bool): True
            
        Error response contains:
            - field_strength_magellans (float): Echo of input
            - safety_status (str): Safety classification
            - error (str): Human-readable error message
            - warnings (list[str]): Warning messages
            - success (bool): False
            
    Requirements:
        - 5.1: Calculate jump distance using the Blackwell Drive equation
        - 5.2: Return error if field strength is at or below 200 Magellans
        - 5.3: Return error if field strength is above 3,000,000 Magellans
        - 5.7: Return all required fields in success response
        - 5.8: Echo input field strength in response
        - 5.9: Include warnings for unsafe field strengths
        - 10.1: Return success=False for invalid inputs
        - 10.2: Include human-readable error message
        - 10.3: Include safety status in error response
        - 10.4: Return success=True with warnings for successful calculations
        - 10.5: Return success=True with empty warnings for safe calculations
    """
    from calculator.constants import M0, MAX_ABSOLUTE_MAGELLANS
    from calculator.equations import calculate_jump_distance, get_efficiency_factor
    from calculator.safety import classify_safety_status, generate_warnings, calculate_power_utilization
    
    # Extract field_strength_magellans from args
    field_strength_magellans = args.field_strength_magellans
    
    # Classify safety status first (for error responses)
    safety_status = classify_safety_status(field_strength_magellans)
    
    # Validate input: M > M0 and M <= MAX_ABSOLUTE_MAGELLANS
    if field_strength_magellans <= M0:
        return {
            "field_strength_magellans": field_strength_magellans,
            "safety_status": safety_status.value,
            "error": f"Field strength must be greater than {M0} Magellans (safety threshold M0)",
            "warnings": generate_warnings(field_strength_magellans, safety_status),
            "success": False
        }
    
    if field_strength_magellans > MAX_ABSOLUTE_MAGELLANS:
        return {
            "field_strength_magellans": field_strength_magellans,
            "safety_status": safety_status.value,
            "error": f"Field strength exceeds catastrophic limit ({MAX_ABSOLUTE_MAGELLANS} Magellans)",
            "warnings": generate_warnings(field_strength_magellans, safety_status),
            "success": False
        }
    
    # Calculate jump distance
    try:
        distance = calculate_jump_distance(field_strength_magellans)
    except ValueError as e:
        return {
            "field_strength_magellans": field_strength_magellans,
            "safety_status": safety_status.value,
            "error": str(e),
            "warnings": generate_warnings(field_strength_magellans, safety_status),
            "success": False
        }
    
    # Get efficiency factor and determine zone
    efficiency_factor = get_efficiency_factor(field_strength_magellans)
    if field_strength_magellans < 1_000.0:
        efficiency_zone = "standard"
    elif field_strength_magellans < 10_000.0:
        efficiency_zone = "optimal"
    else:
        efficiency_zone = "diminishing"
    
    # Generate warnings
    warnings = generate_warnings(field_strength_magellans, safety_status)
    
    # Calculate power utilization
    power_utilization = calculate_power_utilization(field_strength_magellans)
    
    # Return success response
    return {
        "distance_light_years": distance,
        "field_strength_magellans": field_strength_magellans,
        "efficiency_factor": efficiency_factor,
        "efficiency_zone": efficiency_zone,
        "power_utilization_pct": power_utilization,
        "safety_status": safety_status.value,
        "warnings": warnings,
        "success": True
    }


def long_range_field_strength(args: LongRangeFieldStrengthArgs) -> dict:
    """
    Calculate required field strength for a target distance.
    
    Performs inverse calculation using Newton-Raphson iteration to determine
    the field strength needed to reach the specified distance.
    
    Args:
        args: LongRangeFieldStrengthArgs containing target_distance_light_years
        
    Returns:
        dict: Calculation results or error response
        
        Success response contains:
            - field_strength_magellans (float): Calculated field strength
            - field_strength_formatted (str): Human-readable formatted string
            - distance_light_years (float): Echo of target distance
            - efficiency_factor (float): Applied efficiency factor (1.0, 1.2, or 0.8)
            - efficiency_zone (str): Zone name ("standard", "optimal", or "diminishing")
            - power_utilization_pct (float): Percentage of max safe field strength
            - safety_status (str): Safety classification
            - warnings (list[str]): Warning messages (empty if safe)
            - success (bool): True
            
        Error response contains:
            - distance_light_years (float): Echo of input
            - error (str): Human-readable error message
            - warnings (list[str]): Empty list
            - success (bool): False
            
    Requirements:
        - 6.1: Calculate field strength using Newton-Raphson iteration
        - 6.2: Return error if target distance is zero or negative
        - 6.6: Return all required fields in success response
        - 6.7: Echo target distance in response
        - 6.8: Include warnings for unsafe field strengths
        - 10.1: Return success=False for invalid inputs
        - 10.2: Include human-readable error message
        - 10.3: Include safety status in error response
        - 10.4: Return success=True with warnings for successful calculations
        - 10.5: Return success=True with empty warnings for safe calculations
    """
    from calculator.equations import calculate_field_strength, format_field_strength, get_efficiency_factor
    from calculator.safety import classify_safety_status, generate_warnings, calculate_power_utilization
    
    # Extract target_distance_light_years from args
    target_distance_light_years = args.target_distance_light_years
    
    # Validate input: D > 0
    if target_distance_light_years <= 0:
        return {
            "distance_light_years": target_distance_light_years,
            "error": "Target distance must be greater than 0 light-years",
            "warnings": [],
            "success": False
        }
    
    # Calculate field strength using Newton-Raphson
    try:
        field_strength = calculate_field_strength(target_distance_light_years)
    except ValueError as e:
        return {
            "distance_light_years": target_distance_light_years,
            "error": str(e),
            "warnings": [],
            "success": False
        }
    
    # Format field strength
    formatted_strength = format_field_strength(field_strength)
    
    # Get efficiency factor and determine zone
    efficiency_factor = get_efficiency_factor(field_strength)
    if field_strength < 1_000.0:
        efficiency_zone = "standard"
    elif field_strength < 10_000.0:
        efficiency_zone = "optimal"
    else:
        efficiency_zone = "diminishing"
    
    # Classify safety status
    safety_status = classify_safety_status(field_strength)
    
    # Generate warnings
    warnings = generate_warnings(field_strength, safety_status)
    
    # Calculate power utilization
    power_utilization = calculate_power_utilization(field_strength)
    
    # Return success response
    return {
        "field_strength_magellans": field_strength,
        "field_strength_formatted": formatted_strength,
        "distance_light_years": target_distance_light_years,
        "efficiency_factor": efficiency_factor,
        "efficiency_zone": efficiency_zone,
        "power_utilization_pct": power_utilization,
        "safety_status": safety_status.value,
        "warnings": warnings,
        "success": True
    }
