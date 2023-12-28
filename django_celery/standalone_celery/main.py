from celery import Celery

app = Celery('worker',
             broker='redis://redis:6379/0',
             backend='redis://redis:6379/0',
             include=['worker.tasks'])

# app = Celery('worker',
#              include=['worker.tasks'])

# app.config_from_object('celeryconfig')

if __name__ == '__main__':
    app.start()
