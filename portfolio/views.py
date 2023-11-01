from django.shortcuts import render
from django.views.generic import ListView
from about.models import About, Partners, BusinessPlan
from arrangements.models import Arrangements
from portfolio.models import Portfolio, Category
from services.models import Service, ServiceType
from slider.models import Slider
from team.models import Team


class ServiceView(ListView):
    model = Service
    template_name = 'portfolio/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ServiceView, self).get_context_data()
        context['sliders'] = Slider.objects.all().filter(status=True)
        context['abouts'] = About.objects.all()
        context['business_planes'] = BusinessPlan.objects.all()
        context['services_types'] = ServiceType.objects.all()
        context['clients'] = Partners.objects.all().filter(active=True)
        context['portfolios'] = Portfolio.objects.all().filter(status=True)
        context['categories'] = Category.objects.all()
        context['teams'] = Team.objects.all()
        context['arrangements'] = Arrangements.objects.all()

        return context
