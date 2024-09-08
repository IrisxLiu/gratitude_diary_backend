""" Test urlpatterns """
from django.test import TestCase
from django.urls import reverse, resolve
from joylist.views import home, joy_list, joy_detail, joy_delete, joy_edit


class TestUrls(TestCase):
    def test_home(self):
        """ Test home page
            Parameters:
                self: current testcase
        """
        print("home url tested")
        url = reverse('chill_check:home')
        self.assertEqual(resolve(url).func, home)

    def test_joy_list(self):
        """ Test all joys list page
            Parameters:
                self: current testcase
        """
        print("list url tested")
        url = reverse('chill_check:joys')
        self.assertEqual(resolve(url).func, joy_list)

    def test_joy_detail(self):
        """ Test detail page
            Parameters:
                self: current testcase
        """
        print("detail url tested")
        url = reverse('chill_check:detail', args=[3])
        self.assertEqual(resolve(url).func, joy_detail)

    def test_joy_edit(self):
        """ Test edit page
            Parameters:
                self: current testcase
        """
        print("edit url tested")
        url = reverse('chill_check:edit', args=[1])
        self.assertEqual(resolve(url).func, joy_edit)

    def test_joy_delete(self):
        """ Test delete page
            Parameters:
                self: current testcase
        """
        print("delete url tested")
        url = reverse('chill_check:delete', args=[5])
        self.assertEqual(resolve(url).func, joy_delete)
