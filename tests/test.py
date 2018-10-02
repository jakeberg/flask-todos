import unittest
import TodoListResource from app


class TestTodoCRUD(unittest.TestCase):

    def test_list_get(self):
        result = TodoListResource.get()
        self.assertEqual(result, "Try these commands: sup? / nasa")

if __name__ == '__main__':
    unittest.main()
