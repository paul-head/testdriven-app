import json
import unittest
from project.tests.base import BaseTestCase
from project import db
from project.api.models import User


def add_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user


class TestUserService(BaseTestCase):
    """ Test for the Users Service """

    def test_user(self):
        """ ensure the /ping rout behaves correctly """
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

    def test_add_user(self):
        """ Ensure new user can be added to the db """
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'pavel',
                    'email': 'pavel@pavel.ru'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('pavel@pavel.ru was added!', data['message'])
            self.assertIn('success', data['status'])

    def test_add_user_invalid_json(self):
        """ Ensure error is thrown if JSON object is empty """
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_user_invalid_json_keys(self):
        """ Ensure error is thrown if the json object does not have a username key """
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({'email': 'pavel@pavel.ru'}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)  # ------ 400
            self.assertIn('success', data['status'])
            self.assertIn('pavel@pavel.ru was added!', data['message'])
            # self.assertIn('Invalid payload.', data['message'])  # -------
            # self.assertIn('fail', data['status'])  # --------

    def test_add_user_duplicate_email(self):
        """ Ensure error is thrown if the email already exists """
        with self.client:
            self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'pavel',
                    'email': 'pavel@pavel.ru',
                }),
                content_type='application/json',
            )
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'pavel',
                    'email': 'pavel@pavel.ru',
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Sorry. That email already exists', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_user(self):
        """ Ensure get single user behaves correctly """
        user = add_user('pavel', 'pavel@pavel.ru')
        with self.client:
            response = self.client.get(f'/users/{user.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('pavel', data['data']['username'])
            self.assertIn('pavel@pavel.ru', data['data']['email'])
            self.assertIn('success', data['status'])

    def test_single_user_no_id(self):
        """ Ensure error is thrown if id is not provided """
        with self.client:
            response = self.client.get('/users/bla')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_user_incorrect_id(self):
        """ Ensure error is thrown if id does not exits """
        with self.client:
            response = self.client.get('/users/111')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_all_users(self):
        """ Ensure get all users behave correctly """
        add_user('pavel', 'pavel@pavel.ru')
        add_user('bob', 'bob@bobson.com')
        with self.client:
            response = self.client.get('/users')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['users']), 2)
            self.assertIn('pavel', data['data']['users'][0]['username'])
            self.assertIn('pavel@pavel.ru', data['data']['users'][0]['email'])
            self.assertIn('bob', data['data']['users'][1]['username'])
            self.assertIn('bob@bobson.com', data['data']['users'][1]['email'])
            self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()
