from django.test import TestCase
from .models import Todo


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='first todo', body='some task to complete')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'first todo')

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_body = f'{todo.body}'
        self.assertEquals(expected_body, 'some task to complete')

    def test_complete_status(self):
        todo = Todo.objects.get(id=1)
        expected_status = todo.completed
        self.assertEquals(expected_status, False)
