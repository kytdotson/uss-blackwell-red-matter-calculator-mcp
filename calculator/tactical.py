"""
Tactical jump calculations for USS Blackwell Red Matter Core.

This module implements the extreme close-range tactical jump system equations,
enabling precision maneuvers within stellar systems (meters to 30 AU). Unlike
long-range dimensional folding which operates on macro-spacetime geometry,
tactical jumps exploit quantum-scale subspace resonances.

Key features:
- Time-dependent charge accumulation with exponential decay
- Multiple interacting field systems (red matter core + warp core)
- Phase offset and subspace resonance tuning parameters
- Cumulative quantum scarring from sequential jumps
- Exponential criticality risk buildup
- Complex coordinate transformation matrices

All functions are pure mathematical operations with no external dependencies
beyond Python's math library and typing annotations.
"""

import math
from typing import Tuple, List, Optional



# =============================================================================
# Modulation Factor Functions
# =============================================================================

def calculate_resonance_modulation(R: float) -> float:
    """
    Calculate subspace resonance modulation factor Ψ(R).
    
    Equation: Ψ(R) = (R/50)^0.4 × sin(πR/56.5) × (1 + 0.1×cos(2πR/113))
    
    This factor modulates jump distance based on local subspace frequency.
    Optimal resonance zones occur at ~25, ~47, ~72, ~95 THz where the
    modulation factor is maximized. Null zones at ~0, ~56.5, ~113 THz
    produce near-zero or negative modulation.
    
    Args:
        R: Subspace resonance frequency in THz (3.00-113.00)
        
    Returns:
        Resonance modulation factor (can be negative in null zones)
        
    Requirements:
        - Design 3.2.1: Subspace Resonance Modulation
    """
    term1 = (R / 50.0) ** 0.4
    term2 = math.sin(math.pi * R / 56.5)
    term3 = 1.0 + 0.1 * math.cos(2.0 * math.pi * R / 113.0)
    
    return term1 * term2 * term3


def calculate_phase_resonance_coupling(phi: float, R: float) -> float:
    """
    Calculate phase-resonance coupling factor Ω(φ,R).
    
    Equation: Ω(φ,R) = 0.8 + 0.2×cos(2πφ + πR/113) × (1 - |φ - 0.75|)
    
    This factor represents the interaction between phase offset and subspace
    resonance settings. Optimal coupling occurs when phase offset is near
    0.75 (the default), with deviation reducing coupling efficiency.
    
    Args:
        phi: Phase offset (0.00-1.00)
        R: Subspace resonance frequency in THz (3.00-113.00)
        
    Returns:
        Phase-resonance coupling factor (0.6-1.0 range)
        
    Requirements:
        - Design 3.2.2: Phase-Resonance Coupling
    """
    cos_term = math.cos(2.0 * math.pi * phi + math.pi * R / 113.0)
    deviation_term = 1.0 - abs(phi - 0.75)
    
    return 0.8 + 0.2 * cos_term * deviation_term


def calculate_safe_tolerance(C: float, phi: float) -> float:
    """
    Calculate safe tolerance function ζ(C).
    
    Equation: ζ(C) = 0.7 + 0.3 × cos(2πC/180 + πφ/2)
    
    This factor represents the safety margin in Cochrane field operations,
    modulated by both the field strength and phase offset. It affects the
    overall coupling efficiency and system stability.
    
    Args:
        C: Cochrane guide field in millicochranes (100-900)
        phi: Phase offset (0.00-1.00)
        
    Returns:
        Safe tolerance factor (0.4-1.0 range)
        
    Requirements:
        - Design 3.2.3: Safe Tolerance Function
    """
    return 0.7 + 0.3 * math.cos(2.0 * math.pi * C / 180.0 + math.pi * phi / 2.0)


def calculate_cochrane_efficiency(C: float, phi: float, R: float) -> float:
    """
    Calculate Cochrane coupling efficiency η(C).
    
    Equation: η(C) = ln(C + δ) × |sin(πC/C_max)| × ζ(C) × Ω(φ,R)
    
    This is the primary efficiency factor for warp field coupling to the
    red matter core. It combines logarithmic scaling, harmonic oscillation,
    safe tolerance, and phase-resonance coupling effects.
    
    Args:
        C: Cochrane guide field in millicochranes (100-900)
        phi: Phase offset (0.00-1.00)
        R: Subspace resonance frequency in THz (3.00-113.00)
        
    Returns:
        Cochrane coupling efficiency factor (positive value)
        
    Requirements:
        - Design 3.2.4: Cochrane Coupling Efficiency
        - Requires: calculate_safe_tolerance, calculate_phase_resonance_coupling
    """
    from calculator.constants import DELTA, C_MAX
    
    ln_term = math.log(C + DELTA)
    sin_term = abs(math.sin(math.pi * C / C_MAX))
    zeta = calculate_safe_tolerance(C, phi)
    omega = calculate_phase_resonance_coupling(phi, R)
    
    return ln_term * sin_term * zeta * omega



