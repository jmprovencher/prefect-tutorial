from prefect import flow, task
from prefect.tasks import task_input_hash
from datetime import timedelta

@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(minutes=1))
def hello_task(name_input):
    # Doing some work
    print(f"Welcome {name_input}!")
    return "Welcome " + name_input

@flow
def hello_flow(name_input):
    hello_task(name_input)

hello_flow("Mario Bros")