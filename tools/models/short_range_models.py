"""
Pydantic models for short-range (tactical) jump calculation tools.

This module defines parameter models for:
- short_range_jump_distance: Calculate tactical jump distance
- short_range_field_strength: Calculate required field strength for tactical jump
- short_range_criticality: Calculate system criticality level
- short_range_sequential_jumps: Plan and validate jump sequences
- short_range_optimize_cochrane: Find optimal Cochrane field zones
"""

from typing import Literal, Optional
from pydantic import BaseModel, Field


class ShortRangeJumpDistanceArgs(BaseModel):
    """Parameters for short_range_jump_distance tool."""
    
    charge_time_minutes: float = Field(
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
    )
    
    cochrane_field: float = Field(
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
    )
    
    phase_offset: float = Field(
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
    )
    
    subspace_resonance: float = Field(
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
    )
    
    magellan_field: Optional[float] = Field(
        default=None,
        description=(
            "Instantaneous red matter field strength in Magellans at jump "
            "execution. Optional. If not provided, defaults to 500.0 (typical "
            "tactical field strength). Range: 100 to 2000 typical for tactical "
            "jumps. Unlike long-range jumps, tactical jumps use charge density "
            "multiplication, so lower field strengths are sufficient."
        )
    )
    
    energization_time: float = Field(
        default=0.0,
        description=(
            "Minutes since red matter core energization. Used for criticality "
            "tracking. Range: 0.0 to 60.0. Defaults to 0.0 (first jump in "
            "sequence). Criticality accumulates exponentially with energization "
            "time. Core de-energization required for quantum scarring recovery."
        ),
        ge=0.0,
        le=60.0
    )
    
    jump_count: int = Field(
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
    )


class ShortRangeFieldStrengthArgs(BaseModel):
    """Parameters for short_range_field_strength tool."""
    
    target_distance_meters: float = Field(
        description=(
            "Target tactical jump distance in meters. Range: 1 to 4,500,000,000 "
            "(30 AU). Tactical jumps operate from 1 meter to 30 AU using "
            "quantum-scale subspace resonances. The system uses Newton-Raphson "
            "iteration to calculate required field strength and charge time."
        ),
        ge=1.0,
        le=4_500_000_000.0
    )
    
    cochrane_field: float = Field(
        default=350.0,
        description=(
            "Warp core coupling strength in millicochranes. Range: 100 to 900. "
            "Defaults to 350. See short_range_jump_distance for detailed "
            "description."
        ),
        ge=100.0,
        le=900.0
    )
    
    phase_offset: float = Field(
        default=0.75,
        description=(
            "Phase offset for temporal alignment. Range: 0.00 to 1.00. Defaults "
            "to 0.75 (optimal). See short_range_jump_distance for detailed "
            "description."
        ),
        ge=0.0,
        le=1.0
    )
    
    subspace_resonance: float = Field(
        default=47.23,
        description=(
            "Subspace resonance frequency in THz. Range: 3.0 to 113.0. Defaults "
            "to 47.23. See short_range_jump_distance for detailed description."
        ),
        ge=3.0,
        le=113.0
    )


class ShortRangeCriticalityArgs(BaseModel):
    """Parameters for short_range_criticality tool."""
    
    energization_time_minutes: float = Field(
        description=(
            "Minutes since red matter core energization. Range: 0.0 to 60.0. "
            "Criticality grows exponentially with energization time. Used to "
            "calculate red matter criticality component and estimate time to "
            "criticality thresholds."
        ),
        ge=0.0,
        le=60.0
    )
    
    jump_count: int = Field(
        description=(
            "Number of jumps performed during current energization period. "
            "Range: 0 to 20. Each jump contributes to cumulative quantum "
            "scarring with exponentially increasing impact."
        ),
        ge=0,
        le=20
    )
    
    magellan_field: float = Field(
        description=(
            "Current red matter field strength in Magellans. Range: 100 to 2000 "
            "typical for tactical operations. Used to calculate interaction "
            "factor between red matter and warp core systems."
        ),
        ge=100.0,
        le=2000.0
    )
    
    cochrane_field: float = Field(
        default=350.0,
        description=(
            "Warp core coupling strength in millicochranes. Range: 100 to 900. "
            "Defaults to 350. Higher values increase warp core stress component "
            "of criticality."
        ),
        ge=100.0,
        le=900.0
    )
    
    phase_offset: float = Field(
        default=0.75,
        description=(
            "Phase offset. Range: 0.00 to 1.00. Defaults to 0.75. Affects "
            "criticality modifier through phase-resonance coupling."
        ),
        ge=0.0,
        le=1.0
    )
    
    subspace_resonance: float = Field(
        default=47.23,
        description=(
            "Subspace resonance frequency in THz. Range: 3.0 to 113.0. Defaults "
            "to 47.23. Affects criticality modifier through resonance modulation."
        ),
        ge=3.0,
        le=113.0
    )
    
    charge_time_minutes: float = Field(
        default=2.0,
        description=(
            "Charge time for criticality calculation in minutes. Range: 0.3 to "
            "15.0. Defaults to 2.0. Used to calculate warp core stress component."
        ),
        ge=0.3,
        le=15.0
    )


