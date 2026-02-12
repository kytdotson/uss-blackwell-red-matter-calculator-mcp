"""Safety classification system for USS Blackwell Red Matter Core.

This module provides safety status classification for field strength values,
warning generation, and power utilization calculations.
"""

from enum import Enum


class SafetyStatus(str, Enum):
    """Safety status classification for red matter field strength.
    
    Classifies field strength values into safety categories based on
    operational boundaries defined in the USS Blackwell specifications.
    """
    
    CRITICAL_FAILURE = "CRITICAL_FAILURE"
    EXTREMELY_DANGEROUS = "EXTREMELY_DANGEROUS"
    CAUTION_ADVISED = "CAUTION_ADVISED"
    WITHIN_SAFE_PARAMETERS = "WITHIN_SAFE_PARAMETERS"
    EXCEEDS_SAFE_LIMITS = "EXCEEDS_SAFE_LIMITS"
    CATASTROPHIC_OVERLOAD_RISK = "CATASTROPHIC_OVERLOAD_RISK"


def classify_safety_status(field_strength: float) -> SafetyStatus:
    """Classify the safety status of a given field strength.
    
    Args:
        field_strength: Red matter field strength in Magellans
        
    Returns:
        SafetyStatus enum value corresponding to the field strength range
        
    Safety Ranges:
        - M <= 200: CRITICAL_FAILURE
        - 200 < M < 500: EXTREMELY_DANGEROUS
        - 500 <= M < 1000: CAUTION_ADVISED
        - 1000 <= M <= 2,000,000: WITHIN_SAFE_PARAMETERS
        - 2,000,000 < M <= 3,000,000: EXCEEDS_SAFE_LIMITS
        - M > 3,000,000: CATASTROPHIC_OVERLOAD_RISK
    """
    if field_strength <= 200:
        return SafetyStatus.CRITICAL_FAILURE
    elif field_strength < 500:
        return SafetyStatus.EXTREMELY_DANGEROUS
    elif field_strength < 1000:
        return SafetyStatus.CAUTION_ADVISED
    elif field_strength <= 2_000_000:
        return SafetyStatus.WITHIN_SAFE_PARAMETERS
    elif field_strength <= 3_000_000:
        return SafetyStatus.EXCEEDS_SAFE_LIMITS
    else:
        return SafetyStatus.CATASTROPHIC_OVERLOAD_RISK


def generate_warnings(field_strength: float, safety_status: SafetyStatus) -> list[str]:
    """Generate warning messages based on field strength and safety status.
    
    Args:
        field_strength: Red matter field strength in Magellans
        safety_status: Current safety status classification
        
    Returns:
        List of warning strings. Empty list if no warnings needed.
        
    Warning Conditions:
        - WITHIN_SAFE_PARAMETERS: No warnings
        - EXTREMELY_DANGEROUS: "EXTREMELY DANGEROUS: Field strength is critically low"
        - CAUTION_ADVISED: "CAUTION: Field strength is below optimal operating range"
        - EXCEEDS_SAFE_LIMITS: "WARNING: Field strength exceeds maximum safe output"
        - CRITICAL_FAILURE and CATASTROPHIC_OVERLOAD_RISK: No warnings (handled as errors)
    """
    if safety_status == SafetyStatus.WITHIN_SAFE_PARAMETERS:
        return []
    elif safety_status == SafetyStatus.EXTREMELY_DANGEROUS:
        return ["EXTREMELY DANGEROUS: Field strength is critically low"]
    elif safety_status == SafetyStatus.CAUTION_ADVISED:
        return ["CAUTION: Field strength is below optimal operating range"]
    elif safety_status == SafetyStatus.EXCEEDS_SAFE_LIMITS:
        return ["WARNING: Field strength exceeds maximum safe output"]
    else:
        # CRITICAL_FAILURE and CATASTROPHIC_OVERLOAD_RISK are handled as errors
        return []


def calculate_power_utilization(field_strength: float) -> float:
    """Calculate power utilization as percentage of maximum safe field strength.
    
    Args:
        field_strength: Red matter field strength in Magellans
        
    Returns:
        Percentage of 2 MegaMagellan ceiling (0-100+)
        
    Formula:
        (field_strength / 2,000,000.0) * 100.0
    """
    return (field_strength / 2_000_000.0) * 100.0

