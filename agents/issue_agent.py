from tools.jira_tools import get_ticket, add_comment

def issue_agent(state):
    ticket_id = state.jira_ticket

    print(f"[Issue Agent] Fetching JIRA ticket: {ticket_id}")

    data = get_ticket(ticket_id)

    summary = data["fields"]["summary"]
    description = data["fields"].get("description", "")

    state.issue_summary = summary

    print(f"[Issue Agent] Summary: {summary}")
    print(f"[Issue Agent] Description: {description}")

    # Add comment to JIRA to show AI is working on it
    add_comment(ticket_id, "AI Agent started analyzing this ticket.")

    return state