class JumpEntry(BaseModel):
    """Single jump in a sequential jump sequence."""
    
    distance_meters: float = Field(
        description=(
            "Target jump distance for this leg in meters. Range: 1 to "
            "4,500,000,000 (30 AU). Each jump in the sequence can have a "
            "different distance."
        ),
        ge=1.0,
        le=4_500_000_000.0
    )
    
    charge_time_minutes: float = Field(
        description=(
            "Core charge time for this specific jump in minutes. Range: 0.3 to "
            "15.0. Each jump can have a different charge time. Longer charge "
            "times enable greater distances but increase criticality."
        ),
        ge=0.3,
        le=15.0
    )
    
    target_description: str = Field(
        default="",
        description=(
            "Optional human-readable label for this jump leg. Examples: "
            "'Approach asteroid', 'Evade debris field', 'Final approach to "
            "station'. Defaults to empty string."
        )
    )


class ShortRangeSequentialJumpsArgs(BaseModel):
    """Parameters for short_range_sequential_jumps tool."""
    
    jump_sequence: list[JumpEntry] = Field(
        description=(
            "Ordered list of jump objects defining the planned sequence. Each "
            "jump requires distance_meters (float, 1 to 4,500,000,000) and "
            "charge_time_minutes (float, 0.3 to 15.0). Optional per jump: "
            "target_description (string). The tool calculates cumulative "
            "criticality across all jumps and validates the sequence is safe."
        ),
        min_length=1,
        max_length=20
    )
    
    cochrane_field: float = Field(
        default=350.0,
        description=(
            "Warp core coupling strength in millicochranes for all jumps. "
            "Range: 100 to 900. Defaults to 350."
        ),
        ge=100.0,
        le=900.0
    )
    
    phase_offset: float = Field(
        default=0.75,
        description=(
            "Phase offset for all jumps. Range: 0.00 to 1.00. Defaults to 0.75."
        ),
        ge=0.0,
        le=1.0
    )
    
    subspace_resonance: float = Field(
        default=47.23,
        description=(
            "Subspace resonance frequency in THz for all jumps. Range: 3.0 to "
            "113.0. Defaults to 47.23."
        ),
        ge=3.0,
        le=113.0
    )
    
    magellan_field: float = Field(
        default=500.0,
        description=(
            "Red matter field strength in Magellans for all jumps. Range: 100 to "
            "2000. Defaults to 500."
        ),
        ge=100.0,
        le=2000.0
    )


class ShortRangeOptimizeCochraneArgs(BaseModel):
    """Parameters for short_range_optimize_cochrane tool."""
    
    phase_offset: float = Field(
        default=0.75,
        description=(
            "Phase offset for optimization. Range: 0.00 to 1.00. Defaults to "
            "0.75. The tool identifies safe Cochrane zones for this phase offset."
        ),
        ge=0.0,
        le=1.0
    )
    
    subspace_resonance: float = Field(
        default=47.23,
        description=(
            "Subspace resonance frequency in THz. Range: 3.0 to 113.0. Defaults "
            "to 47.23. The tool identifies safe Cochrane zones for this resonance."
        ),
        ge=3.0,
        le=113.0
    )
    
    optimization_goal: Literal["efficiency", "distance", "field", "safety"] = Field(
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
    )
