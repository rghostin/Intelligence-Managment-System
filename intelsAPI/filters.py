import django_filters

from intelsAPI.models import Intel, Tag


class IntelFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    creation_date = django_filters.DateFilter()
    creation_date__gte = django_filters.DateFilter(field_name='creation_date', lookup_expr='gte')
    creation_date__lte = django_filters.DateFilter(field_name='creation_date', lookup_expr='lte')

    tag = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(),
                                                          field_name="tags__name",
                                                          to_field_name="name", conjoined=True)

    class Meta:
        model = Intel
        fields = ['title', 'creation_date']

