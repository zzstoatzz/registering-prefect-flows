from custom_module import task_a, task_b
from prefect import Flow, task
from prefect.storage import Docker

import httpx

storage = Docker(
    registry_url='330830921905.dkr.ecr.us-east-1.amazonaws.com',
    dockerfile='Dockerfile'
)

@task
def get_cat_fact():
    data = httpx.get('https://catfact.ninja/fact').json()
    print(data)

with Flow('sandbox', storage=storage) as flow:
    
    result = task_a()
    task_b(upstream_tasks=[result])
    
    get_cat_fact()
    
    

#super random thing

if __name__ == "__main__":
    flow.run(run_on_schedule=False)