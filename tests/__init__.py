"""
Implementation of a Pokemon-like game for fun and training purposes.
"""
__version__ = "0.0.0"

import pytest

from game.config import ROOT_DIR


def test(*args, **kwargs):
    """Run basic tests of the package."""
    pytest.main([str(ROOT_DIR), *args], **kwargs)
