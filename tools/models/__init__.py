"""
Pydantic models for USS Blackwell Red Matter Calculator MCP server tool parameters.

This module provides comprehensive parameter validation and documentation for all
tools, following the patterns specified in issue-mcp-parameter-description-guide.md.
"""

from tools.models.long_range_models import (
    LongRangeJumpDistanceArgs,
    LongRangeFieldStrengthArgs,
)

from tools.models.short_range_models import (
    ShortRangeJumpDistanceArgs,
    ShortRangeFieldStrengthArgs,
    ShortRangeCriticalityArgs,
    JumpEntry,
    ShortRangeSequentialJumpsArgs,
    ShortRangeOptimizeCochraneArgs,
)

__all__ = [
    "LongRangeJumpDistanceArgs",
    "LongRangeFieldStrengthArgs",
    "ShortRangeJumpDistanceArgs",
    "ShortRangeFieldStrengthArgs",
    "ShortRangeCriticalityArgs",
    "JumpEntry",
    "ShortRangeSequentialJumpsArgs",
    "ShortRangeOptimizeCochraneArgs",
]
