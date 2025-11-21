Jenkins job config for GitHub repository
======================================

This folder contains a Pipeline job config XML and usage instructions to create a Jenkins job that checks out the repository and runs the repository's `Jenkinsfile` located at `jenkins/Jenkinsfile`.

Files
-----
- `github_pipeline_job_config.xml` — Pipeline job config (use to create/import a Jenkins job). Replace placeholders before creating the job.

Quick checklist (what to replace)
--------------------------------
- In `github_pipeline_job_config.xml` replace:
  - `<url>` with your repo URL (e.g. `https://github.com/OWNER/REPO.git`).
  - `<credentialsId>` with the Jenkins credentials ID you will create (or remove the element for public repos).
  - Branch spec if you don't use `main` (default: `*/main`).

Prerequisites
-------------
- Running Jenkins with the following plugins installed (minimum):
  - Git plugin
  - Pipeline (workflow) plugins
  - GitHub plugin (for webhook trigger)
- An account on Jenkins with API access (username and API token) to create jobs.

Create Jenkins credentials (recommended)
--------------------------------------
1. Manage Jenkins → Manage Credentials → (choose domain) → Add Credentials.
2. Preferred:
   - Kind: "Username with password" — username = GitHub username, password = personal access token (PAT) with repo access.
   - OR: Kind: "Secret text" — use PAT and adjust how you reference it in your pipeline if needed.
3. Give the credential an ID (example: `github-pat-ci`) and use that value for `<credentialsId>` in the XML.

Create the job via Jenkins UI
----------------------------
1. Jenkins → New Item → type job name → select "Pipeline" → OK.
2. Either paste a pipeline script or choose to configure the job to use SCM; instead of building in the UI you can import `github_pipeline_job_config.xml` or use the REST API described below.

Create the job via Jenkins REST API (example)
-------------------------------------------
The simplest scripted approach is: (1) get a crumb, (2) POST the config XML to create the job.

1) Get Jenkins crumb (if CSRF protection enabled). Replace `USER` and `API_TOKEN` below:

```
# replace USER and API_TOKEN
curl -u 'USER:API_TOKEN' 'http://172.17.80.1:8080/crumbIssuer/api/json'
```

Response example:
```
{"crumbRequestField":"Jenkins-Crumb","crumb":"abcd-efgh-1234"}
```

2) Create the job (example uses job name `ai4devops-pipeline` — replace if you want a different name). Include crumb header if required:

```
# from repo root; creates job named ai4devops-pipeline
# without crumb (CSRF disabled):
curl -u 'USER:API_TOKEN' -H 'Content-Type: application/xml' --data-binary @jenkins/github_pipeline_job_config.xml 'http://172.17.80.1:8080/createItem?name=ai4devops-pipeline'

# with crumb (CSRF enabled):
curl -u 'USER:API_TOKEN' -H 'Jenkins-Crumb: CRUMB_VALUE' -H 'Content-Type: application/xml' --data-binary @jenkins/github_pipeline_job_config.xml 'http://172.17.80.1:8080/createItem?name=ai4devops-pipeline'
```

Notes:
- Use the absolute path to the XML file from the machine you run the curl command on. The `@jenkins/github_pipeline_job_config.xml` path above assumes you run the command from the repository root.
- The `JOB_NAME` must be URL-safe.

Set up GitHub webhook
----------------------
1. In your GitHub repo → Settings → Webhooks → Add webhook.
2. Payload URL: `http://172.17.80.1:8080/github-webhook/`.
3. Content type: `application/json`.
4. Select events: `Push` (or choose individual events as needed).
5. Save.

Verifying and first run
-----------------------
- After creating the job and adding the webhook, push to the branch used in the job spec (default `main`).
- Verify that Jenkins receives the webhook (Jenkins -> Manage Jenkins -> System Log or job Build History).

Security note — token found and rotated
--------------------------------------
During editing, a token-like string was found in the committed XML and removed. If you previously committed an actual token or password, rotate it immediately in GitHub and in any other service where it might have been used.

Alternatives and next steps I can take for you
----------------------------------------------
- Generate a Multibranch Pipeline config (recommended if you want builds for many branches).
- Generate a Job DSL or a small script to automate creating multiple jobs.
- Replace placeholders in the XML with concrete values you provide (repo URL, `credentialsId`, branch, job name). I will not accept secrets; if you want me to produce the exact curl command you can paste non-secret placeholders and I will format the command for you to run locally.

If you'd like, I can now:
- Add the multibranch job XML instead, or
- Produce the exact curl examples filled with your repo URL and job name (you run them locally), or
- Walk you step-by-step (I can show the exact sequence of UI clicks or commands).

Pick one and I'll do it next.
