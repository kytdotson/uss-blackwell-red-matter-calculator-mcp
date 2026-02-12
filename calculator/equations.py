"""
Mathematical equations for USS Blackwell Red Matter Core dimensional fold calculations.

This module implements the core Blackwell Drive equation and related mathematical
functions for calculating jump distances and required field strengths. All functions
are pure mathematical operations with no external dependencies beyond Python's math library.
"""

from calculator.constants import (
    EFFICIENCY_STANDARD_MAX,
    EFFICIENCY_OPTIMAL_MAX,
    XI_STANDARD,
    XI_OPTIMAL,
    XI_DIMINISHING
)


def get_efficiency_factor(field_strength: float) -> float:
    """
    Calculate the efficiency factor ξ(M) based on field strength.
    
    The efficiency factor is a piecewise function representing field harmonic behavior:
    - Standard zone (M < 1,000): ξ = 1.0
    - Optimal zone (1,000 <= M < 10,000): ξ = 1.2
    - Diminishing zone (M >= 10,000): ξ = 0.8
    
    Args:
        field_strength: Red matter field strength in Magellans
        
    Returns:
        Efficiency factor (1.0, 1.2, or 0.8)
        
    Requirements:
        - 5.4: Standard zone efficiency factor
        - 5.5: Optimal zone efficiency factor
        - 5.6: Diminishing zone efficiency factor
    """
    if field_strength < EFFICIENCY_STANDARD_MAX:
        return XI_STANDARD
    elif field_strength < EFFICIENCY_OPTIMAL_MAX:
        return XI_OPTIMAL
    else:
        return XI_DIMINISHING


def calculate_jump_distance(field_strength: float) -> float:
    """
    Calculate jump distance using the Blackwell Drive equation.
    
    The dimensional fold equation is:
    D = K × ln(M − M₀) × √(M / Mₓ) × ξ(M)
    
    Where:
    - D: Jump distance in light-years
    - K: Dimensional constant (12.7)
    - M: Field strength in Magellans
    - M₀: Safety threshold (200 Magellans)
    - Mₓ: Critical resonance point (1847 Magellans)
    - ξ(M): Efficiency factor (piecewise function)
    
    Args:
        field_strength: Red matter field strength in Magellans (must be > M₀)
        
    Returns:
        Jump distance in light-years
        
    Raises:
        ValueError: If field_strength <= M₀ (200 Magellans)
        
    Requirements:
        - 5.1: Calculate jump distance using the Blackwell Drive equation
        - 5.2: Raise error if field strength is at or below safety threshold
    """
    import math
    from calculator.constants import M0, MX, K
    
    if field_strength <= M0:
        raise ValueError(f"Field strength must be greater than {M0} Magellans (safety threshold M0)")
    
    # Get efficiency factor for this field strength
    xi = get_efficiency_factor(field_strength)
    
    # Calculate jump distance using the Blackwell Drive equation
    # D = K × ln(M − M₀) × √(M / Mₓ) × ξ(M)
    distance = K * math.log(field_strength - M0) * math.sqrt(field_strength / MX) * xi
    
    return distance


def format_field_strength(field_strength: float) -> str:
    """
    Format field strength value with human-readable SI-style prefixes.
    
    Formats field strength using appropriate unit prefixes:
    - MegaMagellans (MM) for values >= 1,000,000
    - kiloMagellans (kM) for values >= 1,000 but < 1,000,000
    - Magellans (M) for values < 1,000
    
    All values are formatted to 2 decimal places.
    
    Args:
        field_strength: Red matter field strength in Magellans
        
    Returns:
        Formatted string with appropriate unit prefix
        
    Examples:
        >>> format_field_strength(2500000.0)
        '2.50 MegaMagellans'
        >>> format_field_strength(1500.0)
        '1.50 kiloMagellans'
        >>> format_field_strength(250.5)
        '250.50 Magellans'
        
    Requirements:
        - 8.1: Format as MegaMagellans when M >= 1,000,000
        - 8.2: Format as kiloMagellans when 1,000 <= M < 1,000,000
        - 8.3: Format as Magellans when M < 1,000
    """
    if field_strength >= 1_000_000.0:
        return f"{field_strength / 1_000_000.0:.2f} MegaMagellans"
    elif field_strength >= 1_000.0:
        return f"{field_strength / 1_000.0:.2f} kiloMagellans"
    else:
        return f"{field_strength:.2f} Magellans"



