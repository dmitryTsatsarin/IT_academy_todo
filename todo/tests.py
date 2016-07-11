from django.test import TestCase
from todo.models import Tasks


class ToDoTest(TestCase):

    def test_ok_add_task(self):
        data = {'task': 'test_task', 'status': False, 'order': 1}
        self.client.post('/add_task/', data)
        q_data = Tasks.objects.filter()
        self.assertEquals(q_data.count(), 1)
        task = q_data.get()
        self.assertEquals(task.task, data['task'])
        self.assertEquals(task.status, data['status'])
        self.assertEquals(task.order, data['order'])

    def test_ok_del_task(self):
        data_post = {'task': 'test_task', 'status': False, 'order': 1}
        self.client.post('/add_task/', data_post)
        data_get = {'order': 1}
        self.client.get('/delete/', data_get)
        q_data = Tasks.objects.filter()
        self.assertEquals(q_data.count(), 0)

    # def test_ok_edit_task(self):
    #     data = {'task': 'test_task1', 'status': False, 'order': 1},
    #     self.client.post('/add_task/', data)
    #     data_post = {'status': 'on', 'task': 'changed_test_task'}
    #     self.client.post('/edit/', data_post)
    #     q_data =
    #
    #     q_data.task = 'changed_test_task'
    #     q_data.status = True
    #     q_data.order = 2
    #     q_data.save()
    #     q_data_changed = Tasks.objects.filter().last()
    #     self.assertEquals(q_data_changed.task, 'changed_test_task')
    #     self.assertEquals(q_data_changed.status, True)
    #     self.assertEquals(q_data_changed.order, 2)
