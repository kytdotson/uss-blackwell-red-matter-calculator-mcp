"""
Physical constants and configuration parameters for the USS Blackwell Red Matter Core.

This module defines all mathematical constants, efficiency zone boundaries,
safety thresholds, and Newton-Raphson solver parameters used in dimensional
fold calculations.
"""

# Physical constants
M0: float = 200.0       # Safety threshold (Magellans) - minimum field strength
MX: float = 1847.0      # Critical resonance point (Magellans)
K: float = 12.7         # Dimensional constant

# Efficiency zone boundaries
EFFICIENCY_STANDARD_MAX: float = 1_000.0    # Upper bound for standard efficiency zone
EFFICIENCY_OPTIMAL_MAX: float = 10_000.0    # Upper bound for optimal efficiency zone

# Efficiency factor values
XI_STANDARD: float = 1.0    # Efficiency factor for standard zone (M < 1,000)
XI_OPTIMAL: float = 1.2     # Efficiency factor for optimal zone (1,000 <= M < 10,000)
XI_DIMINISHING: float = 0.8 # Efficiency factor for diminishing zone (M >= 10,000)

# Safety boundaries
MAX_SAFE_MAGELLANS: float = 2_000_000.0      # Maximum safe field strength
MAX_ABSOLUTE_MAGELLANS: float = 3_000_000.0  # Catastrophic limit

# Newton-Raphson solver settings
NR_INITIAL_GUESS: float = 1_000.0    # Initial field strength guess for inverse calculation
NR_TOLERANCE: float = 0.01           # Convergence tolerance in light-years
NR_MAX_ITERATIONS: int = 100         # Maximum solver iterations
NR_DELTA_M: float = 1.0              # Delta for numerical derivative approximation
NR_MAX_M: float = MAX_ABSOLUTE_MAGELLANS * 2.0  # Maximum field strength during iteration


# =============================================================================
# Tactical Jump System Constants
# =============================================================================

# Tactical jump distance equation constants
ALPHA: float = 2.847e6              # Range scaling constant
BETA: float = 0.73                  # Power efficiency factor
GAMMA: float = 450.0                # Field saturation threshold (Magellans)

# Power integration constants
P0: float = 1.2e8                   # Base power normalization (watts)
XI_DECAY: float = 8.2               # Energy decay constant (minutes)
P_WARP_MAX: float = 8.7e8           # Maximum warp power (watts)
SIGMA: float = 1.23                 # Warp field rise time (min⁻¹)

# Cochrane coupling constants
DELTA: float = 47.3                 # Logarithmic offset
C_MAX: float = 1000.0               # Maximum Cochrane (warp 1.0 millicochranes)

# Criticality constants
C0: float = 0.0023                  # Base criticality
LAMBDA: float = 0.47                # Primary exponential (min⁻¹)
DELTA_JUMP_BASE: float = 0.034      # Jump impact factor base
MU_JUMP_BASE: float = 0.12          # Jump decay rate base

# Criticality thresholds
CRITICALITY_WARNING: float = 0.15       # Tertiary core warning
CRITICALITY_EJECTION: float = 0.35      # Tertiary core ejection required
CRITICALITY_FAILURE: float = 0.75       # Primary core failure imminent
CRITICALITY_CATASTROPHIC: float = 0.95  # Catastrophic overload inevitable

# Operational limits
MAX_CHARGE_TIME: float = 15.0       # Minutes (practical limit)
SAFE_CHARGE_TIME: float = 10.0      # Minutes (recommended maximum)
MIN_DISTANCE_METERS: float = 1.0    # Minimum tactical jump distance
MAX_DISTANCE_METERS: float = 4.5e9  # Maximum distance (30 AU)
MIN_COCHRANE: float = 100.0         # Minimum Cochrane field
MAX_COCHRANE: float = 900.0         # Maximum Cochrane field
MIN_PHASE_OFFSET: float = 0.0       # Minimum phase offset
MAX_PHASE_OFFSET: float = 1.0       # Maximum phase offset
MIN_RESONANCE: float = 3.0          # Minimum subspace resonance (THz)
MAX_RESONANCE: float = 113.0        # Maximum subspace resonance (THz)
