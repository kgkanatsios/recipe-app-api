from django.test import TestCase
from django.contrib.auth import get_user_model

# docker-compose run app sh -c "python manage.py test"
# docker-compose run app sh -c "python manage.py test && flake8"


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = "test@email.com"
        password = "pass123word456"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized(self):
        email = 'test@Email.COM'
        password = "pass123word456"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='password'
            )

    def test_create_new_superuser(self):
        email = "test@email.com"
        password = "pass123word456"
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
