"""
USS Blackwell MCP Server - Short-range tactical jump calculation tools.

This module provides tools for calculating short-range tactical jump distances,
field strengths, criticality assessments, and parameter optimization using the
enhanced tactical jump equations. Unlike long-range dimensional folding which
operates on macro-spacetime geometry, tactical jumps exploit quantum-scale
subspace resonances for precision maneuvers within stellar systems (meters to 30 AU).

The tactical system involves:
- Time-dependent charge accumulation with exponential decay
- Multiple interacting field systems (red matter core + warp core)
- Phase offset and subspace resonance tuning parameters
- Cumulative quantum scarring from sequential jumps
- Exponential criticality risk buildup
- Complex coordinate transformation matrices
"""

from typing import Annotated, Dict, List, Literal, Optional, Tuple, Any
from pydantic import Field

# Pydantic model imports for parameter validation
from tools.models.short_range_models import (
    JumpEntry,
)

# Calculator module imports for tactical calculations
from calculator.tactical import (
    # Modulation factors
    calculate_resonance_modulation,
    calculate_phase_resonance_coupling,
    calculate_safe_tolerance,
    calculate_cochrane_efficiency,
    
    # Power integration
    calculate_phase_timing_modulation,
    calculate_coupling_coefficient,
    calculate_dynamic_stability,
    calculate_warp_power,
    integrate_charge_density,
    
    # Distance calculations
    calculate_tactical_distance,
    calculate_required_field_tactical,
    
    # Criticality calculations
    calculate_criticality_modifier,
    calculate_red_matter_criticality,
    calculate_warp_core_stress,
    calculate_interaction_factor,
    calculate_total_criticality,
    
    # Coordinate accuracy
    calculate_flexure_matrix,
    apply_flexure_transformation,
    
    # Landing offset
    calculate_landing_offset,
    
    # Safety and validation
    validate_tactical_parameters,
    check_resonance_danger_zones,
    find_cochrane_safe_zones,
    classify_criticality_level,
    estimate_time_to_threshold,
)

# Constants imports
from calculator.constants import (
    # Tactical distance equation constants
    ALPHA,
    BETA,
    GAMMA,
    
    # Power integration constants
    P0,
    XI_DECAY,
    P_WARP_MAX,
    SIGMA,
    
    # Cochrane coupling constants
    DELTA,
    C_MAX,
    
    # Criticality constants
    C0,
    LAMBDA,
    DELTA_JUMP_BASE,
    MU_JUMP_BASE,
    
    # Criticality thresholds
    CRITICALITY_WARNING,
    CRITICALITY_EJECTION,
    CRITICALITY_FAILURE,
    CRITICALITY_CATASTROPHIC,
    
    # Operational limits
    MAX_CHARGE_TIME,
    SAFE_CHARGE_TIME,
    MIN_DISTANCE_METERS,
    MAX_DISTANCE_METERS,
    MIN_COCHRANE,
    MAX_COCHRANE,
    MIN_PHASE_OFFSET,
    MAX_PHASE_OFFSET,
    MIN_RESONANCE,
    MAX_RESONANCE,
)


def short_range_describe() -> Dict[str, Any]:
    """
    Describe the short-range tactical jump system.
    
    Returns comprehensive reference documentation about the tactical jump system,
    including physics explanation (Rizan's Resonance Bridge Theory), adjustable
    parameters, all equations with variable descriptions, operational parameters,
    safe zones, criticality thresholds, and example calculations.
    
    Returns:
        dict: System reference documentation with the following fields:
            - system_name (str): Name of the tactical jump system
            - distance_range (dict): Minimum and maximum operational distances
            - physics_explanation (str): Rizan's Resonance Bridge Theory
            - adjustable_parameters (dict): Phase offset and subspace resonance details
            - equations (dict): All tactical jump equations with variable descriptions
            - operational_parameters (dict): Cochrane field, charge time, and other limits
            - criticality_thresholds (dict): Warning levels and their meanings
            - safe_zones (dict): Guidance on optimal parameter ranges
            - example_calculations (list): Verification examples with known results
            - success (bool): Always True
    """
    return {
        "system_name": "Extreme Close-Range Tactical Jump System",
        "system_type": "Quantum-Scale Subspace Resonance Exploitation",
        "distance_range": {
            "min_meters": MIN_DISTANCE_METERS,
            "max_meters": MAX_DISTANCE_METERS,
            "max_au": 30.0,
            "description": "Tactical jumps operate from 1 meter to 30 AU (4.488 trillion meters)"
        },
        
        "physics_explanation": {
            "theory_name": "Rizan's Resonance Bridge Theory",
            "description": (
                "While long-range dimensional folding operates on macro-spacetime geometry, "
                "tactical jumps exploit quantum-scale subspace resonances discovered by Dr. Elara Rizan. "
                "The theory posits that local subspace exhibits harmonic oscillations at specific "
                "frequencies (3-113 THz range), creating temporary 'resonance bridges' that can be "
                "traversed with precise field modulation. Unlike the clean dimensional collapse of "
                "long-range jumps, tactical jumps leave quantum scarring in the subspace fabric, "
                "causing cumulative criticality buildup with each successive jump."
            ),
            "key_differences_from_long_range": [
                "Distance scale: Meters to AU instead of light-years",
                "Time dependency: Requires charge accumulation over minutes",
                "Field interaction: Red matter core + warp core coupling",
                "Risk profile: Exponentially increasing criticality with use",
                "Tuning parameters: Phase offset and subspace resonance adjustment",
                "Coordinate accuracy: Subject to flexure matrix transformations"
            ],
            "quantum_scarring": (
                "Each tactical jump creates microscopic tears in the subspace fabric that "
                "accumulate exponentially. The red matter core's quantum state becomes increasingly "
                "unstable with each jump, leading to criticality thresholds that require core "
                "de-energization and recovery time."
            )
        },
        
        "adjustable_parameters": {
            "phase_offset": {
                "symbol": "φ",
                "range": f"{MIN_PHASE_OFFSET} to {MAX_PHASE_OFFSET}",
                "default": 0.75,
                "description": (
                    "Phase offset controls the temporal alignment between red matter core "
                    "oscillations and warp field harmonics. The optimal value of 0.75 provides "
                    "maximum stability and coupling efficiency. Deviation from this value increases "
                    "criticality risk and reduces phase-resonance coupling."
                ),
                "effects": [
                    "Influences Cochrane coupling efficiency η(C)",
                    "Affects phase-resonance coupling Ω(φ,R)",
                    "Modifies warp core stress component",
                    "Shifts resonance danger zones by ±5 THz",
                    "Impacts coordinate accuracy through flexure matrix"
                ]
            },
            "subspace_resonance": {
                "symbol": "R",
                "range": f"{MIN_RESONANCE} to {MAX_RESONANCE} THz",
                "default": 47.23,
                "description": (
                    "Subspace resonance frequency represents the local quantum oscillation rate "
                    "of the subspace fabric. This value varies by stellar region and must be "
                    "measured before tactical operations. The resonance modulation factor Ψ(R) "
                    "exhibits strong harmonic behavior with optimal zones and null zones."
                ),
                "optimal_zones": [
                    {"center_thz": 25, "description": "First harmonic peak"},
                    {"center_thz": 47, "description": "Second harmonic peak (default)"},
                    {"center_thz": 72, "description": "Third harmonic peak"},
                    {"center_thz": 95, "description": "Fourth harmonic peak"}
                ],
                "null_zones": [
                    {"center_thz": 0, "description": "Zero frequency null"},
                    {"center_thz": 56.5, "description": "Primary null zone"},
                    {"center_thz": 113, "description": "Maximum frequency null"}
                ],
                "danger_zones_base": [14, 28, 42, 56, 70, 84, 98],
                "danger_zone_note": "Danger zones shift by (φ - 0.75) × 5 THz based on phase offset"
            }
        },
        
        "equations": {
            "tactical_distance": {
                "equation": "D = α × M^β × (1 - e^(-M/γ)) × ρ(t) × η(C) × Ψ(R)",
                "description": "Primary tactical jump distance equation",
                "variables": {
                    "D": "Jump distance in meters",
                    "α": f"Range scaling constant ({ALPHA:.3e})",
                    "M": "Instantaneous Magellan field strength",
                    "β": f"Power efficiency factor ({BETA})",
                    "γ": f"Field saturation threshold ({GAMMA} Magellans)",
                    "ρ(t)": "Charge density factor (time integral)",
                    "η(C)": "Cochrane coupling efficiency",
                    "Ψ(R)": "Subspace resonance modulation"
                }
            },
            "charge_density_integral": {
                "equation": "ρ(t) = (1/P₀) ∫₀ᵗ [P_red(τ) + P_warp(τ) × κ(C,φ,R)] × e^(-τ/ξ) × Λ(φ,R,τ) dτ",
                "description": "Time-dependent charge accumulation from red matter and warp cores",
                "variables": {
                    "ρ(t)": "Charge density factor",
                    "P₀": f"Base power normalization ({P0:.2e} watts)",
                    "t": "Charge time in minutes",
                    "P_red(τ)": "Red matter core power output (constant ~1.0e8 watts)",
                    "P_warp(τ)": "Warp core power contribution (time-dependent)",
                    "κ(C,φ,R)": "Enhanced coupling coefficient",
                    "ξ": f"Energy decay constant ({XI_DECAY} minutes)",
                    "Λ(φ,R,τ)": "Dynamic phase-resonance stability"
                },
                "integration_method": "Simpson's rule with 100 steps"
            },
            "warp_power": {
                "equation": "P_warp(τ) = (C/1000)^2.4 × P_warp_max × (1 - e^(-στ)) × Φ(φ,τ)",
                "description": "Warp core power contribution with rise time",
                "variables": {
                    "P_warp(τ)": "Warp core power at time τ (watts)",
                    "C": "Cochrane guide field (millicochranes)",
                    "P_warp_max": f"Maximum warp power ({P_WARP_MAX:.2e} watts)",
                    "σ": f"Warp field rise time constant ({SIGMA} min⁻¹)",
                    "Φ(φ,τ)": "Phase timing modulation"
                }
            },
            "resonance_modulation": {
                "equation": "Ψ(R) = (R/50)^0.4 × sin(πR/56.5) × (1 + 0.1×cos(2πR/113))",
                "description": "Subspace resonance modulation factor",
                "variables": {
                    "Ψ(R)": "Resonance modulation factor (can be negative in null zones)",
                    "R": "Subspace resonance frequency (THz)"
                },
                "range": "Approximately -1.5 to +1.5"
            },
            "cochrane_efficiency": {
                "equation": "η(C) = ln(C + δ) × |sin(πC/C_max)| × ζ(C) × Ω(φ,R)",
                "description": "Cochrane coupling efficiency with safe tolerance",
                "variables": {
                    "η(C)": "Cochrane coupling efficiency factor",
                    "C": "Cochrane guide field (millicochranes)",
                    "δ": f"Logarithmic offset ({DELTA})",
                    "C_max": f"Maximum Cochrane ({C_MAX}, warp 1.0)",
                    "ζ(C)": "Safe tolerance function",
                    "Ω(φ,R)": "Phase-resonance coupling"
                }
            },
            "phase_resonance_coupling": {
                "equation": "Ω(φ,R) = 0.8 + 0.2×cos(2πφ + πR/113) × (1 - |φ - 0.75|)",
                "description": "Phase-resonance coupling factor",
                "variables": {
                    "Ω(φ,R)": "Phase-resonance coupling (0.6 to 1.0 range)",
                    "φ": "Phase offset (0.00-1.00)",
                    "R": "Subspace resonance (THz)"
                }
            },
            "total_criticality": {
                "equation": "C_total = C_red(t,n,φ,R) + C_warp(C,t,φ) × β_interaction(M,φ,R)",
                "description": "Total system criticality from red matter and warp core stress",
                "variables": {
                    "C_total": "Total criticality (0.0 to 1.0+)",
                    "C_red": "Red matter criticality component",
                    "C_warp": "Warp core stress component",
                    "β_interaction": "Interaction factor between systems",
                    "t": "Energization time (minutes)",
                    "n": "Number of jumps performed"
                }
            },
            "red_matter_criticality": {
                "equation": "C_red = C₀ × e^(λt) × (1 + Σᵢ₌₁ⁿ δᵢ × e^(μᵢt)) × Χ(φ,R,t)",
                "description": "Red matter criticality with exponential growth and jump accumulation",
                "variables": {
                    "C_red": "Red matter criticality component",
                    "C₀": f"Base criticality ({C0})",
                    "λ": f"Primary exponential rate ({LAMBDA} min⁻¹)",
                    "t": "Energization time (minutes)",
                    "n": "Number of jumps",
                    "δᵢ": f"Jump impact factor (base {DELTA_JUMP_BASE} × i^1.3)",
                    "μᵢ": f"Jump decay rate (base {MU_JUMP_BASE} × √i)",
                    "Χ(φ,R,t)": "Phase-resonance criticality modifier"
                }
            },
            "flexure_matrix": {
                "equation": "𝐅(M,φ,R) = 3×3 matrix with phase-resonance dependent elements",
                "description": "Coordinate transformation matrix for spatial accuracy",
                "properties": [
                    "Symmetric matrix: f₁₂ = f₂₁, f₁₃ = f₃₁, f₂₃ = f₃₂",
                    "Diagonal elements near 1.0: f₁₁, f₂₂, f₃₃ ∈ [0.94, 1.00]",
                    "Off-diagonal elements small: |fᵢⱼ| < 0.02 for i ≠ j",
                    "Transformation: [Δx, Δy, Δz]ᵀ = 𝐅 × [x, y, z]ᵀ"
                ]
            }
        },
        
        "operational_parameters": {
            "cochrane_field": {
                "symbol": "C",
                "range": f"{MIN_COCHRANE} to {MAX_COCHRANE} millicochranes",
                "default": 350.0,
                "description": (
                    "Cochrane guide field strength controls warp core coupling to the red matter "
                    "system. Higher values increase power contribution but also increase warp core "
                    "stress. Safe zones vary with phase offset and subspace resonance."
                ),
                "warp_factor_note": "1000 millicochranes = Warp Factor 1.0"
            },
            "charge_time": {
                "range": f"0.3 to {MAX_CHARGE_TIME} minutes",
                "safe_range": f"0.3 to {SAFE_CHARGE_TIME} minutes",
                "description": (
                    "Time allowed for charge density accumulation. Longer charge times enable "
                    "greater distances but increase criticality risk. Charge times beyond 10 minutes "
                    "generate warnings due to exponential criticality growth."
                )
            },
            "magellan_field": {
                "symbol": "M",
                "typical_range": "100 to 2000 Magellans",
                "description": (
                    "Instantaneous red matter field strength at jump execution. For tactical jumps, "
                    "this is typically much lower than long-range jumps due to the charge density "
                    "multiplication factor."
                )
            },
            "energization_tracking": {
                "description": (
                    "Criticality tracking begins when the red matter core is energized and continues "
                    "until de-energization. All jumps during an energization period contribute to "
                    "cumulative quantum scarring."
                ),
                "recovery_note": "Core de-energization required for quantum scarring recovery"
            }
        },
        
        "criticality_thresholds": {
            "nominal": {
                "range": f"C_total < {CRITICALITY_WARNING}",
                "level": "NOMINAL",
                "description": "All systems operating within normal parameters",
                "action": "Continue operations normally"
            },
            "warning": {
                "range": f"{CRITICALITY_WARNING} ≤ C_total < {CRITICALITY_EJECTION}",
                "level": "WARNING",
                "description": "Tertiary core criticality warning - monitor closely",
                "action": "Increase monitoring frequency, prepare for de-energization"
            },
            "critical": {
                "range": f"{CRITICALITY_EJECTION} ≤ C_total < {CRITICALITY_FAILURE}",
                "level": "CRITICAL",
                "description": "Tertiary core ejection required - abort sequence",
                "action": "Cease tactical operations, initiate core de-energization"
            },
            "failure_imminent": {
                "range": f"{CRITICALITY_FAILURE} ≤ C_total < {CRITICALITY_CATASTROPHIC}",
                "level": "FAILURE_IMMINENT",
                "description": "Primary core failure imminent - emergency shutdown",
                "action": "Emergency core shutdown, evacuate engineering sections"
            },
            "catastrophic": {
                "range": f"C_total ≥ {CRITICALITY_CATASTROPHIC}",
                "level": "CATASTROPHIC",
                "description": "Catastrophic overload inevitable - evacuate immediately",
                "action": "Abandon ship protocols, core breach imminent"
            }
        },
        
        "safe_zones": {
            "optimal_phase_offset": {
                "value": 0.75,
                "tolerance": "±0.05",
                "description": "Phase offset of 0.75 provides maximum stability and coupling efficiency"
            },
            "optimal_resonance_frequencies": {
                "primary": 47.23,
                "alternatives": [25, 72, 95],
                "description": "Resonance frequencies near harmonic peaks maximize distance modulation"
            },
            "cochrane_safe_zones": {
                "description": (
                    "Safe Cochrane ranges vary with phase offset and subspace resonance. "
                    "Use short_range_optimize_cochrane() to identify safe zones for current conditions."
                ),
                "general_guidance": "Avoid Cochrane values where |sin(πC/C_max)| approaches zero"
            },
            "charge_time_recommendations": {
                "minimum_practical": "0.5 minutes (30 seconds)",
                "optimal_range": "1.0 to 5.0 minutes",
                "maximum_safe": "10.0 minutes",
                "description": "Balance between distance capability and criticality risk"
            },
            "sequential_jump_limits": {
                "safe_sequence": "3-5 jumps",
                "maximum_recommended": "7 jumps",
                "description": "Jump count before criticality approaches warning threshold",
                "recovery_required": "Core de-energization after extended sequences"
            }
        },
        
        "example_calculations": [
            {
                "scenario": "Standard tactical jump",
                "inputs": {
                    "charge_time_minutes": 2.0,
                    "magellan_field": 500.0,
                    "cochrane_field": 350.0,
                    "phase_offset": 0.75,
                    "subspace_resonance": 47.23
                },
                "expected_outputs": {
                    "charge_density_approx": 2.4,
                    "distance_meters_approx": 120000,
                    "distance_km_approx": 120,
                    "criticality_approx": 0.05,
                    "criticality_level": "NOMINAL"
                },
                "notes": "Typical single tactical jump with optimal parameters"
            },
            {
                "scenario": "Emergency short-range jump",
                "inputs": {
                    "charge_time_minutes": 0.5,
                    "magellan_field": 300.0,
                    "cochrane_field": 350.0,
                    "phase_offset": 0.75,
                    "subspace_resonance": 47.23
                },
                "expected_outputs": {
                    "charge_density_approx": 0.6,
                    "distance_meters_approx": 15000,
                    "distance_km_approx": 15,
                    "criticality_approx": 0.02,
                    "criticality_level": "NOMINAL"
                },
                "notes": "Minimal charge time for emergency maneuvers"
            },
            {
                "scenario": "Extended range tactical jump",
                "inputs": {
                    "charge_time_minutes": 5.0,
                    "magellan_field": 800.0,
                    "cochrane_field": 450.0,
                    "phase_offset": 0.75,
                    "subspace_resonance": 47.23
                },
                "expected_outputs": {
                    "charge_density_approx": 5.8,
                    "distance_meters_approx": 850000,
                    "distance_km_approx": 850,
                    "criticality_approx": 0.12,
                    "criticality_level": "NOMINAL"
                },
                "notes": "Longer charge time for maximum tactical range"
            },
            {
                "scenario": "Sequential jump criticality buildup",
                "inputs": {
                    "energization_time_minutes": 8.0,
                    "jump_count": 3,
                    "magellan_field": 500.0,
                    "cochrane_field": 350.0,
                    "phase_offset": 0.75,
                    "subspace_resonance": 47.23
                },
                "expected_outputs": {
                    "criticality_approx": 0.18,
                    "criticality_level": "WARNING",
                    "jumps_remaining_estimate": 2
                },
                "notes": "Criticality after 3 jumps over 8 minutes of energization"
            },
            {
                "scenario": "Resonance null zone penalty",
                "inputs": {
                    "charge_time_minutes": 2.0,
                    "magellan_field": 500.0,
                    "cochrane_field": 350.0,
                    "phase_offset": 0.75,
                    "subspace_resonance": 56.5
                },
                "expected_outputs": {
                    "resonance_modulation_approx": 0.0,
                    "distance_meters_approx": 0,
                    "notes": "Jump fails in resonance null zone"
                },
                "notes": "Demonstrates importance of avoiding null zones"
            }
        ],
        
        "success": True
    }


