""" Test JoyForm """
from django.test import TestCase
from joylist.forms import JoyForm
from joylist.models import Joy


class TestForms(TestCase):
    def setUp(self):
        """ Set up the form for future use
            Parameters:
                self: current testcase
        """
        self.form = JoyForm(
            data={'title': 'Test', 'desc': 'Test form'}
            )

    def test_create_form(self):
        """ Test form creation
            Parameters:
                self: current testcase
        """
        print("create tested")
        self.assertTrue(self.form.is_valid())

    def test_invalid_form(self):
        """ Test to create an empty form
            Parameters:
                self: current testcase
        """
        form = JoyForm()
        self.assertFalse(form.is_valid())

    def test_placeholder(self):
        """ Test the placeholders of the form
            Parameters:
                self: current testcase
        """
        print("placeholder tested")
        title_placeholder = self.form.fields['title'].widget.attrs.get(
            'placeholder'
            )
        desc_placeholder = self.form.fields['desc'].widget.attrs.get(
            'placeholder'
            )
        self.assertEqual(
            title_placeholder,
            "Highlight"
            )
        self.assertEqual(
            desc_placeholder,
            "Illustrate the story behind you smile"
            )

    def test_model_assignment(self):
        """ Test if the form is associated with Joy model
            Parameters:
                self: current testcase
        """
        print('model tested')
        self.assertEqual(
            self.form._meta.model, Joy
            )

    def test_fields(self):
        """ Test if all fields of Joy model are included
            Parameters:
                self: current testcase
        """
        print('fields tested')
        self.assertIn('title', self.form.fields)
        self.assertIn('desc', self.form.fields)
