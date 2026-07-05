"""Test configuration for Storage Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "storage-agent", "category": "Cloud Engineering"}