# =============================================================================
# Power Integration Functions
# =============================================================================

def calculate_phase_timing_modulation(phi: float, tau: float) -> float:
    """
    Calculate phase timing modulation Φ(φ,τ).
    
    Equation: Φ(φ,τ) = 1 + 0.3×sin(2πφ + 0.5τ) × e^(-0.1τ)
    
    This factor modulates warp core power contribution based on phase offset
    and time since energization. The exponential decay term represents
    stabilization of the phase lock over time.
    
    Args:
        phi: Phase offset (0.00-1.00)
        tau: Time since energization in minutes
        
    Returns:
        Phase timing modulation factor
        
    Requirements:
        - Design 3.3.1: Phase Timing Modulation
    """
    sin_term = math.sin(2.0 * math.pi * phi + 0.5 * tau)
    exp_term = math.exp(-0.1 * tau)
    
    return 1.0 + 0.3 * sin_term * exp_term


def calculate_coupling_coefficient(C: float, phi: float, R: float) -> float:
    """
    Calculate enhanced coupling coefficient κ(C,φ,R).
    
    Equation: κ(C,φ,R) = 0.15 × ln(C/100) × sin(πC/450) × (1 + φ×sin(πR/56.5))
    
    This coefficient determines how effectively warp core power couples to
    the red matter core during charge accumulation. It depends on Cochrane
    field strength, phase offset, and subspace resonance.
    
    Args:
        C: Cochrane field in millicochranes (100-900)
        phi: Phase offset (0.00-1.00)
        R: Subspace resonance frequency in THz (3.00-113.00)
        
    Returns:
        Coupling coefficient for warp core contribution
        
    Requirements:
        - Design 3.3.2: Enhanced Coupling Coefficient
    """
    ln_term = math.log(C / 100.0)
    sin_c_term = math.sin(math.pi * C / 450.0)
    sin_r_term = math.sin(math.pi * R / 56.5)
    
    return 0.15 * ln_term * sin_c_term * (1.0 + phi * sin_r_term)


def calculate_dynamic_stability(phi: float, R: float, tau: float) -> float:
    """
    Calculate dynamic phase-resonance stability Λ(φ,R,τ).
    
    Equation: Λ(φ,R,τ) = 1 + 0.2×cos(2πφ + πR/113 + 0.3τ) × e^(-0.05τ)
    
    This factor represents the time-varying stability of the phase-resonance
    coupling during charge accumulation. The exponential decay indicates
    stabilization over time, while the cosine term captures oscillatory
    behavior from phase-resonance interactions.
    
    Args:
        phi: Phase offset (0.00-1.00)
        R: Subspace resonance frequency in THz (3.00-113.00)
        tau: Time since energization in minutes
        
    Returns:
        Dynamic stability factor
        
    Requirements:
        - Design 3.3.3: Dynamic Phase-Resonance Stability
    """
    cos_term = math.cos(2.0 * math.pi * phi + math.pi * R / 113.0 + 0.3 * tau)
    exp_term = math.exp(-0.05 * tau)
    
    return 1.0 + 0.2 * cos_term * exp_term


def calculate_warp_power(C: float, phi: float, tau: float) -> float:
    """
    Calculate warp core power contribution P_warp(τ).
    
    Equation: P_warp(τ) = (C/1000)^2.4 × P_warp_max × (1 - e^(-στ)) × Φ(φ,τ)
    
    This function calculates the time-dependent power output from the warp
    core during charge accumulation. Power rises exponentially with time
    constant σ and is modulated by phase timing effects.
    
    Args:
        C: Cochrane field in millicochranes (100-900)
        phi: Phase offset (0.00-1.00)
        tau: Time since energization in minutes
        
    Returns:
        Warp core power contribution in watts
        
    Requirements:
        - Design 3.3.4: Warp Core Power Contribution
        - Requires: calculate_phase_timing_modulation
    """
    from calculator.constants import P_WARP_MAX, SIGMA
    
    cochrane_factor = (C / 1000.0) ** 2.4
    rise_term = 1.0 - math.exp(-SIGMA * tau)
    phase_timing = calculate_phase_timing_modulation(phi, tau)
    
    return cochrane_factor * P_WARP_MAX * rise_term * phase_timing



