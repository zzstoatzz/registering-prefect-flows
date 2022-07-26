from prefect import task

@task(log_stdout=True)
def task_a():
    print('hi i am the first task')

@task(log_stdout=True)
def task_b():
    print('hi i am the second task')