from celery import Celery

app = Celery('worker',
             broker='redis://redis:6379/0',
             backend='redis://redis:6379/0',
             include=['worker.tasks'])

# app = Celery('worker',
#              include=['worker.tasks'])

# app.config_from_object('celeryconfig')

app.conf.task_routes = {
    'worker.tasks.add': {
        'queue': 'queue2'
    },
    'worker.tasks.mul': {
        'queue': 'queue2'
    },
    'worker.tasks.xsum': {
        'queue': 'queue2'
    }
}

if __name__ == '__main__':
    app.start()
