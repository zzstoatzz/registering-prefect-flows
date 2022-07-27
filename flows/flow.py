from prefect import Flow
from prefect.storage import Docker

from custom_module import task_a, task_b

storage = Docker(
    registry_url='330830921905.dkr.ecr.us-east-1.amazonaws.com',
    dockerfile='Dockerfile'
)

with Flow('sandbox', storage=storage) as flow:
    result = task_a()
    task_b(upstream_tasks=[result])

#super random thing

if __name__ == "__main__":
    flow.run(run_on_schedule=False)