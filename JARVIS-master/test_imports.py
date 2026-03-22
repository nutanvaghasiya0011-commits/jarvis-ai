#!/usr/bin/env python3
"""Test script to check JARVIS imports and basic functionality."""

try:
    print("Testing basic imports... - test_imports.py:5")
    import sys
    print(f"Python version: {sys.version} - test_imports.py:7")

    print("Testing JARVIS imports... - test_imports.py:9")
    from Jarvis.config import config
    print("✓ config imported successfully - test_imports.py:11")
    print(f"Config attributes: {[attr for attr in dir(config) if not attr.startswith('_')]} - test_imports.py:12")

    print("\nAll basic imports successful! JARVIS should be ready to run. - test_imports.py:14")

except ImportError as e:
    print(f"Import error: {e} - test_imports.py:17")
except (OSError, RuntimeError) as e:
    print(f"Other error: {e} - test_imports.py:19")