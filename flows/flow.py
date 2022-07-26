from prefect import Flow
from prefect.storage import Docker

from custom_module import task_a, task_b

storage = Docker(
    registry_url='727888219528.dkr.ecr.us-east-2.amazonaws.com',
    dockerfile='Dockerfile'
)

with Flow('sandbox', storage=storage) as flow:
    result = task_a()
    task_b(upstream_tasks=[result])