def short_range_jump_distance(
    charge_time_minutes: Annotated[float, Field(
        description=(
            "Charge accumulation time in minutes. Controls how long the red "
            "matter core accumulates energy before jump execution. Range: 0.3 to "
            "15.0. Safe operating range: 0.3 to 10.0. Longer charge times enable "
            "greater distances but increase criticality risk exponentially. "
            "Values >10.0 generate criticality warnings due to quantum scarring "
            "accumulation."
        ),
        ge=0.3,
        le=15.0
    )],
    cochrane_field: Annotated[float, Field(
        default=350.0,
        description=(
            "Warp core coupling strength in millicochranes. Controls the warp "
            "core's power contribution to the tactical jump system. Range: 100 to "
            "900. Defaults to 350. Note: 1000 millicochranes = Warp Factor 1.0. "
            "Safe zones vary with phase_offset and subspace_resonance due to "
            "harmonic interactions. Use short_range_optimize_cochrane() to "
            "identify safe zones for current conditions. Avoid values where "
            "sin(πC/C_max) approaches zero (null zones)."
        ),
        ge=100.0,
        le=900.0
    )] = 350.0,
    phase_offset: Annotated[float, Field(
        default=0.75,
        description=(
            "Phase offset controlling temporal alignment between red matter core "
            "oscillations and warp field harmonics. Range: 0.00 to 1.00. Defaults "
            "to 0.75 (optimal). The optimal value of 0.75 provides maximum "
            "stability and coupling efficiency. Deviation increases criticality "
            "risk and reduces phase-resonance coupling. Affects Cochrane coupling "
            "efficiency, shifts resonance danger zones by ±5 THz per 0.1 deviation, "
            "and impacts coordinate accuracy through flexure matrix."
        ),
        ge=0.0,
        le=1.0
    )] = 0.75,
    subspace_resonance: Annotated[float, Field(
        default=47.23,
        description=(
            "Subspace resonance frequency in THz (terahertz). Represents the "
            "local quantum oscillation rate of the subspace fabric. Range: 3.0 to "
            "113.0 THz. Defaults to 47.23 (second harmonic peak). This value "
            "varies by stellar region and must be measured before tactical "
            "operations. Optimal zones (harmonic peaks): 25, 47, 72, 95 THz. "
            "Null zones (near-zero modulation): 0, 56.5, 113 THz. Danger zones "
            "(base): 14, 28, 42, 56, 70, 84, 98 THz (shift by (φ-0.75)×5 based "
            "on phase_offset)."
        ),
        ge=3.0,
        le=113.0
    )] = 47.23,
    magellan_field: Annotated[Optional[float], Field(
        default=None,
        description=(
            "Instantaneous red matter field strength in Magellans at jump "
            "execution. Optional. If not provided, defaults to 500.0 (typical "
            "tactical field strength). Range: 100 to 2000 typical for tactical "
            "jumps. Unlike long-range jumps, tactical jumps use charge density "
            "multiplication, so lower field strengths are sufficient."
        )
    )] = None,
    energization_time: Annotated[float, Field(
        default=0.0,
        description=(
            "Minutes since red matter core energization. Used for criticality "
            "tracking. Range: 0.0 to 60.0. Defaults to 0.0 (first jump in "
            "sequence). Criticality accumulates exponentially with energization "
            "time. Core de-energization required for quantum scarring recovery."
        ),
        ge=0.0,
        le=60.0
    )] = 0.0,
    jump_count: Annotated[int, Field(
        default=0,
        description=(
            "Number of previous jumps performed during current energization "
            "period. Used for cumulative quantum scarring calculation. Range: 0 "
            "to 20. Defaults to 0 (first jump). Each jump creates microscopic "
            "tears in subspace fabric that accumulate exponentially. Safe "
            "sequence: 3-5 jumps. Maximum recommended: 7 jumps before "
            "de-energization."
        ),
        ge=0,
        le=20
    )] = 0
) -> Dict[str, Any]:
    """
    Calculate achievable distance for a tactical jump given charge time and parameters.

    This is the forward calculation: given charge time and system parameters, determine
    how far the ship can jump. Optionally accepts a pre-calculated Magellan field strength,
    otherwise uses a default tactical field value.

    Args:
        charge_time_minutes: Charge duration in minutes (required)
        cochrane_field: Cochrane guide field in millicochranes (default: 350.0)
        phase_offset: Phase offset 0.00-1.00 (default: 0.75)
        subspace_resonance: Subspace resonance frequency in THz (default: 47.23)
        magellan_field: Instantaneous Magellan field if known (optional, default: None)
        energization_time: Minutes since core energization (default: 0.0)
        jump_count: Number of previous jumps in sequence (default: 0)

    Returns:
        Dict[str, Any]: Response dictionary with the following structure:
        
        Success response (success=True):
            - distance_meters (float): Jump distance in meters
            - distance_formatted (str): Human-readable distance with units
            - field_strength_magellans (float): Magellan field strength used
            - charge_time_minutes (float): Charge duration
            - charge_density (float): Integrated charge density factor
            - modulation_factors (dict):
                - cochrane_efficiency (float): η(C) value
                - resonance_modulation (float): Ψ(R) value
                - phase_resonance_coupling (float): Ω(φ,R) value
            - criticality (dict):
                - total (float): Total criticality value
                - red_matter (float): Red matter component
                - warp_core (float): Warp core component
                - level (str): Criticality level name
                - status_message (str): Status description
                - time_to_next_threshold_minutes (float|None): Time estimate
            - coordinate_accuracy (dict):
                - flexure_matrix (List[List[float]]): 3x3 transformation matrix
                - accuracy_degradation_pct (float): Accuracy degradation percentage
            - landing_offset (dict):
                - offset_meters (float): Scalar magnitude of positional error
                - offset_formatted (str): Human-readable distance with units
                - directional_components (dict):
                    - fore_aft_meters (float): Forward/aft component (+ = forward, - = aft)
                    - port_starboard_meters (float): Port/starboard component (+ = starboard, - = port)
                    - dorsal_ventral_meters (float): Dorsal/ventral component (+ = dorsal, - = ventral)
                - directional_summary (str): Plain-language direction description
                - severity (str): Categorical severity (NEGLIGIBLE|MINOR|SIGNIFICANT|DANGEROUS|CATASTROPHIC)
                - narrative_summary (str): Complete narrative sentence ready for dialogue
            - warnings (List[str]): Operational warnings
            - danger_zones (List[str]): Active danger zone warnings
            - success (bool): True
        
        Error response (success=False):
            - error (str): Error message
            - validation_errors (List[str]): Validation error details (if applicable)
            - success (bool): False

    Example:
        >>> result = short_range_jump_distance(
        ...     charge_time_minutes=2.0,
        ...     cochrane_field=350.0,
        ...     phase_offset=0.75,
        ...     subspace_resonance=47.23
        ... )
        >>> print(f"Distance: {result['distance_formatted']}")
        Distance: 120.5 kilometers
    """
    try:
        # Subtask 16.2: Validate input parameters
        is_valid, validation_errors = validate_tactical_parameters(
            charge_time=charge_time_minutes,
            C=cochrane_field,
            phi=phase_offset,
            R=subspace_resonance,
            distance=None
        )

        if not is_valid:
            return {
                "error": "Invalid input parameters",
                "validation_errors": validation_errors,
                "success": False
            }

        # Subtask 16.3: Integrate charge density
        charge_density = integrate_charge_density(
            charge_time=charge_time_minutes,
            C=cochrane_field,
            phi=phase_offset,
            R=subspace_resonance
        )

        # Subtask 16.4: Calculate or use provided Magellan field
        if magellan_field is None:
            # Use default tactical field strength
            M = 500.0
        else:
            M = magellan_field

        # Subtask 16.5: Calculate distance with all modulation factors
        distance_meters = calculate_tactical_distance(
            M=M,
            rho=charge_density,
            C=cochrane_field,
            phi=phase_offset,
            R=subspace_resonance
        )

        # Calculate individual modulation factors for response
        cochrane_efficiency = calculate_cochrane_efficiency(cochrane_field, phase_offset, subspace_resonance)
        resonance_modulation = calculate_resonance_modulation(subspace_resonance)
        phase_resonance_coupling = calculate_phase_resonance_coupling(phase_offset, subspace_resonance)

        # Subtask 16.6: Calculate criticality
        total_energization_time = energization_time + charge_time_minutes
        C_total, C_red, C_warp = calculate_total_criticality(
            t=total_energization_time,
            n=jump_count,
            M=M,
            C=cochrane_field,
            phi=phase_offset,
            R=subspace_resonance
        )

        criticality_level, status_message = classify_criticality_level(C_total)

        # Estimate time to next threshold
        thresholds = [CRITICALITY_WARNING, CRITICALITY_EJECTION, CRITICALITY_FAILURE, CRITICALITY_CATASTROPHIC]
        time_to_next_threshold = None
        for threshold in thresholds:
            if C_total < threshold:
                time_to_next_threshold = estimate_time_to_threshold(
                    current_criticality=C_total,
                    next_threshold=threshold,
                    t=total_energization_time,
                    n=jump_count,
                    phi=phase_offset,
                    R=subspace_resonance
                )
                break

        # Subtask 16.7: Calculate coordinate accuracy
        flexure_matrix = calculate_flexure_matrix(
            M=M,
            rho=charge_density,
            phi=phase_offset,
            R=subspace_resonance
        )

        # Calculate accuracy degradation as percentage deviation from identity matrix
        # Average deviation of diagonal elements from 1.0
        diagonal_deviation = (
            abs(flexure_matrix[0][0] - 1.0) +
            abs(flexure_matrix[1][1] - 1.0) +
            abs(flexure_matrix[2][2] - 1.0)
        ) / 3.0
        accuracy_degradation_pct = diagonal_deviation * 100.0

        # Calculate landing offset
        landing_offset = calculate_landing_offset(
            distance_meters=distance_meters,
            accuracy_degradation_pct=accuracy_degradation_pct
        )

        # Subtask 16.8: Check for danger zones
        danger_zones = check_resonance_danger_zones(subspace_resonance, phase_offset)

        # Subtask 16.9: Generate warnings
        warnings = []

        # Charge time warnings
        if charge_time_minutes > SAFE_CHARGE_TIME:
            warnings.append(
                f"Charge time ({charge_time_minutes:.1f} min) exceeds safe limit "
                f"({SAFE_CHARGE_TIME} min) - criticality risk elevated"
            )

        # Criticality warnings
        if criticality_level != "NOMINAL":
            warnings.append(
                f"Criticality level: {criticality_level} - {status_message}"
            )

        # Resonance modulation warnings
        if abs(resonance_modulation) < 0.1:
            warnings.append(
                f"Subspace resonance ({subspace_resonance:.2f} THz) near null zone - "
                f"distance severely reduced (modulation: {resonance_modulation:.3f})"
            )

        # Phase offset warnings
        if abs(phase_offset - 0.75) > 0.15:
            warnings.append(
                f"Phase offset ({phase_offset:.2f}) deviates significantly from optimal (0.75) - "
                f"coupling efficiency reduced"
            )

        # Coordinate accuracy warnings
        if accuracy_degradation_pct > 5.0:
            warnings.append(
                f"Coordinate accuracy degradation: {accuracy_degradation_pct:.2f}% - "
                f"positioning error may be significant"
            )

        # Distance warnings
        if distance_meters < 10.0:
            warnings.append(
                f"Jump distance extremely short ({distance_meters:.2f} meters) - "
                f"verify parameters and consider adjusting resonance or field strength"
            )
        elif distance_meters > MAX_DISTANCE_METERS * 0.9:
            warnings.append(
                f"Jump distance approaching maximum tactical range - "
                f"consider long-range dimensional folding instead"
            )

        # Subtask 16.10: Format distance output (meters/km/AU)
        if distance_meters < 1000:
            distance_formatted = f"{distance_meters:.2f} meters"
        elif distance_meters < 1e6:
            distance_formatted = f"{distance_meters / 1000:.2f} kilometers"
        elif distance_meters < 1e9:
            distance_formatted = f"{distance_meters / 1e6:.2f} megameters"
        else:
            # Convert to AU (1 AU ≈ 1.496e11 meters, but using 1.5e11 for simplicity)
            au = distance_meters / 1.496e11
            distance_formatted = f"{au:.3f} AU"

        # Subtask 16.11: Build success response with all fields
        return {
            "distance_meters": distance_meters,
            "distance_formatted": distance_formatted,
            "field_strength_magellans": M,
            "charge_time_minutes": charge_time_minutes,
            "charge_density": charge_density,
            "modulation_factors": {
                "cochrane_efficiency": cochrane_efficiency,
                "resonance_modulation": resonance_modulation,
                "phase_resonance_coupling": phase_resonance_coupling
            },
            "criticality": {
                "total": C_total,
                "red_matter": C_red,
                "warp_core": C_warp,
                "level": criticality_level,
                "status_message": status_message,
                "time_to_next_threshold_minutes": time_to_next_threshold
            },
            "coordinate_accuracy": {
                "flexure_matrix": flexure_matrix,
                "accuracy_degradation_pct": accuracy_degradation_pct
            },
            "landing_offset": landing_offset,
            "warnings": warnings,
            "danger_zones": danger_zones,
            "success": True
        }

    except Exception as e:
        # Subtask 16.12: Handle errors and build error response
        return {
            "error": f"Calculation failed: {str(e)}",
            "success": False
        }


