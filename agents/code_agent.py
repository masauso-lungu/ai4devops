def code_agent(state):
    print(f"[Code Agent] Generating code for task: {state.issue_summary}")
    state.generated_code = "print('Hello World')"
    state.commit_hash = "mocked123"
    return state
