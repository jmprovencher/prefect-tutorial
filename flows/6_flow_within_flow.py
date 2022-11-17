from prefect import flow

@flow
def common_flow(config: dict):
    print("I am Mansour and I love flows of flows!")
    intermediate_result = 42
    return intermediate_result

@flow
def main_flow():
    # do some things
    # then call another flow function
    data = common_flow(config={})
    data = common_flow(config={})
    data = common_flow(config={})
    # do more things

main_flow()