def integrate_charge_density(
    charge_time: float,
    C: float,
    phi: float,
    R: float,
    P_red_base: float = 1.0e8
) -> float:
    """
    Calculate charge density integral ρ(t).
    
    Equation:
    ρ(t) = (1/P₀) ∫₀ᵗ [P_red(τ) + P_warp(τ) × κ(C,φ,R)] × e^(-τ/ξ) × Λ(φ,R,τ) dτ
    
    This function performs numerical integration using Simpson's rule to
    calculate the accumulated charge density over the specified charge time.
    The integral accounts for:
    - Red matter core base power output
    - Warp core power contribution with coupling
    - Exponential energy decay
    - Dynamic phase-resonance stability
    
    Args:
        charge_time: Charge duration in minutes
        C: Cochrane field in millicochranes (100-900)
        phi: Phase offset (0.00-1.00)
        R: Subspace resonance frequency in THz (3.00-113.00)
        P_red_base: Base red matter power output in watts (default: 1.0e8)
        
    Returns:
        Charge density factor ρ(t) (dimensionless)
        
    Requirements:
        - Design 3.3.5: Charge Density Integration
        - Requires: calculate_warp_power, calculate_coupling_coefficient,
                   calculate_dynamic_stability
    """
    from calculator.constants import P0, XI_DECAY
    
    # Calculate coupling coefficient (constant for this integration)
    kappa = calculate_coupling_coefficient(C, phi, R)
    
    # Integration function
    def integrand(tau: float) -> float:
        P_warp = calculate_warp_power(C, phi, tau)
        Lambda = calculate_dynamic_stability(phi, R, tau)
        decay = math.exp(-tau / XI_DECAY)
        
        # Ensure total power contribution is non-negative
        # (negative coupling can cause warp core to extract energy, but total should stay positive)
        total_power = P_red_base + P_warp * kappa
        total_power = max(0.0, total_power)
        
        return total_power * decay * Lambda
    
    # Simpson's rule integration with 100 steps
    n_steps = 100
    h = charge_time / n_steps
    
    integral = integrand(0) + integrand(charge_time)
    
    for i in range(1, n_steps):
        tau = i * h
        weight = 4 if i % 2 == 1 else 2
        integral += weight * integrand(tau)
    
    integral *= h / 3.0
    
    return integral / P0



# =============================================================================
# Distance Calculation Functions
# =============================================================================

def calculate_tactical_distance(
    M: float,
    rho: float,
    C: float,
    phi: float,
    R: float
) -> float:
    """
    Calculate tactical jump distance.
    
    Equation: D = α × M^β × (1 - e^(-M/γ)) × ρ(t) × η(C) × Ψ(R)
    
    This is the forward calculation that determines how far the ship can
    jump given the instantaneous Magellan field strength and all system
    parameters. The distance is affected by:
    - Field strength (power law with saturation)
    - Charge density (accumulated energy)
    - Cochrane coupling efficiency
    - Subspace resonance modulation
    
    Args:
        M: Instantaneous Magellan field output
        rho: Charge density factor from integration
        C: Cochrane field in millicochranes (100-900)
        phi: Phase offset (0.00-1.00)
        R: Subspace resonance frequency in THz (3.00-113.00)
        
    Returns:
        Distance in meters (up to ~4.5×10⁹ for 30 AU)
        
    Requirements:
        - Design 3.4: Distance Calculation
        - Requires: calculate_cochrane_efficiency, calculate_resonance_modulation
    """
    from calculator.constants import ALPHA, BETA, GAMMA
    
    power_term = M ** BETA
    saturation_term = 1.0 - math.exp(-M / GAMMA)
    eta = calculate_cochrane_efficiency(C, phi, R)
    psi = calculate_resonance_modulation(R)
    
    distance = ALPHA * power_term * saturation_term * rho * eta * psi
    
    return distance


