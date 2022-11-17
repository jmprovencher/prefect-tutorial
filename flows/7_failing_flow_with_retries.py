from prefect import flow, task

# this tasks runs 3 times before the flow fails
@task(retries=2, retry_delay_seconds=5)
def failure():
    print('running')
    raise ValueError("bad code")

@flow
def test_retries():
    return failure()

test_retries()