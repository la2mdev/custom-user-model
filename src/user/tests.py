from django.test import TestCase
from django.contrib.auth import get_user_model


class UserAccountTest(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        superuser =db.objects.create_superuser(
            'testuser@super.com', 'username', 'firstname', 'password'
        )

        self.assertEqual(superuser.email, 'testuser@super.com')
        self.assertEqual(superuser.username, 'username')
        self.assertEqual(superuser.first_name, 'firstname')
        self.assertEqual(str(superuser), superuser.username)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com', username='username', first_name='firstname',
                password='password', is_superuser=False
            )
        
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com', username='username', first_name='firstname',
                password='password', is_staff=False
            )
        
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='', username='username', first_name='firstname',
                password='password'
            )

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user('testuser@user.com', 'username', 'firstname', 'password')
        self.assertEqual(user.email, 'testuser@user.com')
        self.assertEqual(user.firstname, 'username')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)

        with self.assertRaises(ValueError):
            db.objects.create_user(
                email='', username='username', first_name='first_name', password='password'
            )