def calculate_required_field_tactical(
    target_distance: float,
    rho: float,
    C: float,
    phi: float,
    R: float
) -> float:
    """
    Calculate required Magellan field for target distance using Newton-Raphson.
    
    This function inverts the tactical distance equation to find the field
    strength M that produces the desired jump distance D. Uses numerical
    iteration since the equation cannot be solved analytically.
    
    Newton-Raphson iteration:
    1. Start with initial guess (500 Magellans for tactical range)
    2. Calculate distance at current M
    3. Calculate numerical derivative
    4. Update: M_new = M - (calculated_distance - target_distance) / derivative
    5. Repeat until convergence (< 1 meter error)
    
    Args:
        target_distance: Desired distance in meters
        rho: Charge density factor from integration
        C: Cochrane field in millicochranes (100-900)
        phi: Phase offset (0.00-1.00)
        R: Subspace resonance frequency in THz (3.00-113.00)
        
    Returns:
        Required Magellan field strength
        
    Raises:
        ValueError: If convergence fails or distance unachievable
        
    Requirements:
        - Design 3.5: Inverse Calculation (Required Field Strength)
        - Requires: calculate_tactical_distance
    """
    from calculator.constants import NR_MAX_ITERATIONS
    
    # Check for impossible cases
    if target_distance <= 0:
        raise ValueError("Target distance must be positive")
    
    if rho <= 0:
        raise ValueError("Cannot achieve any distance with zero or negative charge density")
    
    # Calculate modulation factors to check if distance is achievable
    psi = calculate_resonance_modulation(R)
    if abs(psi) < 1e-10:
        raise ValueError(f"Target distance unachievable: resonance at null zone (R={R:.2f} THz)")
    
    # Adaptive initial guess based on target distance
    # Use a rough estimate: smaller distances need smaller fields
    if target_distance < 1e5:
        M = 5.0  # Very small distance
    elif target_distance < 1e6:
        M = 20.0  # Small distance
    elif target_distance < 1e7:
        M = 100.0  # Medium-small distance
    elif target_distance < 1e8:
        M = 300.0  # Medium distance
    else:
        M = 600.0  # Large distance
    
    tolerance_meters = 1.0  # 1 meter tolerance
    
    # Track previous M values to detect oscillation
    prev_M = None
    oscillation_count = 0
    
    for iteration in range(NR_MAX_ITERATIONS):
        # Calculate distance at current M
        calculated_distance = calculate_tactical_distance(M, rho, C, phi, R)
        
        # Check convergence
        error = abs(calculated_distance - target_distance)
        if error < tolerance_meters:
            return M
        
        # Numerical derivative (adaptive delta based on current M)
        delta_M = max(0.01, M * 0.005)  # 0.5% of current M, minimum 0.01
        M_plus = M + delta_M
        distance_plus = calculate_tactical_distance(M_plus, rho, C, phi, R)
        derivative = (distance_plus - calculated_distance) / delta_M
        
        if abs(derivative) < 1e-10:
            raise ValueError("Solver encountered zero derivative - cannot converge")
        
        # Newton-Raphson update with damping for stability
        step = (calculated_distance - target_distance) / derivative
        
        # Apply damping if step is too large
        damping_factor = 1.0
        if abs(step) > M * 0.5:  # If step is more than 50% of current M
            damping_factor = 0.5
        
        M_new = M - damping_factor * step
        
        # Detect oscillation
        if prev_M is not None and abs(M_new - prev_M) < abs(M - prev_M) * 0.1:
            oscillation_count += 1
            if oscillation_count > 5:
                # Use bisection method to stabilize
                damping_factor *= 0.5
                M_new = M - damping_factor * step
        else:
            oscillation_count = 0
        
        prev_M = M
        
        # Clamp to reasonable range (allow very low fields for short distances)
        if M_new < 0.5:
            M_new = 0.5
        elif M_new > 10000.0:
            raise ValueError("Required field strength exceeds tactical range limits (>10,000 Magellans)")
        
        M = M_new
    
    raise ValueError(f"Solver failed to converge within {NR_MAX_ITERATIONS} iterations (last error: {error:.2f} meters)")



# =============================================================================
# Criticality Calculation Functions
# =============================================================================

def calculate_criticality_modifier(phi: float, R: float, t: float) -> float:
    """
    Calculate phase-resonance criticality modifier Χ(φ,R,t).
    
    Equation: Χ(φ,R,t) = 1 + 0.4×|sin(2πφ + πR/56.5)|×(1 - e^(-0.2t))
    
    This modifier increases criticality based on phase-resonance coupling
    and energization time. The exponential term means the effect builds
    up over time, representing accumulated quantum stress.
    
    Args:
        phi: Phase offset (0.00-1.00)
        R: Subspace resonance frequency in THz (3.00-113.00)
        t: Energization time in minutes
        
    Returns:
        Criticality modifier (1.0-1.4 range)
        
    Requirements:
        - Design 3.6.1: Phase-Resonance Criticality Modifier
    """
    sin_term = abs(math.sin(2.0 * math.pi * phi + math.pi * R / 56.5))
    exp_term = 1.0 - math.exp(-0.2 * t)
    
    return 1.0 + 0.4 * sin_term * exp_term


