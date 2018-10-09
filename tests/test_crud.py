import unittest
import app
from datetime import datetime, timedelta, date
from todos import todos

class TestTodoListCRUD(unittest.TestCase):

    def test_todo_list_get(self):
        result = app.todo_list_get()
        self.assertEqual(result, todos)

    # def test_todo_list_post(self):
    #     newTodo = {
    #     	"title": "new todo",
    #         "due_date": "2/7/2019",
    #         "completed": False
    #     }
    #     result = app.todo_list_post(newTodo)
    #     print("asdfasdfasd", result)


class TestTodoCRUD(unittest.TestCase):

    def test_todo_get(self):
        todo = {
            "title":"do somethin",
            "creation_date": "2018-10-02 15:07:08.183240",
            "last_updated_date": "2018-10-02 15:07:08.183240",
            "due_date": "12-2-2018",
            "completed": False,
            "completion_date": "incomplete"
        }
        result = app.todo_get(1)
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

        result = app.todo_put(1, put_todo)
        self.assertEqual(result["title"], updated_todo["title"])
        self.assertEqual(result["due_date"], updated_todo["due_date"])
        self.assertEqual(result["completed"], updated_todo["completed"])

        if result["completion_date"] != "incomplete":
            pass

        result_seconds = result["last_updated_date"][17:19]
        if int(NOW) <= int(result_seconds) <= int(AFTER):
            pass

    def test_todo_delete(self):
        result = app.todo_delete(2)
        self.assertEqual(app.todo_get(2), "Item not in list")
        
        # Adds todo back into list for other tests
        repair_todo = {
            "title": "todo number 2",
            "due_date": "1-2-2019",
            "completed": False,
            }
        app.todo_put(2, repair_todo)


if __name__ == '__main__':
    unittest.main()
