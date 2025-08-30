import platform
import sys


def test_print_python_version():
    # Print detailed Python version info; always passes
    print(f"sys.version: {sys.version}")
    print(f"platform.python_version(): {platform.python_version()}")
    print(f"executable: {sys.executable}")
    assert True