def calculate_field_strength(target_distance: float) -> float:
    """
    Calculate required field strength for a target jump distance using Newton-Raphson iteration.
    
    This function inverts the Blackwell Drive equation to find the field strength M
    that produces the desired jump distance D. The solver uses numerical derivatives
    to handle efficiency zone discontinuities.
    
    Newton-Raphson iteration:
    1. Start with initial guess (1000 Magellans)
    2. Calculate distance at current M
    3. Calculate numerical derivative: f'(M) ≈ [f(M + ΔM) - f(M)] / ΔM
    4. Update: M_new = M - (calculated_distance - target_distance) / f'(M)
    5. Clamp M to stay > M₀
    6. Repeat until |calculated_distance - target_distance| < tolerance
    
    Args:
        target_distance: Desired jump distance in light-years (must be > 0)
        
    Returns:
        Required field strength in Magellans
        
    Raises:
        ValueError: If target_distance <= 0
        ValueError: If solver fails to converge within max iterations
        ValueError: If required field strength exceeds computational bounds
        
    Requirements:
        - 6.1: Calculate field strength using Newton-Raphson iteration
        - 6.2: Raise error if target distance is zero or negative
        - 6.3: Converge within 0.01 light-years of target distance
        - 6.4: Return error if no convergence within 100 iterations
        - 6.5: Return error if field strength exceeds 4,000,000 Magellans
        - 14.1: Use ΔM = 1 Magellan for numerical derivative
        - 14.2: Prevent field strength from falling at or below 200 Magellans
        - 14.3: Terminate with error if M > 4,000,000 without convergence
        - 14.4: Return converged field strength when within tolerance
        - 14.5: Return error after 100 iterations without convergence
    """
    import math
    from calculator.constants import (
        M0,
        NR_INITIAL_GUESS,
        NR_TOLERANCE,
        NR_MAX_ITERATIONS,
        NR_DELTA_M,
        NR_MAX_M
    )
    
    # Validate input
    if target_distance <= 0:
        raise ValueError("Target distance must be greater than 0 light-years")
    
    # Initialize Newton-Raphson iteration
    M = NR_INITIAL_GUESS
    
    for iteration in range(NR_MAX_ITERATIONS):
        # Check if field strength exceeds computational bounds
        if M > NR_MAX_M:
            raise ValueError(
                f"Target distance requires field strength beyond safe computational bounds "
                f"(exceeded {NR_MAX_M} Magellans)"
            )
        
        # Calculate distance at current field strength
        calculated_distance = calculate_jump_distance(M)
        
        # Check convergence
        error = abs(calculated_distance - target_distance)
        if error < NR_TOLERANCE:
            return M
        
        # Calculate numerical derivative: f'(M) ≈ [f(M + ΔM) - f(M)] / ΔM
        M_plus_delta = M + NR_DELTA_M
        distance_plus_delta = calculate_jump_distance(M_plus_delta)
        derivative = (distance_plus_delta - calculated_distance) / NR_DELTA_M
        
        # Avoid division by zero
        if abs(derivative) < 1e-10:
            raise ValueError("Solver encountered zero derivative - cannot converge")
        
        # Newton-Raphson update: M_new = M - f(M) / f'(M)
        # where f(M) = calculated_distance - target_distance
        M_new = M - (calculated_distance - target_distance) / derivative
        
        # Clamp M to stay above safety threshold
        if M_new <= M0:
            M_new = M0 + 1.0  # Stay just above threshold
        
        M = M_new
    
    # Failed to converge within max iterations
    raise ValueError(
        f"Solver failed to converge within {NR_MAX_ITERATIONS} iterations "
        f"(last error: {error:.4f} light-years)"
    )
