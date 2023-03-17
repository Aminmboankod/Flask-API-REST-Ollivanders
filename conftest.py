import pytest

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "connectionDB: mark test as requiring database connection"
    )
