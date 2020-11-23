import django_filters
from django_filters.widgets import RangeWidget

from intelsAPI.models import Intel, Tag


class IntelFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    creation_date_range = django_filters.DateFromToRangeFilter(field_name='creation_date')
    tag = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(),
                                                          field_name="tags__name",
                                                          to_field_name="name", conjoined=True)

    class Meta:
        model = Intel
        fields = ['title']

