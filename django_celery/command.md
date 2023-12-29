# Task group
```
# Group
from celery import group, signature
from worker.tasks import add, xsum

job = group(signature('worker.tasks.add', args=(i, i)) for i in range(10))
result = job.apply_async()

job = group(add.s(i, i) for i in range(10))
result = job.apply_async()
"""
<GroupResult: 10c0dfa3-489b-4a86-a101-90ac77b2e64f [e500072b-214d-48a4-adc6-f212d5859a11, 10622db4-b849-464e-a067-8e2e0f83d849, 762a60e6-d2c5-42f0-b150-a5868834e0bf, cefc7e86-6ba1-42d1-8471-a4728c9eb304, 8d0221ff-432e-4498-bcd5-7c7ce7825b02, 1e4f76bb-22fa-4a3a-ba9c-ec8b0cc205c7, 3db0dcd9-3807-45a2-80fe-cdaa1101feaf, be94d86e-2a6f-4596-b068-8f2c6b3895f7, ba61b0c9-c434-427a-8d06-8e18529b94e9, 631c3ce0-7c92-4c53-af31-ff38ea78ce0f]>
"""
result.get()
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# Chain
from celery import chain

workflow = chain(add.s(2, 2), add.s(4), add.s(8))
result = workflow.apply_async()
result.get()
# 16


# Chord
from celery import chord

callback = xsum.s()
header = [add.s(i, i) for i in range(10)]
result = chord(header)(callback)
result.get()
# 90


# Starmap
result = add.starmap(zip(range(10), range(10))).apply_async()
result.get()
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```