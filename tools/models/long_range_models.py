"""
Pydantic models for long-range jump calculation tools.

This module defines parameter models for:
- long_range_jump_distance: Calculate jump distance from field strength
- long_range_field_strength: Calculate required field strength for target distance
"""

from pydantic import BaseModel, Field


class LongRangeJumpDistanceArgs(BaseModel):
    """Parameters for long_range_jump_distance tool."""
    
    field_strength_magellans: float = Field(
        description=(
            "Red matter field strength in Magellans. The Magellan (M) measures "
            "the field intensity required to flex one cubic meter of spacetime "
            "by one Planck length. Range: 200.01 to 3,000,000. Safe operating "
            "range: 500 to 2,000,000. Values ≤200 cause equation failure (safety "
            "threshold M₀). Values 200-500 are extremely dangerous (high fold "
            "collapse risk). Values >2,000,000 exceed safe limits (core "
            "destabilization risk). Values >3,000,000 cause catastrophic overload."
        ),
        gt=200.0,
        le=3_000_000.0
    )


class LongRangeFieldStrengthArgs(BaseModel):
    """Parameters for long_range_field_strength tool."""
    
    target_distance_light_years: float = Field(
        description=(
            "Target jump distance in light-years. Must be positive. The system "
            "uses Newton-Raphson iteration to calculate the required field "
            "strength. Typical range: 1 to 50,000 light-years. Distances >50,000 "
            "may require field strengths exceeding safe limits."
        ),
        gt=0.0
    )