def short_range_field_strength(
    target_distance_meters: Annotated[float, Field(
        description=(
            "Target tactical jump distance in meters. Range: 1 to 4,500,000,000 "
            "(30 AU). Tactical jumps operate from 1 meter to 30 AU using "
            "quantum-scale subspace resonances. The system uses Newton-Raphson "
            "iteration to calculate required field strength and charge time."
        ),
        ge=1.0,
        le=4_500_000_000.0
    )],
    cochrane_field: Annotated[float, Field(
        default=350.0,
        description=(
            "Warp core coupling strength in millicochranes. Range: 100 to 900. "
            "Defaults to 350. See short_range_jump_distance for detailed "
            "description."
        ),
        ge=100.0,
        le=900.0
    )] = 350.0,
    phase_offset: Annotated[float, Field(
        default=0.75,
        description=(
            "Phase offset for temporal alignment. Range: 0.00 to 1.00. Defaults "
            "to 0.75 (optimal). See short_range_jump_distance for detailed "
            "description."
        ),
        ge=0.0,
        le=1.0
    )] = 0.75,
    subspace_resonance: Annotated[float, Field(
        default=47.23,
        description=(
            "Subspace resonance frequency in THz. Range: 3.0 to 113.0. Defaults "
            "to 47.23. See short_range_jump_distance for detailed description."
        ),
        ge=3.0,
        le=113.0
    )] = 47.23
) -> Dict[str, Any]:
    """
    Calculate required field strength for a target distance (inverse calculation).
    
    This is the inverse calculation: given a desired distance and charge time, determine
    the Magellan field strength required to achieve that distance. Also assesses feasibility
    based on field limits and criticality constraints.
    
    Args:
        target_distance_meters: Desired jump distance in meters (required)
        cochrane_field: Cochrane guide field in millicochranes (default: 350.0)
        phase_offset: Phase offset 0.00-1.00 (default: 0.75)
        subspace_resonance: Subspace resonance frequency in THz (default: 47.23)
    
    Returns:
        Dict[str, Any]: Response dictionary with the following structure:
        
        Success response (success=True):
            - field_strength_magellans (float): Required Magellan field strength
            - field_strength_formatted (str): Human-readable field strength with units
            - target_distance_meters (float): Target distance requested
            - target_distance_formatted (str): Human-readable distance with units
            - charge_time_minutes (float): Charge duration
            - charge_density (float): Integrated charge density factor
            - feasibility (dict):
                - achievable (bool): Whether jump is feasible
                - field_within_limits (bool): Field strength within operational limits
                - criticality_acceptable (bool): Criticality below critical threshold
                - reason (str): Explanation of feasibility status
            - criticality (dict):
                - total (float): Total criticality value
                - red_matter (float): Red matter component
                - warp_core (float): Warp core component
                - level (str): Criticality level name
                - status_message (str): Status description
                - time_to_next_threshold_minutes (float|None): Time estimate
            - warnings (List[str]): Operational warnings
            - recommendations (List[str]): Tactical recommendations
            - success (bool): True
        
        Error response (success=False):
            - error (str): Error message
            - validation_errors (List[str]): Validation error details (if applicable)
            - target_distance_meters (float): Target distance (if applicable)
            - charge_density (float): Charge density (if calculated)
            - feasibility (dict): Feasibility assessment (if applicable)
            - success (bool): False

    Example:
        >>> result = short_range_field_strength(
        ...     target_distance_meters=100000,
        ...     charge_time_minutes=2.0,
        ...     cochrane_field=350.0,
        ...     phase_offset=0.75,
        ...     subspace_resonance=47.23
        ... )
        >>> print(f"Required field: {result['field_strength_formatted']}")
        Required field: 612.3 Magellans
    """
    try:
        # ShortRangeFieldStrengthArgs doesn't have these fields, so we use defaults
        charge_time_minutes = 2.0  # Default charge time for field strength calculation
        energization_time = 0.0
        jump_count = 0
        
        # Subtask 17.2: Validate input parameters
        is_valid, validation_errors = validate_tactical_parameters(
            charge_time=charge_time_minutes,
            C=cochrane_field,
            phi=phase_offset,
            R=subspace_resonance,
            distance=target_distance_meters
        )
        
        if not is_valid:
            return {
                "error": "Invalid input parameters",
                "validation_errors": validation_errors,
                "success": False
            }
        
        # Subtask 17.3: Integrate charge density
        charge_density = integrate_charge_density(
            charge_time=charge_time_minutes,
            C=cochrane_field,
            phi=phase_offset,
            R=subspace_resonance
        )
        
        # Subtask 17.4: Calculate required field using Newton-Raphson
        try:
            required_field = calculate_required_field_tactical(
                target_distance=target_distance_meters,
                rho=charge_density,
                C=cochrane_field,
                phi=phase_offset,
                R=subspace_resonance
            )
        except ValueError as e:
            # Newton-Raphson failed to converge or distance unachievable
            return {
                "error": f"Unable to calculate required field: {str(e)}",
                "target_distance_meters": target_distance_meters,
                "charge_density": charge_density,
                "feasibility": {
                    "achievable": False,
                    "field_within_limits": False,
                    "criticality_acceptable": False,
                    "reason": str(e)
                },
                "success": False
            }
        
        # Subtask 17.5: Calculate criticality with found field
        total_energization_time = energization_time + charge_time_minutes
        C_total, C_red, C_warp = calculate_total_criticality(
            t=total_energization_time,
            n=jump_count,
            M=required_field,
            C=cochrane_field,
            phi=phase_offset,
            R=subspace_resonance
        )
        
        criticality_level, status_message = classify_criticality_level(C_total)
        
        # Estimate time to next threshold
        thresholds = [CRITICALITY_WARNING, CRITICALITY_EJECTION, CRITICALITY_FAILURE, CRITICALITY_CATASTROPHIC]
        time_to_next_threshold = None
        for threshold in thresholds:
            if C_total < threshold:
                time_to_next_threshold = estimate_time_to_threshold(
                    current_criticality=C_total,
                    next_threshold=threshold,
                    t=total_energization_time,
                    n=jump_count,
                    phi=phase_offset,
                    R=subspace_resonance
                )
                break
        
        # Subtask 17.6: Assess feasibility (field limits, criticality)
        field_within_limits = 50.0 <= required_field <= 10000.0
        criticality_acceptable = C_total < CRITICALITY_EJECTION  # Below critical threshold
        achievable = field_within_limits and criticality_acceptable
        
        feasibility_reason = []
        if not field_within_limits:
            if required_field < 50.0:
                feasibility_reason.append("Required field strength too low (< 50 Magellans)")
            else:
                feasibility_reason.append(f"Required field strength exceeds tactical limits ({required_field:.1f} > 10000 Magellans)")
        
        if not criticality_acceptable:
            feasibility_reason.append(f"Criticality level {criticality_level} exceeds safe operational threshold")
        
        # Subtask 17.7: Generate warnings and recommendations
        warnings = []
        recommendations = []
        
        # Field strength warnings
        if required_field > 2000.0:
            warnings.append(
                f"Required field strength ({required_field:.1f} Magellans) is very high - "
                f"consider increasing charge time or adjusting parameters"
            )
            recommendations.append("Increase charge time to reduce required field strength")
        
        if required_field < 100.0:
            warnings.append(
                f"Required field strength ({required_field:.1f} Magellans) is very low - "
                f"distance may be achievable with minimal power"
            )
        
        # Charge time warnings
        if charge_time_minutes > SAFE_CHARGE_TIME:
            warnings.append(
                f"Charge time ({charge_time_minutes:.1f} min) exceeds safe limit "
                f"({SAFE_CHARGE_TIME} min) - criticality risk elevated"
            )
            recommendations.append("Reduce charge time to decrease criticality risk")
        
        # Criticality warnings
        if criticality_level != "NOMINAL":
            warnings.append(
                f"Criticality level: {criticality_level} - {status_message}"
            )
            
            if criticality_level == "WARNING":
                recommendations.append("Monitor criticality closely; consider de-energization after jump")
            elif criticality_level in ["CRITICAL", "FAILURE_IMMINENT", "CATASTROPHIC"]:
                recommendations.append("ABORT: Criticality level too high for safe operation")
                recommendations.append("Initiate core de-energization immediately")
        
        # Check for danger zones
        danger_zones = check_resonance_danger_zones(subspace_resonance, phase_offset)
        if danger_zones:
            warnings.extend(danger_zones)
            recommendations.append(f"Adjust subspace resonance away from danger zone (current: {subspace_resonance:.2f} THz)")
        
        # Resonance modulation warnings
        resonance_modulation = calculate_resonance_modulation(subspace_resonance)
        if abs(resonance_modulation) < 0.1:
            warnings.append(
                f"Subspace resonance ({subspace_resonance:.2f} THz) near null zone - "
                f"distance severely limited (modulation: {resonance_modulation:.3f})"
            )
            recommendations.append("Adjust subspace resonance to optimal zone (~25, ~47, ~72, or ~95 THz)")
        
        # Phase offset warnings
        if abs(phase_offset - 0.75) > 0.15:
            warnings.append(
                f"Phase offset ({phase_offset:.2f}) deviates significantly from optimal (0.75) - "
                f"coupling efficiency reduced"
            )
            recommendations.append("Adjust phase offset closer to 0.75 for optimal efficiency")
        
        # Distance warnings
        if target_distance_meters > MAX_DISTANCE_METERS * 0.9:
            warnings.append(
                f"Target distance approaching maximum tactical range - "
                f"consider long-range dimensional folding instead"
            )
            recommendations.append("Use long-range jump system for distances > 25 AU")
        
        # Feasibility recommendations
        if not achievable:
            if not field_within_limits and required_field > 10000.0:
                recommendations.append("Reduce target distance or increase charge time")
                recommendations.append("Consider using long-range jump system for this distance")
            
            if not criticality_acceptable:
                recommendations.append("Reduce energization time or jump count")
                recommendations.append("De-energize core and allow quantum scarring recovery")
        
        # Subtask 17.8: Format field strength output
        field_strength_formatted = f"{required_field:.2f} Magellans"
        
        # Format target distance
        if target_distance_meters < 1000:
            target_distance_formatted = f"{target_distance_meters:.2f} meters"
        elif target_distance_meters < 1e6:
            target_distance_formatted = f"{target_distance_meters / 1000:.2f} kilometers"
        elif target_distance_meters < 1e9:
            target_distance_formatted = f"{target_distance_meters / 1e6:.2f} megameters"
        else:
            au = target_distance_meters / 1.496e11
            target_distance_formatted = f"{au:.3f} AU"
        
        # Subtask 17.9: Build success response with all fields
        return {
            "field_strength_magellans": required_field,
            "field_strength_formatted": field_strength_formatted,
            "target_distance_meters": target_distance_meters,
            "target_distance_formatted": target_distance_formatted,
            "charge_time_minutes": charge_time_minutes,
            "charge_density": charge_density,
            "feasibility": {
                "achievable": achievable,
                "field_within_limits": field_within_limits,
                "criticality_acceptable": criticality_acceptable,
                "reason": " | ".join(feasibility_reason) if feasibility_reason else "Jump is feasible"
            },
            "criticality": {
                "total": C_total,
                "red_matter": C_red,
                "warp_core": C_warp,
                "level": criticality_level,
                "status_message": status_message,
                "time_to_next_threshold_minutes": time_to_next_threshold
            },
            "warnings": warnings,
            "recommendations": recommendations,
            "success": True
        }
    
    except Exception as e:
        # Subtask 17.10: Handle errors and build error response
        return {
            "error": f"Calculation failed: {str(e)}",
            "success": False
        }


