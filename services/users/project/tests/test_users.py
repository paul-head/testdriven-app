import json
import unittest
from project.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    """ Test for the Users Service """

    def test_user(self):
        """ ensure the /ping rout behaves correctly """
        responce = self.client.get('/users/ping')
        data = json.loads(responce.data.decode())
        self.assertEqual(responce.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()
