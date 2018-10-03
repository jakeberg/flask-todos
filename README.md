## Flask Todo-App

### How to use this app:


1. Start virtual environment:

```python
pipenv shell
```

2. Run flask app:
```python
FLASK_APP=app.py flask run
```

3. Run your REST client(like Postman):

4. You can run these commands at the endpoints provided.

* Get all todos(GET):

http://127.0.0.1:5000/todos


Get one todo(GET):

http://127.0.0.1:5000/todo/2

* Post todo(POST):

http://127.0.0.1:5000/todos

(send json in header)

```

{
	"title": "new todo",
    "due_date": "2/7/2019",
    "completed": false
}

```

* Delete todo (DELETE):

http://127.0.0.1:5000/todo/2

* Update todo(UPDATE):

http://127.0.0.1:5000/todo/2

(send json in header)

```

{
	"title": "update",
    "due_date": "2/8/2019",
    "completed": true
}

```
