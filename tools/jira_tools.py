import os
import requests
from requests.auth import HTTPBasicAuth

JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def get_ticket(ticket_id: str):
    """Fetch JIRA issue details."""
    url = f"{JIRA_BASE_URL}/rest/api/3/issue/{ticket_id}"
    response = requests.get(url, headers=headers, auth=auth)
    response.raise_for_status()
    return response.json()


def add_comment(ticket_id: str, text: str):
    """Post a comment on the JIRA issue."""
    url = f"{JIRA_BASE_URL}/rest/api/3/issue/{ticket_id}/comment"
    payload = {"body": text}

    response = requests.post(url, headers=headers, json=payload, auth=auth)
    response.raise_for_status()
    return response.json()


def transition_ticket(ticket_id: str, transition_id: str):
    """Move issue to another workflow state."""
    url = f"{JIRA_BASE_URL}/rest/api/3/issue/{ticket_id}/transitions"
    payload = {"transition": {"id": transition_id}}

    response = requests.post(url, headers=headers, json=payload, auth=auth)
    response.raise_for_status()
    return response.json()