def calculate_red_matter_criticality(
    t: float,
    n: int,
    phi: float,
    R: float
) -> float:
    """
    Calculate red matter criticality C_red(t,n,φ,R).
    
    Equation: C_red = C₀ × e^(λt) × (1 + Σᵢ₌₁ⁿ δᵢ × e^(μᵢt)) × Χ(φ,R,t)
    
    Where:
    - δᵢ = 0.034 × i^1.3 (jump impact factor)
    - μᵢ = 0.12 × √i (jump decay rate)
    
    This function calculates the red matter core criticality component,
    which grows exponentially with time and is compounded by each tactical
    jump. The quantum scarring from jumps creates an accelerating risk curve.
    
    Args:
        t: Energization time in minutes
        n: Number of jumps performed
        phi: Phase offset (0.00-1.00)
        R: Subspace resonance frequency in THz (3.00-113.00)
        
    Returns:
        Red matter criticality component
        
    Requirements:
        - Design 3.6.2: Red Matter Criticality
        - Requires: calculate_criticality_modifier
    """
    from calculator.constants import C0, LAMBDA, DELTA_JUMP_BASE, MU_JUMP_BASE
    
    # Base exponential growth
    base_criticality = C0 * math.exp(LAMBDA * t)
    
    # Jump accumulation term
    jump_sum = 0.0
    for i in range(1, n + 1):
        delta_i = DELTA_JUMP_BASE * (i ** 1.3)
        mu_i = MU_JUMP_BASE * math.sqrt(i)
        jump_sum += delta_i * math.exp(mu_i * t)
    
    jump_factor = 1.0 + jump_sum
    
    # Phase-resonance modifier
    chi = calculate_criticality_modifier(phi, R, t)
    
    return base_criticality * jump_factor * chi


def calculate_warp_core_stress(C: float, t: float, phi: float) -> float:
    """
    Calculate warp core stress C_warp(C,t,φ).
    
    Equation: C_warp = 0.0012 × (C/100)^1.8 × e^(0.23t) × |sin(πC/200 + πφ)|
    
    This function calculates the warp core stress component of criticality,
    which depends on Cochrane field strength, energization time, and phase
    offset. Higher Cochrane fields and longer energization times increase
    stress exponentially.
    
    Args:
        C: Cochrane field in millicochranes (100-900)
        t: Energization time in minutes
        phi: Phase offset (0.00-1.00)
        
    Returns:
        Warp core stress component
        
    Requirements:
        - Design 3.6.3: Warp Core Stress
    """
    cochrane_factor = (C / 100.0) ** 1.8
    exp_term = math.exp(0.23 * t)
    sin_term = abs(math.sin(math.pi * C / 200.0 + math.pi * phi))
    
    return 0.0012 * cochrane_factor * exp_term * sin_term


def calculate_interaction_factor(M: float, phi: float, R: float) -> float:
    """
    Calculate interaction factor β_interaction(M,φ,R).
    
    Equation: β_interaction = 0.34 × M/1000 × (1 + 0.2×sin(πφ + πR/113))
    
    This factor represents how strongly the warp core stress couples to
    the red matter criticality. Higher field strengths and certain phase-
    resonance combinations increase the interaction.
    
    Args:
        M: Magellan field strength
        phi: Phase offset (0.00-1.00)
        R: Subspace resonance frequency in THz (3.00-113.00)
        
    Returns:
        Interaction factor between red matter and warp systems
        
    Requirements:
        - Design 3.6.4: Interaction Factor
    """
    field_factor = M / 1000.0
    sin_term = math.sin(math.pi * phi + math.pi * R / 113.0)
    
    return 0.34 * field_factor * (1.0 + 0.2 * sin_term)


def calculate_total_criticality(
    t: float,
    n: int,
    M: float,
    C: float,
    phi: float,
    R: float
) -> Tuple[float, float, float]:
    """
    Calculate total criticality C_total(t,n,φ,R).
    
    Equation: C_total = C_red(t,n,φ,R) + C_warp(C,t,φ) × β_interaction(M,φ,R)
    
    This is the master criticality function that combines red matter core
    criticality and warp core stress with their interaction factor. The
    total criticality determines system safety status and operational limits.
    
    Critical thresholds:
    - 0.15: Tertiary core warning
    - 0.35: Tertiary core ejection required
    - 0.75: Primary core failure imminent
    - 0.95: Catastrophic overload inevitable
    
    Args:
        t: Energization time in minutes
        n: Number of jumps performed
        M: Magellan field strength
        C: Cochrane field in millicochranes (100-900)
        phi: Phase offset (0.00-1.00)
        R: Subspace resonance frequency in THz (3.00-113.00)
        
    Returns:
        Tuple[float, float, float]: A 3-tuple containing:
            - [0] total_criticality (float): Combined criticality value (0.0-1.0+)
            - [1] red_matter_component (float): Red matter criticality contribution
            - [2] warp_core_component (float): Warp core stress contribution (with interaction)
        
    Requirements:
        - Design 3.6.5: Total Criticality
        - Requires: calculate_red_matter_criticality, calculate_warp_core_stress,
                   calculate_interaction_factor
    """
    C_red = calculate_red_matter_criticality(t, n, phi, R)
    C_warp = calculate_warp_core_stress(C, t, phi)
    beta = calculate_interaction_factor(M, phi, R)
    
    C_total = C_red + C_warp * beta
    
    return (C_total, C_red, C_warp * beta)



