from prefect import flow, task
import httpx

@task(retries=3)
def get_stars(repo):
    url = f"https://api.github.com/repos/{repo}"
    count = httpx.get(url).json()["stargazers_count"]
    print(f"{repo} has {count} stars!")

@flow
def github_stars(repos):
    for repo in repos:
        get_stars(repo)

# call the flow!
github_stars(["coveo/ui-kit", "coveo/platform-client",  "coveo/plasma"])