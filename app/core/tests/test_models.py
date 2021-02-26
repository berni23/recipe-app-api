
from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models
# helper function


def sample_user(email='test@mail.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful"""
        email = 'test@email.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(

            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        # check_password -> helper function coming with the user model,
        # checking that the password is correct
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@EmAiL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(

            'test@email.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        # user.is_staff -> not defined in the model,
        #  included as part of the permissions mixin
        self.assertTrue(user.is_staff)

    # test_tag_str: creates a tag,  and checks tat qhen converting it
    # to string, it gives us the name

    def test_tag_str(self):
        """ Test the tag string representation"""

        tag = models.Tag.objects.create(

            user=sample_user(),
            name='vegan',
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """ Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(


            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)
