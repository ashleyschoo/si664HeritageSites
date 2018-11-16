import django_filters
from heritagesites.models import CountryArea, HeritageSite, HeritageSiteCategory, \
	IntermediateRegion, SubRegion, Region


class HeritageSiteFilter(django_filters.FilterSet):
	site_name = django_filters.CharFilter(
		field_name='site_name',
		label='Heritage Site Name',
		lookup_expr='icontains'
	)

	# Add description, heritage_site_category, region, sub_region and intermediate_region filters here
	description = django_filters.CharFilter(
		field_name='description',
		label='Description',
		lookup_expr='contains'

		)
	heritage_site_category = django_filters.ModelMultipleChoiceFilter(
		queryset=HeritageSiteCategory.objects.all(),
		field_name = 'heritage_site_category',
		label='Heritage Site Category',
		lookup_expr='exact'
		)

	region = django_filters.ModelMultipleChoiceFilter(
		queryset=Region.objects.all(),
		field_name = 'country_area__location__region__region_name',
		label = 'Region',
		)

	sub_region = django_filters.ModelMultipleChoiceFilter(
		queryset=SubRegion.objects.all(),
		field_name = 'country_area__location__sub_region__sub_region_name',
		label = 'Sub-Region',
		lookup_expr='exact'
		)

	intermediate_region = django_filters.ModelChoiceFilter(
		queryset=IntermediateRegion.objects.all(),
		field_name='country_area__location__intermediate_region__intermediate_region_name',
		label = 'Intermediate Region',
		lookup_expr='exact'
		)
		

	country_area = django_filters.ModelMultipleChoiceFilter(
		field_name='country_area',
		label='Country/Area',
		queryset=CountryArea.objects.all().order_by('country_area_name'),
		lookup_expr='exact'
	)

	# Add date_inscribed filter here
	
	date_inscribed = django_filters.NumberFilter(
		field_name = 'date_inscribed',
		label='Date Inscribed',
		lookup_expr='exact'
		)

	class Meta:
		model = HeritageSite
		# form = SearchForm
		# fields [] is required, even if empty.
		fields = []