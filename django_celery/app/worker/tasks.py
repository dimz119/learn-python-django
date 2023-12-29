import time
from celery import shared_task

@shared_task(queue='celery')
def print_result(x, y, msg=None):
    total = x + y
    if msg:
        return f"{msg}: {total}"
    return total

@shared_task(queue='celery', rate_limit='1/m')
def add(x, y):
    return x + y

@shared_task(queue='celery')
def dumb():
    return

@shared_task(queue='celery')
def xsum(numbers):
    return sum(numbers)

@shared_task(queue='celery')
def p1():
    time.sleep(5)
    return

@shared_task(queue='celery:1')
def p2():
    time.sleep(5)
    return

@shared_task(queue='celery:2')
def p3():
    time.sleep(5)
    return
