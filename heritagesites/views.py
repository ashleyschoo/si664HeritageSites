from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


from .models import HeritageSite
from .models import CountryArea

def index(request):
   return HttpResponse("Hello, world. You're at the UNESCO Heritage Sites index.")

class AboutPageView(generic.TemplateView):
	template_name = 'heritagesites/about.html'

class CountryAreaListView(generic.ListView): #may need ListView? include region stuff?
	model = CountryArea
	context_object_name = 'countries'
	template_name = 'heritagesites/countryarea.html'
	paginate_by = 20

	def get_queryset(self):
		return CountryArea.objects.all().order_by('country_area')

class CountryAreaDetailView(generic.DetailView):
	model = CountryArea
	context_object_name = 'country'
	template_name = 'heritagesites/country_area_detail.html'

class HomePageView(generic.TemplateView):
	template_name = 'heritagesites/home.html'


class SiteListView(generic.ListView):
	model = HeritageSite
	context_object_name = 'sites'
	template_name = 'heritagesites/site.html'
	paginate_by = 50

	def get_queryset(self):
		return HeritageSite.objects.all().select_related('heritage_site_category').order_by('site_name')

class SiteDetailView(generic.DetailView):
	model = HeritageSite
	context_object_name = 'site'
	template_name = 'heritagesites/site_detail.html'