def short_range_criticality(
    energization_time_minutes: Annotated[float, Field(
        description=(
            "Minutes since red matter core energization. Range: 0.0 to 60.0. "
            "Criticality grows exponentially with energization time. Used to "
            "calculate red matter criticality component and estimate time to "
            "criticality thresholds."
        ),
        ge=0.0,
        le=60.0
    )],
    jump_count: Annotated[int, Field(
        description=(
            "Number of jumps performed during current energization period. "
            "Range: 0 to 20. Each jump contributes to cumulative quantum "
            "scarring with exponentially increasing impact."
        ),
        ge=0,
        le=20
    )],
    magellan_field: Annotated[float, Field(
        description=(
            "Current red matter field strength in Magellans. Range: 100 to 2000 "
            "typical for tactical operations. Used to calculate interaction "
            "factor between red matter and warp core systems."
        ),
        ge=100.0,
        le=2000.0
    )],
    cochrane_field: Annotated[float, Field(
        default=350.0,
        description=(
            "Warp core coupling strength in millicochranes. Range: 100 to 900. "
            "Defaults to 350. Higher values increase warp core stress component "
            "of criticality."
        ),
        ge=100.0,
        le=900.0
    )] = 350.0,
    phase_offset: Annotated[float, Field(
        default=0.75,
        description=(
            "Phase offset. Range: 0.00 to 1.00. Defaults to 0.75. Affects "
            "criticality modifier through phase-resonance coupling."
        ),
        ge=0.0,
        le=1.0
    )] = 0.75,
    subspace_resonance: Annotated[float, Field(
        default=47.23,
        description=(
            "Subspace resonance frequency in THz. Range: 3.0 to 113.0. Defaults "
            "to 47.23. Affects criticality modifier through resonance modulation."
        ),
        ge=3.0,
        le=113.0
    )] = 47.23,
    charge_time_minutes: Annotated[float, Field(
        default=2.0,
        description=(
            "Charge time for criticality calculation in minutes. Range: 0.3 to "
            "15.0. Defaults to 2.0. Used to calculate warp core stress component."
        ),
        ge=0.3,
        le=15.0
    )] = 2.0
) -> Dict[str, Any]:
    """
    Assess criticality risk for current or planned operational state.
    
    This tool evaluates the quantum scarring and system stress levels based on
    energization time and jump history. It provides detailed criticality breakdown,
    threshold analysis, and tactical recommendations for safe operations.
    
    Args:
        energization_time_minutes: Time since core energization in minutes (required)
        jump_count: Number of jumps performed in current sequence (required)
        magellan_field: Current or planned Magellan field strength (required)
        cochrane_field: Cochrane guide field in millicochranes (default: 350.0)
        phase_offset: Phase offset 0.00-1.00 (default: 0.75)
        subspace_resonance: Subspace resonance frequency in THz (default: 47.23)
        charge_time_minutes: Charge time for criticality calculation (default: 2.0)
    
    Returns:
        Dict[str, Any]: Response dictionary with the following structure:
        
        Success response (success=True):
            - criticality (dict):
                - total (float): Total criticality value
                - red_matter (float): Red matter component
                - warp_core (float): Warp core component
                - level (str): Criticality level name
                - status_message (str): Status description
            - thresholds (dict): Time estimates to each threshold:
                - warning_minutes (float|None): Time to WARNING threshold
                - ejection_minutes (float|None): Time to EJECTION threshold
                - failure_minutes (float|None): Time to FAILURE threshold
                - catastrophic_minutes (float|None): Time to CATASTROPHIC threshold
            - operational_context (dict):
                - energization_time_minutes (float): Time since energization
                - jump_count (int): Number of jumps performed
                - jumps_remaining_estimate (int|None): Estimated safe jumps remaining
            - recommendations (List[str]): Tactical recommendations
            - warnings (List[str]): Operational warnings
            - success (bool): True
        
        Error response (success=False):
            - error (str): Error message
            - validation_errors (List[str]): Validation error details
            - success (bool): False

    Example:
        >>> result = short_range_criticality(
        ...     energization_time_minutes=5.0,
        ...     jump_count=2,
        ...     magellan_field=500.0,
        ...     cochrane_field=350.0,
        ...     phase_offset=0.75,
        ...     subspace_resonance=47.23
        ... )
        >>> print(f"Criticality: {result['criticality']['level']}")
        Criticality: WARNING
    """
    try:
        # Subtask 18.2: Validate input parameters
        is_valid, validation_errors = validate_tactical_parameters(
            charge_time=None,  # Not applicable for criticality assessment
            C=cochrane_field,
            phi=phase_offset,
            R=subspace_resonance,
            distance=None
        )
        
        # Additional validation for criticality-specific parameters
        if energization_time_minutes < 0:
            validation_errors.append("Energization time must be non-negative")
            is_valid = False
        
        if energization_time_minutes > MAX_CHARGE_TIME:
            validation_errors.append(
                f"Energization time ({energization_time_minutes:.1f} min) exceeds "
                f"maximum safe limit ({MAX_CHARGE_TIME} min)"
            )
            is_valid = False
        
        if jump_count < 0:
            validation_errors.append("Jump count must be non-negative")
            is_valid = False
        
        if jump_count > 20:
            validation_errors.append(
                f"Jump count ({jump_count}) exceeds reasonable operational limits"
            )
            is_valid = False
        
        if magellan_field < 0:
            validation_errors.append("Magellan field strength must be non-negative")
            is_valid = False
        
        if magellan_field > 10000.0:
            validation_errors.append(
                f"Magellan field strength ({magellan_field:.1f}) exceeds tactical limits"
            )
            is_valid = False
        
        if not is_valid:
            return {
                "error": "Invalid input parameters",
                "validation_errors": validation_errors,
                "success": False
            }
        
        # Subtask 18.3: Calculate total criticality and components
        C_total, C_red, C_warp = calculate_total_criticality(
            t=energization_time_minutes,
            n=jump_count,
            M=magellan_field,
            C=cochrane_field,
            phi=phase_offset,
            R=subspace_resonance
        )
        
        # Calculate interaction factor for detailed breakdown
        beta_interaction = calculate_interaction_factor(magellan_field, phase_offset, subspace_resonance)
        
        # Subtask 18.4: Classify criticality level
        criticality_level, status_message = classify_criticality_level(C_total)
        
        # Subtask 18.5: Estimate time to each threshold
        thresholds_data = {}
        threshold_values = [
            ("warning", CRITICALITY_WARNING),
            ("ejection", CRITICALITY_EJECTION),
            ("failure", CRITICALITY_FAILURE),
            ("catastrophic", CRITICALITY_CATASTROPHIC)
        ]
        
        for threshold_name, threshold_value in threshold_values:
            reached = C_total >= threshold_value
            time_to_threshold = None
            
            if not reached:
                time_to_threshold = estimate_time_to_threshold(
                    current_criticality=C_total,
                    next_threshold=threshold_value,
                    t=energization_time_minutes,
                    n=jump_count,
                    phi=phase_offset,
                    R=subspace_resonance
                )
            
            thresholds_data[threshold_name] = {
                "value": threshold_value,
                "reached": reached,
                "time_to_minutes": time_to_threshold
            }
        
        # Subtask 18.6: Estimate jumps remaining
        # Estimate how many more jumps can be performed before reaching ejection threshold
        jumps_remaining_estimate = 0
        
        if C_total < CRITICALITY_EJECTION:
            # Simulate additional jumps to find when we exceed ejection threshold
            # Assume each jump takes ~2 minutes charge time
            test_jump_count = jump_count
            test_time = energization_time_minutes
            
            while test_jump_count < jump_count + 20:  # Max 20 additional jumps to test
                test_jump_count += 1
                test_time += 2.0  # Assume 2 minutes per jump
                
                test_criticality, _, _ = calculate_total_criticality(
                    t=test_time,
                    n=test_jump_count,
                    M=magellan_field,
                    C=cochrane_field,
                    phi=phase_offset,
                    R=subspace_resonance
                )
                
                if test_criticality >= CRITICALITY_EJECTION:
                    jumps_remaining_estimate = test_jump_count - jump_count - 1
                    break
            else:
                # If we didn't exceed threshold in 20 jumps, estimate as "many"
                jumps_remaining_estimate = 20
        else:
            jumps_remaining_estimate = 0
        
        # Subtask 18.7: Generate tactical recommendations
        recommendations = []
        warnings = []
        
        # Criticality-based recommendations
        if criticality_level == "NOMINAL":
            recommendations.append("System operating within normal parameters")
            recommendations.append(f"Estimated {jumps_remaining_estimate} jumps remaining before ejection threshold")
            
            if energization_time_minutes > 5.0:
                recommendations.append("Consider de-energization after mission completion to reset quantum scarring")
        
        elif criticality_level == "WARNING":
            warnings.append(f"Tertiary core criticality warning - {status_message}")
            recommendations.append("Monitor criticality levels closely")
            recommendations.append(f"Approximately {jumps_remaining_estimate} jumps remaining before ejection required")
            recommendations.append("Plan for core de-energization after current sequence")
            
            if jump_count > 3:
                recommendations.append("High jump count contributing to criticality - minimize additional jumps")
        
        elif criticality_level == "CRITICAL":
            warnings.append(f"CRITICAL: {status_message}")
            warnings.append("Tertiary core ejection required immediately")
            recommendations.append("ABORT current jump sequence")
            recommendations.append("Initiate tertiary core ejection protocol")
            recommendations.append("Do not attempt additional jumps")
            
            if thresholds_data["failure"]["time_to_minutes"] is not None:
                recommendations.append(
                    f"Primary core failure in approximately {thresholds_data['failure']['time_to_minutes']:.1f} minutes"
                )
        
        elif criticality_level == "FAILURE_IMMINENT":
            warnings.append(f"DANGER: {status_message}")
            warnings.append("Primary core failure imminent")
            recommendations.append("EMERGENCY SHUTDOWN REQUIRED")
            recommendations.append("Eject all cores immediately")
            recommendations.append("Evacuate engineering sections")
            
            if thresholds_data["catastrophic"]["time_to_minutes"] is not None:
                recommendations.append(
                    f"Catastrophic overload in approximately {thresholds_data['catastrophic']['time_to_minutes']:.1f} minutes"
                )
        
        elif criticality_level == "CATASTROPHIC":
            warnings.append(f"CATASTROPHIC: {status_message}")
            warnings.append("Catastrophic overload inevitable")
            recommendations.append("EVACUATE SHIP IMMEDIATELY")
            recommendations.append("All personnel to escape pods")
            recommendations.append("Warp core breach imminent")
        
        # Time-based recommendations
        if energization_time_minutes > SAFE_CHARGE_TIME:
            warnings.append(
                f"Energization time ({energization_time_minutes:.1f} min) exceeds safe operational limit "
                f"({SAFE_CHARGE_TIME} min)"
            )
            recommendations.append("Extended energization increasing criticality exponentially")
        
        # Jump count recommendations
        if jump_count > 5:
            warnings.append(f"High jump count ({jump_count}) - quantum scarring accumulation significant")
            recommendations.append("Quantum scarring from multiple jumps accelerating criticality growth")
        elif jump_count >= 4:
            warnings.append(f"Jump count ({jump_count}) approaching high levels - monitor quantum scarring")
            recommendations.append("Consider limiting additional jumps to prevent excessive quantum scarring")
        
        # Field strength recommendations
        if magellan_field > 1000.0:
            warnings.append(f"High Magellan field strength ({magellan_field:.1f}) increasing warp core stress")
            recommendations.append("Consider reducing field strength for subsequent jumps if possible")
        
        # Phase offset recommendations
        if abs(phase_offset - 0.75) > 0.15:
            warnings.append(
                f"Phase offset ({phase_offset:.2f}) deviates from optimal (0.75) - "
                f"criticality modifier increased"
            )
            recommendations.append("Adjust phase offset closer to 0.75 to reduce criticality growth rate")
        
        # Check for resonance danger zones
        danger_zones = check_resonance_danger_zones(subspace_resonance, phase_offset)
        if danger_zones:
            warnings.extend(danger_zones)
            recommendations.append(
                f"Adjust subspace resonance away from danger zone (current: {subspace_resonance:.2f} THz)"
            )
        
        # Component-specific warnings
        red_matter_percentage = (C_red / C_total * 100) if C_total > 0 else 0
        warp_core_percentage = (C_warp / C_total * 100) if C_total > 0 else 0
        
        if red_matter_percentage > 70:
            warnings.append(
                f"Red matter criticality dominant ({red_matter_percentage:.1f}%) - "
                f"quantum scarring from jumps is primary concern"
            )
            recommendations.append("Reduce jump frequency and energization time to mitigate red matter criticality")
        
        if warp_core_percentage > 40:
            warnings.append(
                f"Warp core stress significant ({warp_core_percentage:.1f}%) - "
                f"Cochrane field coupling contributing to criticality"
            )
            recommendations.append("Consider reducing Cochrane field strength if operationally feasible")
        
        # Subtask 18.8: Build response with all fields
        return {
            "criticality": {
                "total": C_total,
                "red_matter_component": C_red,
                "warp_core_component": C_warp,
                "interaction_factor": beta_interaction,
                "level": criticality_level,
                "status_message": status_message
            },
            "thresholds": thresholds_data,
            "operational_context": {
                "energization_time_minutes": energization_time_minutes,
                "jump_count": jump_count,
                "jumps_remaining_estimate": jumps_remaining_estimate
            },
            "recommendations": recommendations,
            "warnings": warnings,
            "success": True
        }
    
    except Exception as e:
        # Handle errors and build error response
        return {
            "error": f"Criticality calculation failed: {str(e)}",
            "success": False
        }


