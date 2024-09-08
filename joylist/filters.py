import django_filters
from django_filters import DateFilter, CharFilter
from .models import Joy


class JoyFilter(django_filters.FilterSet):
    title = CharFilter(
        field_name="title", lookup_expr="icontains", label="Title"
    )  # case insensitive
    desc = CharFilter(
        field_name="desc", lookup_expr="icontains", label="Detail"
    )
    start_date = DateFilter(
        field_name="created", lookup_expr="date__gte",
        label="After Date(mm/dd/yyyy)"
    )
    end_date = DateFilter(
        field_name="created", lookup_expr="date__lte",
        label="Before Date(mm/dd/yyyy)"
    )

    class Meta:
        model = Joy
        fields = ["title", "desc"]
