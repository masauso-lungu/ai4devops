from langgraph.graph import StateGraph, END
from state import DevOpsState
from agents.issue_agent import issue_agent
from agents.code_agent import code_agent
from agents.deploy_agent import deploy_agent

def build_graph():
    g = StateGraph(DevOpsState)

    g.add_node("issue_agent", issue_agent)
    g.add_node("code_agent", code_agent)
    g.add_node("deploy_agent", deploy_agent)

    g.set_entry_point("issue_agent")

    g.add_edge("issue_agent", "code_agent")
    g.add_edge("code_agent", "deploy_agent")
    g.add_edge("deploy_agent", END)

    return g.compile()


if __name__ == "__main__":
    app = build_graph()

    output = app.invoke(
        DevOpsState(jira_ticket="AI4D-5")
    )

    print("=== DONE ===")
    print(output)
