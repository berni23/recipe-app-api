from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client, TestCase


class AdminSiteTests(TestCase):

    # create setup function, ran before every test runs
    # create superuser and normal user
    def setUp(self):

        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(

            email='admin@test.com',
            password='password1234'

        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(

            email='test@email.com',
            password='password1234',
            name='Test user full name'

        )

    # test that users are listed in django admin. slightly customize user model
    # admin expects username as the main field, we instead provide email

    def test_users_listed(self):
        """ Test that users are listed on user page"""

        # generate the url for the  list user page
        # reverse function-> allows for changing the url
        # and bechanged automatically
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        # assertContains -> django custom assertion, checks
        # that http response is 200 and the content includes the
        # passed content

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """ Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """ Test that the crate user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
