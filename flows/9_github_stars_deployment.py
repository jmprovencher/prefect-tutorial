from prefect import flow, task, get_run_logger
import httpx

@task(retries=3)
def get_stars(repo):
    url = f"https://api.github.com/repos/{repo}"
    count = httpx.get(url).json()["stargazers_count"]
    logger = get_run_logger()
    logger.info(f"{repo} has {count} stars!")

@flow
def github_stars(repos):
    for repo in repos:
        get_stars(repo)
