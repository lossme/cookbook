import time

from flask import url_for
from flask_restful import Resource


from . import celery


@celery.task(bind=True)
def hello(self, name):
    if name == "error":
        raise Exception('name=error, 运行出错了')

    total = 10
    for i in range(total):
        time.sleep(1)
        self.update_state(state='STARTED',
                          meta={'current': i, 'total': total}
                          )
    return "hello: {}".format(name)


class Hello(Resource):

    def get(self, name):
        task = hello.apply_async(kwargs={'name': name})
        return {
            "status": url_for('hello_status', task_id=task.id)
        }


class HelloTaskStatus(Resource):

    def get(self, task_id):
        """
The tasks current state.

Possible values includes:

    *PENDING*

        The task is waiting for execution.

    *STARTED*

        The task has been started.

    *RETRY*

        The task is to be retried, possibly because of failure.

    *FAILURE*

        The task raised an exception, or has exceeded the retry limit.
        The :attr:`result` attribute then contains the
        exception raised by the task.

    *SUCCESS*

        The task executed successfully.  The :attr:`result` attribute
        then contains the tasks return value.
    """

        task = hello.AsyncResult(task_id)
        if task.state == 'PENDING':
            return {
                'status': task.state
            }
        elif task.state == 'STARTED':
            return {
                'status': task.state,
                'current': task.info.get('current'),
                'total': task.info.get('total')
            }
        elif task.state == 'SUCCESS':
            return {
                'status': task.state,
                'result': task.result
            }
        elif task.state == "FAILURE":
            e = task.result
            return {
                'status': task.state,
                'error': str(e),
                'traceback': task.traceback
            }
