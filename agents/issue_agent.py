def issue_agent(state):
    print(f"[Issue Agent] Reading JIRA ticket {state.jira_ticket}")
    state.issue_summary = "Implement Hello World test"
    return state
