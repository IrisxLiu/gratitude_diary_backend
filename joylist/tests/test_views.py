""" Test all the views in views.py """
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from joylist.models import Joy


class TestViews(TestCase):
    def setUp(self):
        """ Set up the variables needed in test methods
            Parameters:
                self: current testcase
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.joy = Joy.objects.create(title="testtitle", desc="testdesc")
        self.home_url = reverse('chill_check:home')
        self.list_url = reverse('chill_check:joys')
        self.detail_url = reverse('chill_check:detail', args=[self.joy.id])
        self.delete_url = reverse('chill_check:delete', args=[self.joy.id])
        self.edit_url = reverse('chill_check:edit', args=[self.joy.id])
        self.register_url = reverse('chill_check:register')
        self.login_url = reverse('chill_check:login')
        self.logout_url = reverse('chill_check:logout')

    def test_home(self):
        """ Test home view
            Expect to render the correct page and template
            Parameters:
                self: current testcase
        """
        print("home tested")
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'joylist/home.html')

    def test_home_post(self):
        """ Test POST method in home view
            Expect to save correct data and redirect the page correctly
            Parameters:
                self: current testcase
        """
        print("home post tested")
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(
            self.home_url,
            {"title": "testtitle", "desc": "testdesc"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Joy.objects.filter(title="testtitle").exists())

    def test_joy_list(self):
        """ Test joy list view
            Expect to render the correct page and template
            Parameters:
                self: current testcase
        """
        print("joy list tested")
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'joylist/joy_list.html')

    def test_joy_detail(self):
        """ Test joy detail view
            Expect to render the correct page and template
            Parameters:
                self: current testcase
        """
        print("detail tested")
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'joylist/joy_detail.html')

    def test_joy_edit(self):
        """ Test joy edit view
            Expect to edit the item and render correct page
            Parameters:
                self: current testcase
        """
        print("edit tested")
        self.client.login(username="testuser", password="testpassword")
        update_joy = {"title": "Update edit", "desc": "Update test edit"}
        response = self.client.post(self.edit_url, data=update_joy)
        self.joy.refresh_from_db()
        self.assertEqual(self.joy.title, "Update edit")
        self.assertEqual(self.joy.desc, "Update test edit")
        self.assertEqual(response.status_code, 302)

    def test_joy_delete(self):
        """ Test joy delete view
            Expect to delete the item and render the correct page
            Parameters:
                self: current testcase
        """
        print("delete tested")
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(self.delete_url)
        self.assertFalse(Joy.objects.filter(title="testtitle").exists())
        self.assertRedirects(response, self.list_url)

    def test_register(self):
        """ Test user register view
            Expect to create a new user and redirect to login page
        """
        print("register tested")
        response = self.client.post(
            self.register_url,
            {"username": "newuser", "email": "test@test.com",
             "password1": "testpassword", "password2": "testpassword"}
        )
        self.assertTrue(User.objects.filter(username="newuser").exists())
        self.assertRedirects(response, self.login_url)

    def test_login(self):
        """ Test user login view
            Expect to login and redirect to home page
            Parameters:
                self: current testcase
        """
        print("login tested")
        response = self.client.post(
            self.login_url,
            {"username": "testuser", "password": "testpassword"}
        )
        self.assertTrue(self.client.session["_auth_user_id"])
        self.assertRedirects(response, self.home_url)

    def test_logout(self):
        """ Test user logout view
            Expect to logout and redirect to login page
            Parameters:
                self: current testcase
        """
        print("logout tesed")
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(self.logout_url)
        self.assertFalse("_auth_user_id" in self.client.session)
        self.assertRedirects(response, self.login_url)