def short_range_sequential_jumps(
    jump_sequence: Annotated[list[JumpEntry], Field(
        description=(
            "Ordered list of jump objects defining the planned sequence. Each "
            "jump requires distance_meters (float, 1 to 4,500,000,000) and "
            "charge_time_minutes (float, 0.3 to 15.0). Optional per jump: "
            "target_description (string). The tool calculates cumulative "
            "criticality across all jumps and validates the sequence is safe."
        ),
        min_length=1,
        max_length=20
    )],
    cochrane_field: Annotated[float, Field(
        default=350.0,
        description=(
            "Warp core coupling strength in millicochranes for all jumps. "
            "Range: 100 to 900. Defaults to 350."
        ),
        ge=100.0,
        le=900.0
    )] = 350.0,
    phase_offset: Annotated[float, Field(
        default=0.75,
        description=(
            "Phase offset for all jumps. Range: 0.00 to 1.00. Defaults to 0.75."
        ),
        ge=0.0,
        le=1.0
    )] = 0.75,
    subspace_resonance: Annotated[float, Field(
        default=47.23,
        description=(
            "Subspace resonance frequency in THz for all jumps. Range: 3.0 to "
            "113.0. Defaults to 47.23."
        ),
        ge=3.0,
        le=113.0
    )] = 47.23,
    magellan_field: Annotated[float, Field(
        default=500.0,
        description=(
            "Red matter field strength in Magellans for all jumps. Range: 100 to "
            "2000. Defaults to 500."
        ),
        ge=100.0,
        le=2000.0
    )] = 500.0
) -> dict:
    """
    Plan and analyze a sequence of multiple tactical jumps.
    
    Calculates cumulative effects of sequential jumps including:
    - Energization time accumulation
    - Criticality buildup from quantum scarring
    - Field strength requirements for each jump
    - Safety assessment for entire sequence
    
    Workflow Note:
        If you know field parameters (charge time, Magellans) but not target distance,
        call short_range_jump_distance first for each leg to obtain distance_meters,
        then pass those values into the jump sequence.
    
    Args:
        jump_sequence: List of JumpEntry objects with distance_meters, charge_time_minutes, and optional target_description
        cochrane_field: Cochrane guide field in millicochranes (default: 350.0)
        phase_offset: Phase offset 0.00-1.00 (default: 0.75)
        subspace_resonance: Subspace resonance in THz (default: 47.23)
        magellan_field: Red matter field strength in Magellans (default: 500.0)
    
    Returns:
        Dict[str, Any]: Response dictionary with the following structure:
        
        Success response (success=True):
            - sequence_analysis (dict):
                - total_jumps (int): Number of jumps in sequence
                - total_energization_time_minutes (float): Total energization time
                - sequence_safe (bool): Whether entire sequence is safe
                - critical_jump_number (int|None): First unsafe jump (if any)
            - jump_results (List[dict]): Results for each jump:
                - jump_number (int): Jump index (1-based)
                - distance_meters (float): Target distance
                - field_strength_magellans (float|None): Required field
                - criticality_after_jump (float|None): Criticality after this jump
                - criticality_level (str): Level name
                - landing_offset (dict): Landing offset information for this jump:
                    - offset_meters (float): Scalar magnitude of positional error
                    - offset_formatted (str): Human-readable distance with units
                    - directional_components (dict):
                        - fore_aft_meters (float): Forward/aft component (+ = forward, - = aft)
                        - port_starboard_meters (float): Port/starboard component (+ = starboard, - = port)
                        - dorsal_ventral_meters (float): Dorsal/ventral component (+ = dorsal, - = ventral)
                    - directional_summary (str): Plain-language direction description
                    - severity (str): Categorical severity (NEGLIGIBLE|MINOR|SIGNIFICANT|DANGEROUS|CATASTROPHIC)
                    - narrative_summary (str): Complete narrative sentence ready for dialogue
                - safe_to_proceed (bool): Whether safe to continue
                - warnings (List[str]): Jump-specific warnings
            - final_state (dict):
                - criticality_total (float): Final criticality value
                - criticality_level (str): Final level name
                - status_message (str): Final status description
                - energization_time_minutes (float): Total energization time
                - jump_count (int): Total jumps performed
            - recommendations (List[str]): Tactical recommendations
            - success (bool): True
        
        Error response (success=False):
            - error (str): Error message
            - validation_errors (List[str]): Validation error details
            - success (bool): False
        
    Example:
        >>> result = short_range_sequential_jumps(
        ...     jump_sequence=[
        ...         {"distance_meters": 50000, "charge_time_minutes": 2.0},
        ...         {"distance_meters": 75000, "charge_time_minutes": 2.5},
        ...         {"distance_meters": 100000, "charge_time_minutes": 3.0}
        ...     ],
        ...     time_between_jumps_seconds=2.0,
        ...     cochrane_field=350.0
        ... )
    """
    try:
        # Convert JumpEntry objects to dict format expected by the rest of the function
        jump_sequence_list = []
        for entry in jump_sequence:
            jump_dict = {
                "distance_meters": entry.distance_meters,
                "charge_time_minutes": entry.charge_time_minutes,
            }
            if entry.target_description:
                jump_dict["target_description"] = entry.target_description
            jump_sequence_list.append(jump_dict)
        
        # Default time between jumps (not in model, using hardcoded default)
        time_between_jumps_seconds = 2.0
        
        # Subtask 19.2: Validate jump sequence
        if not jump_sequence_list or not isinstance(jump_sequence_list, list):
            return {
                "error": "Jump sequence must be a non-empty list",
                "validation_errors": ["jump_sequence is required and must be a list"],
                "success": False
            }
        
        if len(jump_sequence_list) == 0:
            return {
                "error": "Jump sequence cannot be empty",
                "validation_errors": ["At least one jump must be specified"],
                "success": False
            }
        
        # Validate each jump in sequence
        validation_errors = []
        for i, jump in enumerate(jump_sequence_list):
            if not isinstance(jump, dict):
                validation_errors.append(f"Jump {i+1}: Must be a dictionary")
                continue
            
            if "distance_meters" not in jump:
                validation_errors.append(
                    f"Jump {i+1}: Missing required field 'distance_meters' (float, meters). "
                    f"Each jump object requires: distance_meters, charge_time_minutes. "
                    f"Optional: target_description."
                )
            elif not isinstance(jump["distance_meters"], (int, float)):
                validation_errors.append(f"Jump {i+1}: 'distance_meters' must be a number")
            elif jump["distance_meters"] < MIN_DISTANCE_METERS:
                validation_errors.append(
                    f"Jump {i+1}: Distance ({jump['distance_meters']:.1f} m) below minimum ({MIN_DISTANCE_METERS} m)"
                )
            elif jump["distance_meters"] > MAX_DISTANCE_METERS:
                validation_errors.append(
                    f"Jump {i+1}: Distance ({jump['distance_meters']:.1f} m) exceeds maximum "
                    f"({MAX_DISTANCE_METERS/1e9:.1f} AU)"
                )
            
            if "charge_time_minutes" not in jump:
                validation_errors.append(
                    f"Jump {i+1}: Missing required field 'charge_time_minutes' (float, minutes). "
                    f"Each jump object requires: distance_meters, charge_time_minutes. "
                    f"Optional: target_description."
                )
            elif not isinstance(jump["charge_time_minutes"], (int, float)):
                validation_errors.append(f"Jump {i+1}: 'charge_time_minutes' must be a number")
            elif jump["charge_time_minutes"] <= 0:
                validation_errors.append(f"Jump {i+1}: Charge time must be positive")
            elif jump["charge_time_minutes"] > MAX_CHARGE_TIME:
                validation_errors.append(
                    f"Jump {i+1}: Charge time ({jump['charge_time_minutes']:.1f} min) exceeds maximum "
                    f"({MAX_CHARGE_TIME} min)"
                )
        
        # Validate common parameters
        is_valid, param_errors = validate_tactical_parameters(
            charge_time=None,  # Will validate per-jump
            C=cochrane_field,
            phi=phase_offset,
            R=subspace_resonance
        )
        
        if param_errors:
            validation_errors.extend(param_errors)
        
        if validation_errors:
            return {
                "error": "Jump sequence validation failed",
                "validation_errors": validation_errors,
                "success": False
            }
        
        # Subtask 19.3: Initialize energization tracking
        energization_time = 0.0  # Total time since core energization
        jump_count = 0  # Number of jumps completed
        time_between_jumps_minutes = time_between_jumps_seconds / 60.0
        
        jump_results = []
        critical_jump_index = None
        sequence_safe = True
        
        # Subtask 19.4: Loop through each jump in sequence
        for jump_index, jump in enumerate(jump_sequence_list):
            distance_meters = jump["distance_meters"]
            charge_time_minutes = jump["charge_time_minutes"]
            
            # Add charge time to energization time
            energization_time += charge_time_minutes
            
            # Subtask 19.5: For each jump: integrate charge density
            rho = integrate_charge_density(
                charge_time=charge_time_minutes,
                C=cochrane_field,
                phi=phase_offset,
                R=subspace_resonance
            )
            
            # Subtask 19.6: For each jump: calculate required field
            try:
                M = calculate_required_field_tactical(
                    target_distance=distance_meters,
                    rho=rho,
                    C=cochrane_field,
                    phi=phase_offset,
                    R=subspace_resonance
                )
            except ValueError as e:
                # Field calculation failed - jump not achievable
                jump_results.append({
                    "jump_number": jump_index + 1,
                    "distance_meters": distance_meters,
                    "field_strength_magellans": None,
                    "criticality_after_jump": None,
                    "criticality_level": "UNKNOWN",
                    "safe_to_proceed": False,
                    "warnings": [
                        f"Jump not achievable: {str(e)}",
                        f"Target distance {distance_meters:.1f} m cannot be reached with charge time {charge_time_minutes:.1f} min"
                    ]
                })
                
                if critical_jump_index is None:
                    critical_jump_index = jump_index
                sequence_safe = False
                continue
            
            # Increment jump count (jump is about to be performed)
            jump_count += 1
            
            # Subtask 19.7: For each jump: update criticality
            C_total, C_red, C_warp = calculate_total_criticality(
                t=energization_time,
                n=jump_count,
                M=M,
                C=cochrane_field,
                phi=phase_offset,
                R=subspace_resonance
            )
            
            criticality_level, status_message = classify_criticality_level(C_total)
            
            # Calculate flexure matrix and accuracy degradation for this jump
            flexure_matrix = calculate_flexure_matrix(
                M=M,
                rho=rho,
                phi=phase_offset,
                R=subspace_resonance
            )
            
            # Calculate accuracy degradation as percentage deviation from identity matrix
            diagonal_deviation = (
                abs(flexure_matrix[0][0] - 1.0) +
                abs(flexure_matrix[1][1] - 1.0) +
                abs(flexure_matrix[2][2] - 1.0)
            ) / 3.0
            accuracy_degradation_pct = diagonal_deviation * 100.0
            
            # Calculate landing offset for this jump
            landing_offset = calculate_landing_offset(
                distance_meters=distance_meters,
                accuracy_degradation_pct=accuracy_degradation_pct
            )
            
            # Subtask 19.8: For each jump: check if safe to proceed
            safe_to_proceed = C_total < CRITICALITY_EJECTION  # Below ejection threshold
            
            # Generate warnings for this jump
            jump_warnings = []
            
            if C_total >= CRITICALITY_CATASTROPHIC:
                jump_warnings.append("CATASTROPHIC: Catastrophic overload inevitable - evacuate immediately")
                safe_to_proceed = False
            elif C_total >= CRITICALITY_FAILURE:
                jump_warnings.append("DANGER: Primary core failure imminent - emergency shutdown required")
                safe_to_proceed = False
            elif C_total >= CRITICALITY_EJECTION:
                jump_warnings.append("CRITICAL: Tertiary core ejection required - abort sequence")
                safe_to_proceed = False
            elif C_total >= CRITICALITY_WARNING:
                jump_warnings.append(f"WARNING: {status_message}")
            
            if charge_time_minutes > SAFE_CHARGE_TIME:
                jump_warnings.append(
                    f"Charge time ({charge_time_minutes:.1f} min) exceeds safe limit ({SAFE_CHARGE_TIME} min)"
                )
            
            if M > 1000.0:
                jump_warnings.append(f"High field strength ({M:.1f} Magellans) required - increases stress")
            
            # Check for resonance danger zones
            danger_zones = check_resonance_danger_zones(subspace_resonance, phase_offset)
            if danger_zones:
                jump_warnings.extend(danger_zones)
            
            # Add jump result
            jump_results.append({
                "jump_number": jump_index + 1,
                "distance_meters": distance_meters,
                "field_strength_magellans": M,
                "criticality_after_jump": C_total,
                "criticality_level": criticality_level,
                "landing_offset": landing_offset,
                "safe_to_proceed": safe_to_proceed,
                "warnings": jump_warnings
            })
            
            # Subtask 19.9: Identify critical jump (first unsafe)
            if not safe_to_proceed and critical_jump_index is None:
                critical_jump_index = jump_index
                sequence_safe = False
            
            # Add time between jumps (except after last jump)
            if jump_index < len(jump_sequence_list) - 1:
                energization_time += time_between_jumps_minutes
        
        # Subtask 19.10: Calculate final state
        if jump_count > 0:
            # Get final criticality
            final_criticality = jump_results[-1]["criticality_after_jump"]
            final_level = jump_results[-1]["criticality_level"]
            
            # Determine core status
            if final_criticality is None:
                core_status = "UNKNOWN - Jump sequence incomplete"
            elif final_criticality >= CRITICALITY_CATASTROPHIC:
                core_status = "CATASTROPHIC FAILURE IMMINENT"
            elif final_criticality >= CRITICALITY_FAILURE:
                core_status = "PRIMARY CORE FAILURE IMMINENT"
            elif final_criticality >= CRITICALITY_EJECTION:
                core_status = "TERTIARY CORE EJECTION REQUIRED"
            elif final_criticality >= CRITICALITY_WARNING:
                core_status = "WARNING - Monitor closely"
            else:
                core_status = "NOMINAL - Within safe parameters"
            
            # Estimate recovery time (time for quantum scarring to dissipate)
            # Simplified: assume exponential decay with similar time constant
            if final_criticality is not None and final_criticality > 0.01:
                # Recovery time to reach nominal levels (< 0.01)
                import math
                recovery_time_estimate = XI_DECAY * math.log(final_criticality / 0.01)
                if recovery_time_estimate < 0:
                    recovery_time_estimate = None
            else:
                recovery_time_estimate = None
        else:
            final_criticality = 0.0
            final_level = "NOMINAL"
            core_status = "No jumps completed"
            recovery_time_estimate = None
        
        # Subtask 19.11: Generate sequence recommendations
        recommendations = []
        
        if sequence_safe:
            recommendations.append("All jumps in sequence are within safe operational parameters")
            recommendations.append(
                f"Total energization time: {energization_time:.1f} minutes for {jump_count} jumps"
            )
            
            if final_criticality is not None and final_criticality >= CRITICALITY_WARNING:
                recommendations.append(
                    "Criticality approaching warning threshold - consider de-energization after sequence"
                )
            
            if energization_time > SAFE_CHARGE_TIME:
                recommendations.append(
                    f"Total energization time ({energization_time:.1f} min) exceeds safe limit - "
                    f"monitor criticality closely"
                )
        else:
            if critical_jump_index is not None:
                recommendations.append(
                    f"ABORT: Jump sequence becomes unsafe at jump {critical_jump_index + 1}"
                )
                recommendations.append(
                    f"Maximum safe jumps: {critical_jump_index} of {len(jump_sequence_list)} requested"
                )
            else:
                recommendations.append("ABORT: Jump sequence contains unachievable jumps")
            
            recommendations.append("Do not proceed with full sequence")
            recommendations.append("Consider:")
            recommendations.append("  - Reducing number of jumps")
            recommendations.append("  - Increasing time between jumps for criticality decay")
            recommendations.append("  - Reducing jump distances")
            recommendations.append("  - De-energizing and restarting sequence")
        
        # Jump count recommendations
        if jump_count >= 5:
            recommendations.append(
                f"High jump count ({jump_count}) - quantum scarring accumulation significant"
            )
            recommendations.append("Consider splitting sequence with de-energization period")
        elif jump_count >= 3:
            recommendations.append(
                f"Moderate jump count ({jump_count}) - monitor quantum scarring effects"
            )
        
        # Energization time recommendations
        if energization_time > 10.0:
            recommendations.append(
                f"Extended energization ({energization_time:.1f} min) - criticality growth accelerating"
            )
        
        # Recovery recommendations
        if recovery_time_estimate is not None and recovery_time_estimate > 0:
            recommendations.append(
                f"Estimated recovery time after de-energization: {recovery_time_estimate:.1f} minutes"
            )
            recommendations.append("Allow quantum scarring to dissipate before next sequence")
        
        # Phase offset recommendations
        if abs(phase_offset - 0.75) > 0.15:
            recommendations.append(
                f"Phase offset ({phase_offset:.2f}) deviates from optimal (0.75) - "
                f"adjust for better stability"
            )
        
        # Resonance recommendations
        danger_zones = check_resonance_danger_zones(subspace_resonance, phase_offset)
        if danger_zones:
            recommendations.append(
                f"Subspace resonance ({subspace_resonance:.2f} THz) in danger zone - "
                f"adjust for safer operation"
            )
        
        # Subtask 19.12: Build response with all jump results
        return {
            "sequence_analysis": {
                "total_jumps_requested": len(jump_sequence_list),
                "jumps_feasible": jump_count,
                "total_energization_time_minutes": energization_time,
                "sequence_safe": sequence_safe,
                "critical_jump_index": critical_jump_index
            },
            "jump_results": jump_results,
            "final_state": {
                "total_criticality": final_criticality,
                "criticality_level": final_level,
                "core_status": core_status,
                "recovery_time_estimate_minutes": recovery_time_estimate
            },
            "recommendations": recommendations,
            "success": True
        }
    
    except Exception as e:
        # Handle errors and build error response
        import traceback
        return {
            "error": f"Sequential jump calculation failed: {str(e)}",
            "traceback": traceback.format_exc(),
            "success": False
        }


