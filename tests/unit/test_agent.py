"""Storage Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_design_architecture():
    """Test Design cloud architecture for Storage Agent."""
    tools = AgentTools()
    result = await tools.design_architecture(requirements="test", constraints="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_template():
    """Test Generate IaC template from architecture design."""
    tools = AgentTools()
    result = await tools.generate_template(architecture="test", template_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_review_architecture():
    """Test Review existing architecture against best practices."""
    tools = AgentTools()
    result = await tools.review_architecture(architecture="test", framework="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_estimate_cost():
    """Test Estimate monthly cost for proposed architecture."""
    tools = AgentTools()
    result = await tools.estimate_cost(architecture="test", region="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.storage_agent_agent import StorageAgentAgent
    agent = StorageAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
