"""
Run All Examples

This script runs all tactical jump examples in sequence, providing a comprehensive
demonstration of the short-range tactical jump system capabilities.
"""

import sys
import importlib.util


def run_example(example_file, example_name):
    """Run a single example file."""
    print("\n" + "=" * 80)
    print(f"RUNNING: {example_name}")
    print("=" * 80 + "\n")
    
    try:
        # Import and run the example
        spec = importlib.util.spec_from_file_location("example", example_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Find and call the main example function
        for attr_name in dir(module):
            if attr_name.endswith('_example') and callable(getattr(module, attr_name)):
                example_func = getattr(module, attr_name)
                example_func()
                break
        
        print("\n✓ Example completed successfully\n")
        return True
        
    except Exception as e:
        print(f"\n✗ Example failed with error: {e}\n")
        return False


def main():
    """Run all examples in sequence."""
    examples = [
        ("examples/01_basic_tactical_jump.py", "Example 1: Basic Tactical Jump"),
        ("examples/02_sequential_jump_planning.py", "Example 2: Sequential Jump Planning"),
        ("examples/03_criticality_monitoring.py", "Example 3: Criticality Monitoring"),
        ("examples/04_parameter_optimization.py", "Example 4: Parameter Optimization"),
        ("examples/05_emergency_operations.py", "Example 5: Emergency Operations"),
    ]
    
    print("=" * 80)
    print("USS BLACKWELL TACTICAL JUMP SYSTEM - EXAMPLE SUITE")
    print("=" * 80)
    print()
    print(f"Running {len(examples)} examples...")
    print()
    
    results = []
    for example_file, example_name in examples:
        success = run_example(example_file, example_name)
        results.append((example_name, success))
        
        # Pause between examples for readability
        if example_file != examples[-1][0]:
            input("\nPress Enter to continue to next example...")
    
    # Summary
    print("\n" + "=" * 80)
    print("EXAMPLE SUITE SUMMARY")
    print("=" * 80)
    print()
    
    for name, success in results:
        status = "✓ PASSED" if success else "✗ FAILED"
        print(f"{status}: {name}")
    
    print()
    passed = sum(1 for _, success in results if success)
    total = len(results)
    print(f"Results: {passed}/{total} examples passed")
    print("=" * 80)
    
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