def short_range_optimize_cochrane(
    phase_offset: Annotated[float, Field(
        default=0.75,
        description=(
            "Phase offset for optimization. Range: 0.00 to 1.00. Defaults to "
            "0.75. The tool identifies safe Cochrane zones for this phase offset."
        ),
        ge=0.0,
        le=1.0
    )] = 0.75,
    subspace_resonance: Annotated[float, Field(
        default=47.23,
        description=(
            "Subspace resonance frequency in THz. Range: 3.0 to 113.0. Defaults "
            "to 47.23. The tool identifies safe Cochrane zones for this resonance."
        ),
        ge=3.0,
        le=113.0
    )] = 47.23,
    optimization_goal: Annotated[Literal["efficiency", "distance", "field", "safety"], Field(
        default="efficiency",
        description=(
            "Optimization strategy for Cochrane field selection. Defaults to "
            "efficiency. "
            "efficiency: Rank zones by average Cochrane coupling efficiency "
            "(standard operations, maximizes power utilization). "
            "distance: Rank zones by maximum achievable jump distance (use when "
            "range is the priority). "
            "field: Rank zones by minimum required Magellan field strength (best "
            "for conserving core output). "
            "safety: Rank zones by safe tolerance margin (use when criticality "
            "is already elevated or maximum safety is required)."
        )
    )] = "efficiency"
) -> Dict[str, Any]:
    """
    Find optimal Cochrane field settings for current conditions.
    
    This tool identifies safe Cochrane field ranges based on phase offset and
    subspace resonance, then ranks them according to the specified optimization
    goal. It helps tactical officers select the best Cochrane field value for
    maximum efficiency, distance, or safety.
    
    Optimization goals:
    - "efficiency": Maximize Cochrane coupling efficiency η(C)
    - "distance": Maximize achievable distance (requires charge_time_minutes)
    - "field": Minimize required field strength (requires target_distance_meters)
    - "safety": Maximize safe tolerance ζ(C)
    
    Args:
        phase_offset: Phase offset 0.00-1.00 (default: 0.75)
        subspace_resonance: Subspace resonance frequency in THz (default: 47.23)
        optimization_goal: Optimization strategy (default: "efficiency")hrane field selection. Controls which 
            metric is used to rank safe operating zones. Valid values:
            
            - "efficiency" (default): Rank zones by average Cochrane coupling efficiency (η). 
              Maximizes energy transfer from warp core to red matter system. Best for standard 
              tactical operations.
            
            - "distance": Rank zones by maximum achievable jump distance within the zone.
              Best when maximum range is the priority. Requires charge_time_minutes parameter.
            
            - "field": Rank zones by minimum required Magellan field strength to reach the
              target distance. Best when conserving red matter core output. Requires 
              target_distance_meters parameter.
            
            - "safety": Rank zones by average safe tolerance margin, minimizing criticality
              risk. Best for high-jump-count sequences or when core is already under stress.
            
            Defaults to "efficiency" if not specified.
        min_efficiency: Minimum acceptable efficiency threshold (default: 0.5)
    
    Returns:
        Dict[str, Any]: Response dictionary with the following structure:
        
        Success response (success=True):
            - safe_zones (List[dict]): Safe Cochrane ranges with analysis:
                - zone_start (float): Starting Cochrane value (millicochranes)
                - zone_end (float): Ending Cochrane value (millicochranes)
                - zone_width (float): Width of safe zone
                - avg_efficiency (float): Average coupling efficiency
                - avg_tolerance (float): Average safe tolerance
                - avg_distance_meters (float): Average distance (if applicable)
                - max_distance_meters (float): Maximum distance (if applicable)
                - max_distance_cochrane (float): Cochrane for max distance
                - avg_required_field (float): Average field (if applicable)
                - min_required_field (float): Minimum field (if applicable)
                - min_field_cochrane (float): Cochrane for min field
                - rank (int): Zone ranking (1 = best)
                - optimization_score (float): Score for ranking
            - optimal_cochrane_field (float): Best Cochrane value overall
            - optimal_zone_index (int): Index of best zone
            - optimization_goal (str): Goal used for ranking
            - danger_zones (List[str]): Active danger zone warnings
            - recommendations (List[str]): Tactical recommendations
            - success (bool): True
        
        Error response (success=False):
            - error (str): Error message
            - validation_errors (List[str]): Validation error details (if applicable)
            - phase_offset (float): Phase offset used (if applicable)
            - subspace_resonance (float): Resonance used (if applicable)
            - recommendations (List[str]): Suggestions (if applicable)
            - success (bool): False
    
    Example:
        >>> result = short_range_optimize_cochrane(
        ...     phase_offset=0.75,
        ...     subspace_resonance=47.23,
        ...     charge_time_minutes=2.0,
        ...     optimization_goal="distance"
        ... )
        >>> print(f"Optimal Cochrane: {result['optimal_cochrane_field']}")
        Optimal Cochrane: 425.0 millicochranes
    """
    try:
        # Parameters not in the model - using defaults
        charge_time_minutes = None
        target_distance_meters = None
        min_efficiency = 0.5
        
        # Subtask 20.2: Validate input parameters
        is_valid, validation_errors = validate_tactical_parameters(
            charge_time=charge_time_minutes,
            C=350.0,  # Dummy value for validation
            phi=phase_offset,
            R=subspace_resonance,
            distance=target_distance_meters
        )
        
        # Remove Cochrane validation error since we're scanning the range
        validation_errors = [e for e in validation_errors if "Cochrane" not in e]
        
        # Validate optimization goal
        valid_goals = ["efficiency", "distance", "field", "safety"]
        if optimization_goal not in valid_goals:
            validation_errors.append(
                f"Invalid optimization_goal '{optimization_goal}'. "
                f"Must be one of: {', '.join(valid_goals)}"
            )
        
        # Validate goal-specific requirements
        if optimization_goal == "distance" and charge_time_minutes is None:
            validation_errors.append(
                "optimization_goal='distance' requires charge_time_minutes parameter"
            )
        
        if optimization_goal == "field" and target_distance_meters is None:
            validation_errors.append(
                "optimization_goal='field' requires target_distance_meters parameter"
            )
        
        # Validate min_efficiency
        if min_efficiency < 0.0 or min_efficiency > 1.0:
            validation_errors.append(
                f"min_efficiency must be between 0.0 and 1.0 (got {min_efficiency})"
            )
        
        if validation_errors:
            return {
                "error": "Invalid input parameters",
                "validation_errors": validation_errors,
                "success": False
            }
        
        # Subtask 20.3: Find safe Cochrane zones
        safe_zones = find_cochrane_safe_zones(
            phi=phase_offset,
            R=subspace_resonance,
            min_efficiency=min_efficiency
        )
        
        if not safe_zones:
            return {
                "error": "No safe Cochrane zones found for current parameters",
                "phase_offset": phase_offset,
                "subspace_resonance": subspace_resonance,
                "min_efficiency": min_efficiency,
                "recommendations": [
                    "No safe operating zones identified with current phase offset and resonance",
                    "Consider adjusting phase offset closer to 0.75",
                    "Consider adjusting subspace resonance to optimal zones (~25, ~47, ~72, ~95 THz)",
                    f"Try lowering min_efficiency threshold (current: {min_efficiency})"
                ],
                "success": False
            }
        
        # Subtask 20.4-20.7: For each zone, calculate metrics and rank
        zone_analysis = []
        
        for zone_start, zone_end in safe_zones:
            # Sample the zone at multiple points to get average metrics
            zone_samples = []
            sample_step = max(10, (zone_end - zone_start) // 10)  # At least 10 samples
            
            for C in range(int(zone_start), int(zone_end) + 1, sample_step):
                # Subtask 20.4: Calculate average efficiency
                efficiency = calculate_cochrane_efficiency(C, phase_offset, subspace_resonance)
                tolerance = calculate_safe_tolerance(C, phase_offset)
                
                sample_data = {
                    "cochrane": C,
                    "efficiency": efficiency,
                    "tolerance": tolerance
                }
                
                # Subtask 20.5: Calculate achievable distance (if charge time given)
                if charge_time_minutes is not None:
                    rho = integrate_charge_density(
                        charge_time=charge_time_minutes,
                        C=C,
                        phi=phase_offset,
                        R=subspace_resonance
                    )
                    
                    # Use a standard tactical field strength for distance calculation
                    M = 500.0
                    distance = calculate_tactical_distance(
                        M=M,
                        rho=rho,
                        C=C,
                        phi=phase_offset,
                        R=subspace_resonance
                    )
                    sample_data["distance_meters"] = distance
                
                # Subtask 20.6: Calculate required field (if distance given)
                if target_distance_meters is not None:
                    rho = integrate_charge_density(
                        charge_time=charge_time_minutes if charge_time_minutes else 2.0,
                        C=C,
                        phi=phase_offset,
                        R=subspace_resonance
                    )
                    
                    try:
                        required_field = calculate_required_field_tactical(
                            target_distance=target_distance_meters,
                            rho=rho,
                            C=C,
                            phi=phase_offset,
                            R=subspace_resonance
                        )
                        sample_data["required_field_magellans"] = required_field
                    except ValueError:
                        # Distance not achievable with this Cochrane value
                        sample_data["required_field_magellans"] = None
                
                zone_samples.append(sample_data)
            
            # Calculate zone averages
            avg_efficiency = sum(s["efficiency"] for s in zone_samples) / len(zone_samples)
            avg_tolerance = sum(s["tolerance"] for s in zone_samples) / len(zone_samples)
            
            zone_info = {
                "zone_start": zone_start,
                "zone_end": zone_end,
                "zone_width": zone_end - zone_start,
                "avg_efficiency": avg_efficiency,
                "avg_tolerance": avg_tolerance,
                "samples": zone_samples
            }
            
            # Add distance metrics if calculated
            if charge_time_minutes is not None:
                distances = [s["distance_meters"] for s in zone_samples]
                zone_info["avg_distance_meters"] = sum(distances) / len(distances)
                zone_info["max_distance_meters"] = max(distances)
                zone_info["max_distance_cochrane"] = zone_samples[distances.index(max(distances))]["cochrane"]
            
            # Add field metrics if calculated
            if target_distance_meters is not None:
                valid_fields = [s["required_field_magellans"] for s in zone_samples 
                               if s["required_field_magellans"] is not None]
                if valid_fields:
                    zone_info["avg_required_field"] = sum(valid_fields) / len(valid_fields)
                    zone_info["min_required_field"] = min(valid_fields)
                    zone_info["min_field_cochrane"] = zone_samples[
                        [s["required_field_magellans"] for s in zone_samples].index(min(valid_fields))
                    ]["cochrane"]
                else:
                    zone_info["avg_required_field"] = None
                    zone_info["min_required_field"] = None
                    zone_info["min_field_cochrane"] = None
            
            zone_analysis.append(zone_info)
        
        # Subtask 20.7: Rank zones by optimization goal
        if optimization_goal == "efficiency":
            # Rank by average efficiency (highest first)
            zone_analysis.sort(key=lambda z: z["avg_efficiency"], reverse=True)
            ranking_metric = "avg_efficiency"
        
        elif optimization_goal == "distance":
            # Rank by maximum achievable distance (highest first)
            zone_analysis.sort(key=lambda z: z.get("max_distance_meters", 0), reverse=True)
            ranking_metric = "max_distance_meters"
        
        elif optimization_goal == "field":
            # Rank by minimum required field (lowest first)
            # Filter out zones where distance is not achievable
            achievable_zones = [z for z in zone_analysis if z.get("min_required_field") is not None]
            if achievable_zones:
                zone_analysis = achievable_zones
                zone_analysis.sort(key=lambda z: z["min_required_field"])
            ranking_metric = "min_required_field"
        
        elif optimization_goal == "safety":
            # Rank by average safe tolerance (highest first)
            zone_analysis.sort(key=lambda z: z["avg_tolerance"], reverse=True)
            ranking_metric = "avg_tolerance"
        
        # Subtask 20.8: Select optimal Cochrane value
        if zone_analysis:
            best_zone = zone_analysis[0]
            
            # Select the specific Cochrane value within the best zone
            if optimization_goal == "efficiency":
                # Find sample with highest efficiency in best zone
                best_sample = max(best_zone["samples"], key=lambda s: s["efficiency"])
                optimal_cochrane = best_sample["cochrane"]
                optimal_metric_value = best_sample["efficiency"]
            
            elif optimization_goal == "distance":
                # Use the Cochrane value that gives maximum distance
                optimal_cochrane = best_zone.get("max_distance_cochrane", 
                                                 (best_zone["zone_start"] + best_zone["zone_end"]) // 2)
                optimal_metric_value = best_zone.get("max_distance_meters", 0)
            
            elif optimization_goal == "field":
                # Use the Cochrane value that requires minimum field
                optimal_cochrane = best_zone.get("min_field_cochrane",
                                                 (best_zone["zone_start"] + best_zone["zone_end"]) // 2)
                optimal_metric_value = best_zone.get("min_required_field", 0)
            
            elif optimization_goal == "safety":
                # Find sample with highest tolerance in best zone
                best_sample = max(best_zone["samples"], key=lambda s: s["tolerance"])
                optimal_cochrane = best_sample["cochrane"]
                optimal_metric_value = best_sample["tolerance"]
        else:
            # No zones found (shouldn't happen after earlier check, but be safe)
            optimal_cochrane = None
            optimal_metric_value = None
        
        # Subtask 20.9: Check for danger zones
        danger_zones = check_resonance_danger_zones(subspace_resonance, phase_offset)
        
        # Subtask 20.10: Generate recommendations
        recommendations = []
        warnings = []
        
        # Zone count recommendations
        if len(safe_zones) == 0:
            warnings.append("No safe Cochrane zones identified")
            recommendations.append("Adjust phase offset or subspace resonance to find safe operating zones")
        elif len(safe_zones) == 1:
            recommendations.append(f"Single safe zone identified: {safe_zones[0][0]}-{safe_zones[0][1]} millicochranes")
            recommendations.append("Limited operational flexibility - consider adjusting parameters for more options")
        else:
            recommendations.append(f"{len(safe_zones)} safe zones identified")
            recommendations.append("Multiple safe operating zones available for tactical flexibility")
        
        # Optimal value recommendations
        if optimal_cochrane is not None:
            recommendations.append(
                f"Optimal Cochrane field: {optimal_cochrane} millicochranes "
                f"(optimized for {optimization_goal})"
            )
            
            # Format the metric value
            if optimization_goal == "efficiency":
                recommendations.append(f"Expected coupling efficiency: {optimal_metric_value:.3f}")
            elif optimization_goal == "distance" and optimal_metric_value is not None:
                if optimal_metric_value < 1000:
                    dist_str = f"{optimal_metric_value:.2f} meters"
                elif optimal_metric_value < 1e6:
                    dist_str = f"{optimal_metric_value / 1000:.2f} kilometers"
                else:
                    dist_str = f"{optimal_metric_value / 1e6:.2f} megameters"
                recommendations.append(f"Expected maximum distance: {dist_str}")
            elif optimization_goal == "field" and optimal_metric_value is not None:
                recommendations.append(f"Expected required field: {optimal_metric_value:.2f} Magellans")
            elif optimization_goal == "safety":
                recommendations.append(f"Expected safe tolerance: {optimal_metric_value:.3f}")
        
        # Danger zone warnings
        if danger_zones:
            warnings.extend(danger_zones)
            recommendations.append(
                f"WARNING: Subspace resonance ({subspace_resonance:.2f} THz) in danger zone"
            )
            recommendations.append("Adjust subspace resonance away from unstable frequencies")
            recommendations.append("Optimal resonance zones: ~25, ~47, ~72, ~95 THz")
        
        # Phase offset recommendations
        if abs(phase_offset - 0.75) > 0.15:
            warnings.append(
                f"Phase offset ({phase_offset:.2f}) deviates significantly from optimal (0.75)"
            )
            recommendations.append("Adjust phase offset closer to 0.75 for improved coupling efficiency")
        
        # Resonance modulation check
        resonance_modulation = calculate_resonance_modulation(subspace_resonance)
        if abs(resonance_modulation) < 0.1:
            warnings.append(
                f"Subspace resonance ({subspace_resonance:.2f} THz) near null zone - "
                f"distance severely limited (modulation: {resonance_modulation:.3f})"
            )
            recommendations.append("CRITICAL: Adjust subspace resonance away from null zone immediately")
            recommendations.append("Null zones: ~0, ~56.5, ~113 THz")
        
        # Zone width recommendations
        if zone_analysis:
            narrow_zones = [z for z in zone_analysis if z["zone_width"] < 50]
            if narrow_zones:
                warnings.append(
                    f"{len(narrow_zones)} narrow safe zones detected (width < 50 millicochranes)"
                )
                recommendations.append("Narrow zones provide limited operational flexibility")
                recommendations.append("Maintain precise Cochrane field control in narrow zones")
        
        # Optimization-specific recommendations
        if optimization_goal == "distance" and charge_time_minutes is not None:
            if charge_time_minutes < 1.0:
                recommendations.append(
                    f"Short charge time ({charge_time_minutes:.1f} min) limits distance capability"
                )
                recommendations.append("Consider increasing charge time for greater range")
            elif charge_time_minutes > SAFE_CHARGE_TIME:
                warnings.append(
                    f"Charge time ({charge_time_minutes:.1f} min) exceeds safe limit ({SAFE_CHARGE_TIME} min)"
                )
                recommendations.append("Extended charge time increases criticality risk")
        
        if optimization_goal == "field" and target_distance_meters is not None:
            # Check if any zones can achieve the target
            achievable_zones = [z for z in zone_analysis if z.get("min_required_field") is not None]
            if not achievable_zones:
                warnings.append(
                    f"Target distance ({target_distance_meters:.1f} m) may not be achievable "
                    f"with current parameters"
                )
                recommendations.append("Consider:")
                recommendations.append("  - Increasing charge time")
                recommendations.append("  - Adjusting subspace resonance to optimal zone")
                recommendations.append("  - Reducing target distance")
        
        # Subtask 20.11: Build response with all zone data
        # Format zone data for response (remove detailed samples to reduce size)
        zones_summary = []
        for zone in zone_analysis:
            zone_summary = {
                "zone_start": zone["zone_start"],
                "zone_end": zone["zone_end"],
                "zone_width": zone["zone_width"],
                "avg_efficiency": zone["avg_efficiency"],
                "avg_tolerance": zone["avg_tolerance"]
            }
            
            if "max_distance_meters" in zone:
                zone_summary["max_distance_meters"] = zone["max_distance_meters"]
                zone_summary["max_distance_cochrane"] = zone["max_distance_cochrane"]
            
            if "min_required_field" in zone:
                zone_summary["min_required_field"] = zone["min_required_field"]
                zone_summary["min_field_cochrane"] = zone["min_field_cochrane"]
            
            zones_summary.append(zone_summary)
        
        return {
            "optimal_cochrane_field": optimal_cochrane,
            "optimization_goal": optimization_goal,
            "ranking_metric": ranking_metric,
            "safe_zones": zones_summary,
            "total_safe_zones": len(safe_zones),
            "parameters": {
                "phase_offset": phase_offset,
                "subspace_resonance": subspace_resonance,
                "charge_time_minutes": charge_time_minutes,
                "target_distance_meters": target_distance_meters,
                "min_efficiency": min_efficiency
            },
            "warnings": warnings,
            "recommendations": recommendations,
            "danger_zones_active": danger_zones,
            "success": True
        }
    
    except Exception as e:
        # Handle errors and build error response
        import traceback
        return {
            "error": f"Cochrane optimization failed: {str(e)}",
            "traceback": traceback.format_exc(),
            "success": False
        }
