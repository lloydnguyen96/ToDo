from app import datastore_client as client
from google.cloud import datastore


def fetch_todo():
    # create query object with kind 'Task'
    query = client.query(kind="Task")
    # get all records with this type of kind
    tasks = list(query.fetch())
    return tasks


def update_task_entry(task_id, text):
    # get key of an Datastore entity with kind 'Task' and identifier 'task_id'
    key = client.key('Task', task_id)
    # obtain the entity called 'task' by using the retrieved key.
    task = client.get(key)
    # update entity properties
    task['task'] = text
    # flush these changes to Datastore database
    client.put(task)


def update_status_entry(task_id, text):
    key = client.key('Task', task_id)
    task = client.get(key)
    task['status'] = text
    client.put(task)


def insert_new_task(text):
    task = datastore.Entity(key=client.key('Task'))
    task.update(
        {
            'task': text,
            'status': 'Todo'
        }
    )
    client.put(task)


def remove_task_by_id(task_id):
    """ remove entries based on task ID """
    key = client.key('Task', task_id)
    client.delete(key)
