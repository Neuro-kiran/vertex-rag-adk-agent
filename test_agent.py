from agent import root_agent, retrieval_tool


def test_agent_uses_retrieval():
    assert retrieval_tool in root_agent.tools