# =============================================================================
# Coordinate Accuracy (Flexure Matrix) Functions
# =============================================================================

def calculate_flexure_matrix(
    M: float,
    rho: float,
    phi: float,
    R: float
) -> List[List[float]]:
    """
    Calculate enhanced flexure transformation matrix 𝐅(M,φ,R).
    
    Matrix elements:
    - f₁₁ = 0.97 + 0.03×sin(M/1000 + πφ + πR/113)
    - f₁₂ = f₂₁ = 0.012×ρ(t)×(1 + 0.1×sin(πR/56.5))
    - f₃₃ = 0.94 + 0.06×cos(ρ(t)×π/2 + 2πφ)
    - f₂₂ = 0.95 + 0.05×sin(πφ + πR/56.5)
    - f₁₃ = f₃₁ = 0.008×sin(πR/113)
    - f₂₃ = f₃₂ = 0.006×cos(M/500 + πφ)
    
    The flexure matrix represents spatial distortion effects during tactical
    jumps. Diagonal elements near 1.0 indicate minimal distortion, while
    off-diagonal elements represent coupling between spatial dimensions.
    
    Args:
        M: Magellan field strength
        rho: Charge density factor
        phi: Phase offset (0.00-1.00)
        R: Subspace resonance frequency in THz (3.00-113.00)
        
    Returns:
        List[List[float]]: 3x3 transformation matrix as nested lists:
            - matrix[0]: First row [f₁₁, f₁₂, f₁₃]
            - matrix[1]: Second row [f₂₁, f₂₂, f₂₃]
            - matrix[2]: Third row [f₃₁, f₃₂, f₃₃]
        Matrix is symmetric: f₁₂=f₂₁, f₁₃=f₃₁, f₂₃=f₃₂
        
    Requirements:
        - Design 3.7: Coordinate Accuracy (Flexure Matrix)
    """
    # Calculate matrix elements
    f11 = 0.97 + 0.03 * math.sin(M/1000.0 + math.pi*phi + math.pi*R/113.0)
    f12 = 0.012 * rho * (1.0 + 0.1 * math.sin(math.pi * R / 56.5))
    f13 = 0.008 * math.sin(math.pi * R / 113.0)
    
    f21 = f12  # Symmetric
    f22 = 0.95 + 0.05 * math.sin(math.pi * phi + math.pi * R / 56.5)
    f23 = 0.006 * math.cos(M / 500.0 + math.pi * phi)
    
    f31 = f13  # Symmetric
    f32 = f23  # Symmetric
    f33 = 0.94 + 0.06 * math.cos(rho * math.pi / 2.0 + 2.0 * math.pi * phi)
    
    return [
        [f11, f12, f13],
        [f21, f22, f23],
        [f31, f32, f33]
    ]


def apply_flexure_transformation(
    matrix: List[List[float]],
    target_coords: Tuple[float, float, float]
) -> Tuple[float, float, float]:
    """
    Apply flexure matrix transformation to target coordinates.
    
    [Δx, Δy, Δz]ᵀ = 𝐅 × [x_target, y_target, z_target]ᵀ
    
    This function performs matrix-vector multiplication to transform target
    coordinates through the flexure matrix, yielding the actual arrival
    coordinates accounting for spatial distortion effects.
    
    Args:
        matrix: 3x3 flexure transformation matrix
        target_coords: Target coordinates (x, y, z) in meters
        
    Returns:
        Tuple[float, float, float]: Transformed coordinates as a 3-tuple:
            - [0] delta_x (float): Transformed x-coordinate in meters
            - [1] delta_y (float): Transformed y-coordinate in meters
            - [2] delta_z (float): Transformed z-coordinate in meters
        
    Requirements:
        - Design 3.7: Coordinate Accuracy (Flexure Matrix)
    """
    x, y, z = target_coords
    
    delta_x = matrix[0][0] * x + matrix[0][1] * y + matrix[0][2] * z
    delta_y = matrix[1][0] * x + matrix[1][1] * y + matrix[1][2] * z
    delta_z = matrix[2][0] * x + matrix[2][1] * y + matrix[2][2] * z
    
    return (delta_x, delta_y, delta_z)



# =============================================================================
# Safety and Validation Functions
# =============================================================================

