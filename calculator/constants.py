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
