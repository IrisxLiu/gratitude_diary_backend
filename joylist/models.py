""" Sets structure of database table """
from django.db import models
from django.contrib.auth.models import User


class Joy(models.Model):
    """ class Joy
        Attributes: title, desc, created
        Method: __str__
        Meta: ordering
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    title = models.CharField("Title", max_length=200, null=True)
    desc = models.TextField("Detail", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ String representation by its title
            Parameters:
                self: current testcase
        """
        return self.title

    class Meta:
        """ Sort objects from newest to oldest """
        ordering = ["-created"]  # - reverse the sorting order
