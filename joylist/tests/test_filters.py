""" Test all filters """
from django.test import TestCase
from django.utils import timezone
from joylist.filters import JoyFilter
from joylist.forms import JoyForm
from joylist.models import Joy


class TestFilters(TestCase):
    def setUp(self):
        """ Set up instances for later use
            Parameters:
                self: current testcase
        """
        self.joy1 = Joy.objects.create(
            title="Joy1",
            desc="Desc1",
            created=timezone.now()
        )
        self.joy2 = Joy.objects.create(
            title="Joy2",
            desc="Desc2",
            created=timezone.now()
        )
        self.joy3 = Joy.objects.create(
            title="Joy3",
            desc="Desc3",
            created=timezone.now()
        )

    def test_title(self):
        """ Test title filter
            Parameters:
                self: current testcase
        """
        filter = JoyFilter(
            data={"title": "Joy1"},
            queryset=Joy.objects.all()
        )
        self.assertTrue(filter.is_valid())
        self.assertQuerySetEqual(list(filter.qs), [self.joy1])

    def test_desc(self):
        """ Test desc filter
            Parameters:
                self: current testcase
        """
        filter = JoyFilter(
            data={"desc": "Desc1"},
            queryset=Joy.objects.all()
        )
        self.assertTrue(filter.is_valid())
        self.assertQuerySetEqual(list(filter.qs), [self.joy1])

    def test_start_date(self):
        """ Test start date filter
            Parameters:
                self: current testcase
        """
        filter = JoyFilter(
            data={"start_date": timezone.now().strftime("%m/%d/%Y")},
            queryset=Joy.objects.all()
        )
        self.assertTrue(filter.is_valid())
        self.assertQuerySetEqual(
            list(filter.qs), [self.joy3, self.joy2, self.joy1]
            )

    def test_end_date(self):
        """ Test end date filter
            Parameters:
                self: current testcase
        """
        filter = JoyFilter(
            data={"end_date": timezone.now().strftime("%m/%d/%Y")},
            queryset=Joy.objects.all()
        )
        self.assertTrue(filter.is_valid())
        self.assertQuerySetEqual(
            filter.qs, [self.joy3, self.joy2, self.joy1]
        )

    def test_all_filters(self):
        """ Test all filters combined
            Parameters:
                self: current testcase
        """
        filter_data = {
            "title": "Joy1",
            "desc": "Desc1",
            "start_date": self.joy1.created.strftime("%m/%d/%Y"),
            "end_date": self.joy1.created.strftime("%m/%d/%Y"),
        }
        filter = JoyFilter(data=filter_data, queryset=Joy.objects.all())
        self.assertTrue(filter.is_valid())
        self.assertQuerySetEqual(list(filter.qs), [self.joy1])
