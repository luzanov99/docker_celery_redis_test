from ticket.celery import app


@app.task
def task12():
    print(1)