
import os
import json
import urllib.request
import urllib.error

# Token is provided securely by GitHub Actions
token = os.environ.get("GH_TOKEN")

if not token:
    raise RuntimeError("GH_TOKEN is missing")

# Repository to test
owner = "harshalvg20"
repo = "testcicd"

url = f"https://api.github.com/repos/{owner}/{repo}"

# Create an authenticated API request
request = urllib.request.Request(
    url,
    headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    },
)

try:
    with urllib.request.urlopen(request) as response:
        repository = json.loads(response.read())

    print("GitHub App authentication successful!")
    print(f"Repository: {repository['full_name']}")
    print(f"Private: {repository['private']}")
    print(f"Default branch: {repository['default_branch']}")

except urllib.error.HTTPError as error:
    print(f"GitHub API error: {error.code}")
    raise
