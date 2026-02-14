# Changelog

All notable changes to the USS Blackwell Red Matter Core MCP Server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Landing Offset Enhancement** for short-range tactical jumps
  - New `landing_offset` block in `short_range_jump_distance` responses
  - New `landing_offset` block in each jump result of `short_range_sequential_jumps` responses
  - Scalar magnitude calculation: `offset_meters = (accuracy_degradation_pct / 100) × distance_meters`
  - Random 3D directional components using uniform sphere distribution
  - Directional summary with intelligent component selection (top 2 components)
  - Severity classification (NEGLIGIBLE, MINOR, SIGNIFICANT, DANGEROUS, CATASTROPHIC)
  - Human-readable distance formatting with appropriate units
  - Narrative-ready summary text for fiction writing
  - Coordinate mapping: X-axis (fore/aft), Y-axis (port/starboard), Z-axis (dorsal/ventral)

### Changed
- Enhanced `short_range_jump_distance` tool to include landing offset information
- Enhanced `short_range_sequential_jumps` tool to include landing offset for each jump
- Updated API documentation to reflect new response fields

### Technical Details
- Added `calculate_landing_offset()` function in `calculator/tactical.py`
- Added helper functions for directional components, severity classification, and formatting
- Integrated landing offset calculation into both short-range tactical jump tools
- All offset calculations are independent per jump (no cumulative tracking)
- Directional variety ensures repeated jumps produce different narrative descriptions

### Backward Compatibility
- **Fully backward compatible** - new `landing_offset` field is additive only
- No existing response fields were modified or removed
- No new required parameters added to tool inputs
- Existing API consumers can safely ignore the new field

## [1.0.0] - Initial Release

### Added
- Long-range dimensional fold jump calculations
  - `long_range_jump_distance`: Calculate distance from field strength
  - `long_range_field_strength`: Calculate required field strength for target distance
  - `long_range_describe`: System documentation and reference
- Short-range tactical jump calculations
  - `short_range_jump_distance`: Calculate distance from charge time
  - `short_range_field_strength`: Calculate required field strength
  - `short_range_sequential_jumps`: Multi-jump sequence planning
  - `short_range_optimize_cochrane`: Find safe Cochrane field zones
  - `short_range_describe`: System documentation and reference
- Safety classification system for all jump types
- Criticality tracking for tactical jumps
- Flexure matrix coordinate transformations
- Comprehensive test suite with unit and property-based tests
- MCP server implementation with stdio transport
- Debug mode with inspector and documentation endpoints
