from pydantic import BaseModel

class DevOpsState(BaseModel):
    jira_ticket: str | None = None
    issue_summary: str | None = None
    generated_code: str | None = None
    commit_hash: str | None = None
    deploy_status: str | None = None