def validate_tactical_parameters(
    charge_time: Optional[float],
    C: float,
    phi: float,
    R: float,
    distance: Optional[float] = None
) -> Tuple[bool, List[str]]:
    """
    Validate all tactical jump parameters.
    
    Checks all parameters against operational limits and generates descriptive
    error messages for any violations. This function should be called before
    performing any tactical jump calculations.
    
    Args:
        charge_time: Charge duration in minutes (None if not applicable)
        C: Cochrane field in millicochranes (100-900)
        phi: Phase offset (0.00-1.00)
        R: Subspace resonance frequency in THz (3.00-113.00)
        distance: Target distance in meters (None if not applicable)
        
    Returns:
        Tuple[bool, List[str]]: A 2-tuple containing:
            - [0] is_valid (bool): True if all parameters are valid, False otherwise
            - [1] error_messages (List[str]): List of validation error strings (empty if valid)
        
    Requirements:
        - Design 3.8: Safety and Validation Functions
    """
    from calculator.constants import (
        MIN_COCHRANE, MAX_COCHRANE,
        MIN_PHASE_OFFSET, MAX_PHASE_OFFSET,
        MIN_RESONANCE, MAX_RESONANCE,
        MAX_CHARGE_TIME,
        MIN_DISTANCE_METERS, MAX_DISTANCE_METERS
    )
    
    errors = []
    
    if charge_time is not None:
        if charge_time <= 0:
            errors.append("Charge time must be positive")
        elif charge_time > MAX_CHARGE_TIME:
            errors.append(f"Charge time exceeds maximum safe limit ({MAX_CHARGE_TIME} minutes)")
    
    if C < MIN_COCHRANE or C > MAX_COCHRANE:
        errors.append(f"Cochrane field must be between {MIN_COCHRANE} and {MAX_COCHRANE} millicochranes")
    
    if phi < MIN_PHASE_OFFSET or phi > MAX_PHASE_OFFSET:
        errors.append(f"Phase offset must be between {MIN_PHASE_OFFSET} and {MAX_PHASE_OFFSET}")
    
    if R < MIN_RESONANCE or R > MAX_RESONANCE:
        errors.append(f"Subspace resonance must be between {MIN_RESONANCE} and {MAX_RESONANCE} THz")
    
    if distance is not None:
        if distance < MIN_DISTANCE_METERS:
            errors.append(f"Distance must be at least {MIN_DISTANCE_METERS} meter")
        elif distance > MAX_DISTANCE_METERS:
            errors.append(f"Distance exceeds maximum tactical range ({MAX_DISTANCE_METERS/1e9:.1f} AU)")
    
    return (len(errors) == 0, errors)


def check_resonance_danger_zones(R: float, phi: float) -> List[str]:
    """
    Check if subspace resonance is in a danger zone.
    
    Base danger zones: 14, 28, 42, 56, 70, 84, 98 THz
    Phase offset shifts zones by: (φ - 0.75) × 5 THz
    
    Danger zones represent unstable subspace frequencies where quantum
    scarring effects are amplified. Operating near these zones significantly
    increases criticality buildup and jump failure probability.
    
    Args:
        R: Subspace resonance frequency in THz (3.00-113.00)
        phi: Phase offset (0.00-1.00)
        
    Returns:
        List of active danger zone warnings (empty if safe)
        
    Requirements:
        - Design 3.8: Safety and Validation Functions
    """
    base_zones = [14, 28, 42, 56, 70, 84, 98]
    offset_shift = (phi - 0.75) * 5.0
    
    warnings = []
    danger_threshold = 3.0  # THz proximity threshold
    
    for base_zone in base_zones:
        shifted_zone = base_zone + offset_shift
        if abs(R - shifted_zone) < danger_threshold:
            warnings.append(
                f"DANGER: Resonance near unstable zone at {shifted_zone:.1f} THz "
                f"(current: {R:.2f} THz)"
            )
    
    return warnings


