import unittest
import todo_app
from datetime import datetime, timedelta, date
from todos import todos


class TestTodoListCRUD(unittest.TestCase):

    def test_todo_list_get(self):
        result = todo_app.todo_list_get()
        self.assertEqual(result, todos)

    def test_todo_list_post(self):
        newTodo = {
            "title": "new todo",
            "due_date": "2/7/2019",
            "completed": False
        }
        result = todo_app.todo_list_post(newTodo)
        self.assertEqual(result["name"], "new todo")


class TestTodoCRUD(unittest.TestCase):

    def test_todo_get(self):
        todo = {
            "title": "do somethin",
            "creation_date": "2018-10-02 15:07:08.183240",
            "last_updated_date": "2018-10-02 15:07:08.183240",
            "due_date": "12-2-2018",
            "completed": False,
            "completion_date": "incomplete"
        }
        result = todo_app.todo_get(1)
        self.assertEqual(result, todo)

    def test_todo_put(self):
        td = timedelta(seconds=2)
        time_now = datetime.now()
        time_after = time_now + td
        NOW = str(time_now.second)
        AFTER = str(time_after.second)

        put_todo = {
            "title": "update",
            "due_date": "2/8/2019",
            "completed": True
        }
        updated_todo = {
            "title": "update",
            "due_date": "2/8/2019",
            "completed": True,
        }

        result = todo_app.todo_put(1, put_todo)
        result_seconds = result["last_updated_date"][17:19]

        self.assertEqual(result["title"], updated_todo["title"])
        self.assertEqual(result["due_date"], updated_todo["due_date"])
        self.assertEqual(result["completed"], updated_todo["completed"])
        assert result["completion_date"] != "incomplete"
        assert int(NOW) <= int(result_seconds) <= int(AFTER)

    def test_todo_delete(self):
        result = todo_app.todo_delete(2)
        self.assertEqual(
            todo_app.todo_get(2),
            "Item not in list. -- todo_get()"
            )

        # Adds todo back into list for other tests
        repair_todo = {
            "title": "todo number 2",
            "due_date": "1-2-2019",
            "completed": False,
            }
        todo_app.todo_put(2, repair_todo)


if __name__ == '__main__':
    unittest.main()
