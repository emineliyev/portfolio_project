from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView, CreateView, ListView
from django.contrib import messages
from django.db.models import ProtectedError
from about.models import About, BusinessPlan, Partners
from dashboard.forms.about_form import AboutForm, BusinessPlaneForm, PartnersForm
from dashboard.forms.portfolio_form import PortfolioForm
from portfolio.models import Portfolio


# def handler404(request, exception):
#     return render(request, '404/404.html', status=404)


def index(request):
    return render(request, 'dashboard/index.html')


# ABOUT
class AddAbout(SuccessMessageMixin, UpdateView):
    model = About
    form_class = AboutForm
    template_name = 'dashboard/about/about.html'
    success_message = 'Məlumatlar uğurla yeniləndi!'

    def get_success_url(self):
        return reverse_lazy('dashboards:about', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return About.objects.get(pk=pk)


# BUSINESS PLAN
class BusinessPlanView(ListView):
    model = BusinessPlan
    template_name = 'dashboard/business-plan/business-plan.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BusinessPlanView, self).get_context_data()
        context['businesses'] = BusinessPlan.objects.all().order_by('-id')
        return context


class AddBusinessPlan(SuccessMessageMixin, CreateView):
    form_class = BusinessPlaneForm
    template_name = 'dashboard/business-plan/add-business-plan.html'
    success_url = reverse_lazy('dashboards:business-plan')
    success_message = 'Məlumatlar uğurla əlavə edildi!'

    def get_context_data(self, **kwargs):
        context = super(AddBusinessPlan, self).get_context_data()
        return context


class UpdateBusinessPlan(SuccessMessageMixin, UpdateView):
    model = BusinessPlan
    form_class = BusinessPlaneForm
    template_name = 'dashboard/business-plan/update-business-plan.html'
    success_url = reverse_lazy('dashboards:business-plan')
    success_message = 'Məlumatlar uğurla yeniləndi!'

    def get_context_data(self, **kwargs):
        context = super(UpdateBusinessPlan, self).get_context_data()
        return context


@csrf_exempt
def delete_business_plan(request, business_plan_id):
    reader = BusinessPlan.objects.get(id=business_plan_id)
    try:
        reader.delete()
        messages.success(request, 'Biznes plan silindi!')

    except ProtectedError:
        messages.error(request, 'Xəta baş verdi!')
    return redirect('dashboards:business-plan')


# PARTNERS
class PartnersListView(ListView):
    model = Partners
    template_name = 'dashboard/partner/partners-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PartnersListView, self).get_context_data()
        context['partners'] = Partners.objects.all().order_by('-id')
        return context


class CreatePartner(SuccessMessageMixin, CreateView):
    form_class = PartnersForm
    template_name = 'dashboard/partner/create-partner.html'
    success_url = reverse_lazy('dashboards:partners-list')
    success_message = 'Məlumatlar uğurla əlavə edildi!'

    def get_context_data(self, **kwargs):
        context = super(CreatePartner, self).get_context_data()
        return context


class UpdatePartner(SuccessMessageMixin, UpdateView):
    model = Partners
    form_class = PartnersForm
    template_name = 'dashboard/partner/update-partner.html'
    success_url = reverse_lazy('dashboards:partners-list')
    success_message = 'Məlumatlar uğurla yeniləndi!'

    def get_context_data(self, **kwargs):
        context = super(UpdatePartner, self).get_context_data()
        return context


@csrf_exempt
def delete_partner(request, partner_id):
    reader = Partners.objects.get(id=partner_id)
    try:
        reader.delete()
        messages.success(request, 'Biznes plan silindi!')

    except ProtectedError:
        messages.error(request, 'Xəta baş verdi!')
    return redirect('dashboards:partners-list')


# PORTFOLIO
class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'dashboard/portfolio/portfolio-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PortfolioListView, self).get_context_data()
        context['portfolios'] = Portfolio.objects.all().order_by('-create_at')
        return context


class CreatePortfolio(View):
    model = Portfolio
    form_class = PortfolioForm
    template_name = 'dashboard/portfolio/create-portfolio.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            category = form.cleaned_data['category']
            client = form.cleaned_data['client']
            delivery_date = form.cleaned_data['delivery_date']
            portfolio_url = form.cleaned_data['portfolio_url']
            status = form.cleaned_data['status']
            for image in request.FILES.getlist('images'):
                Portfolio.objects.create(
                    image=image,
                    title=title,
                    description=description,
                    category=category,
                    client=client,
                    delivery_date=delivery_date,
                    portfolio_url=portfolio_url,
                    status=status,
                )
            form.save()
            return render(request, 'dashboard/portfolio/portfolio-list.html')
        return render(request, self.template_name, {"form": form})


class UpdatePortfolio(UpdatePartner):
    pass


def delete_portfolio(request):
    pass


# CATEGORY
class CategoryListView(ListView):
    pass


class CreateCategory(CreateView):
    pass


class UpdateCategory(UpdatePartner):
    pass


def delete_category(request):
    pass