def find_cochrane_safe_zones(
    phi: float,
    R: float,
    min_efficiency: float = 0.5
) -> List[Tuple[float, float]]:
    """
    Identify safe Cochrane field ranges based on coupling efficiency.
    
    Scans the Cochrane range (100-900 millicochranes) to find zones where
    η(C) > min_efficiency and ζ(C) indicates stable operation. Safe zones
    are regions where warp field coupling is efficient and stable.
    
    Args:
        phi: Phase offset (0.00-1.00)
        R: Subspace resonance frequency in THz (3.00-113.00)
        min_efficiency: Minimum acceptable efficiency (default: 0.5)
        
    Returns:
        List[Tuple[float, float]]: List of safe Cochrane ranges, where each tuple contains:
            - [0] zone_start (float): Starting Cochrane value in millicochranes
            - [1] zone_end (float): Ending Cochrane value in millicochranes
        Returns empty list if no safe zones found.
        
    Requirements:
        - Design 3.8: Safety and Validation Functions
        - Requires: calculate_cochrane_efficiency, calculate_safe_tolerance
    """
    from calculator.constants import MIN_COCHRANE, MAX_COCHRANE
    
    safe_zones = []
    in_safe_zone = False
    zone_start = None
    
    # Scan in 10 millicochranes steps
    for C in range(int(MIN_COCHRANE), int(MAX_COCHRANE) + 1, 10):
        efficiency = calculate_cochrane_efficiency(C, phi, R)
        tolerance = calculate_safe_tolerance(C, phi)
        
        is_safe = efficiency > min_efficiency and tolerance > 0.6
        
        if is_safe and not in_safe_zone:
            # Entering safe zone
            zone_start = C
            in_safe_zone = True
        elif not is_safe and in_safe_zone:
            # Exiting safe zone
            zone_end = C - 10
            # Only add zone if it has positive width
            if zone_end > zone_start:
                safe_zones.append((zone_start, zone_end))
            in_safe_zone = False
    
    # Close final zone if still in one
    if in_safe_zone:
        safe_zones.append((zone_start, MAX_COCHRANE))
    
    return safe_zones


def classify_criticality_level(C_total: float) -> Tuple[str, str]:
    """
    Classify criticality level and provide status message.
    
    Maps total criticality value to operational status levels with
    corresponding human-readable messages for tactical decision-making.
    
    Args:
        C_total: Total criticality value (0.0-1.0+)
        
    Returns:
        Tuple[str, str]: A 2-tuple containing:
            - [0] level_name (str): Criticality level identifier
                ("NOMINAL", "WARNING", "CRITICAL", "FAILURE_IMMINENT", "CATASTROPHIC")
            - [1] status_message (str): Human-readable status description
        
    Criticality Levels:
        - NOMINAL (< 0.15): Normal operations
        - WARNING (0.15-0.35): Tertiary core warning
        - CRITICAL (0.35-0.75): Core ejection required
        - FAILURE_IMMINENT (0.75-0.95): Primary failure imminent
        - CATASTROPHIC (≥ 0.95): Overload inevitable
        
    Requirements:
        - Design 3.8: Safety and Validation Functions
    """
    from calculator.constants import (
        CRITICALITY_WARNING,
        CRITICALITY_EJECTION,
        CRITICALITY_FAILURE,
        CRITICALITY_CATASTROPHIC
    )
    
    if C_total < CRITICALITY_WARNING:
        return ("NOMINAL", "All systems operating within normal parameters")
    elif C_total < CRITICALITY_EJECTION:
        return ("WARNING", "Tertiary core criticality warning - monitor closely")
    elif C_total < CRITICALITY_FAILURE:
        return ("CRITICAL", "Tertiary core ejection required - abort sequence")
    elif C_total < CRITICALITY_CATASTROPHIC:
        return ("FAILURE_IMMINENT", "Primary core failure imminent - emergency shutdown")
    else:
        return ("CATASTROPHIC", "Catastrophic overload inevitable - evacuate immediately")


def estimate_time_to_threshold(
    current_criticality: float,
    next_threshold: float,
    t: float,
    n: int,
    phi: float,
    R: float
) -> Optional[float]:
    """
    Estimate time until next criticality threshold.
    
    Uses exponential growth rate to project when the next threshold will
    be reached. This provides tactical officers with time estimates for
    planning jump sequences and de-energization timing.
    
    Args:
        current_criticality: Current C_total value
        next_threshold: Next threshold value to reach
        t: Current energization time in minutes
        n: Current jump count
        phi: Phase offset (0.00-1.00)
        R: Subspace resonance frequency in THz (3.00-113.00)
        
    Returns:
        Optional[float]: Estimated minutes until threshold is reached, or None if:
            - Current criticality already exceeds threshold
            - Current criticality is zero or negative
            - Threshold will not be reached based on current growth rate
        
    Requirements:
        - Design 3.8: Safety and Validation Functions
    """
    from calculator.constants import LAMBDA
    
    if current_criticality >= next_threshold:
        return 0.0
    
    # Simplified exponential projection
    # C(t) ≈ C_current × e^(λ × Δt)
    # Solve for Δt when C(t) = threshold
    
    if current_criticality <= 0:
        return None
    
    ratio = next_threshold / current_criticality
    if ratio <= 1.0:
        return None
    
    delta_t = math.log(ratio) / LAMBDA
    
    return delta_t
