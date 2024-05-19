from github import Github
import os

# Replace with your GitHub personal access token
TOKEN = os.getenv('WORKFLOW_SECRET')

# Replace with the repository owner and name
REPO_OWNER = 'jge162'
REPO_NAME = 'create-release'

# Replace with the workflow ID
WORKFLOW_ID = 'create-release.yml'

# Replace with the name of the action you want to check
ACTION_NAME = 'jge162/create-release@main'

g = Github(TOKEN)
repo = g.get_repo(f'{REPO_OWNER}/{REPO_NAME}')

workflow_runs = repo.get_workflow_runs()

# Check the most recent workflow run with the given ID and name
for workflow_run in workflow_runs:
    if workflow_run.id == WORKFLOW_ID and workflow_run.name == ACTION_NAME:
        # Check if the workflow run has completed and was successful
        if workflow_run.status == 'completed' and workflow_run.conclusion == 'success':
            print('Workflow run succeeded')
        else:
            print('Workflow run failed')
        break


print(f'Status: {workflow_run.status}')
print(f'Conclusion: {workflow_run.conclusion}')
print(f'Created at: {workflow_run.created_at}')
print(f'Updated at: {workflow_run.updated_at}')

"""
OUTPUT, confirms action is running fine
Run echo "Run, Build Application using scripts"
Run, Build Application using scripts
Status: completed
Conclusion: success
Created at: 2023-02-13 10:42:53
Updated at: 2023-02-13 10:43:06
"""
