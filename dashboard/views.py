from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.db.models import ProtectedError

from django.views.generic import UpdateView, CreateView, ListView
from about.models import About, BusinessPlan, Partners
from account.models import User
from arrangements.models import Icons, Phone, Email, SocIcon, Arrangements
from dashboard.forms.about_form import AboutForm, BusinessPlaneForm, PartnersForm
from dashboard.forms.contact_form import ContactForm
from dashboard.forms.email_form import EmailForm
from dashboard.forms.icons_form import IconForm
from dashboard.forms.phone_form import PhoneForm
from dashboard.forms.portfolio_form import PortfolioForm, PortfolioImageForm, CategoryForm
from dashboard.forms.service_form import ServiceForm, ServiceTypeForm
from dashboard.forms.slider_form import SliderForm
from dashboard.forms.social_network_form import SocialNetworkForm
from dashboard.forms.team_form import TeamForm
from portfolio.models import Portfolio, PortfolioImage, Category
from services.models import Service, ServiceType
from slider.models import Slider
from team.models import Team


@login_required
def index(request):
    portfolio_count = Portfolio.objects.count()
    slider_count = Slider.objects.count()
    partner_count = Partners.objects.count()
    team_count = Team.objects.count()
    user_count = User.objects.count()
    context = {
        'portfolio_count': portfolio_count,
        'slider_count': slider_count,
        'partner_count': partner_count,
        'team_count': team_count,
        'user_count': user_count
    }
    return render(request, 'dashboard/index.html', context=context)


# ABOUT
class AddAbout(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
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
class BusinessPlanView(LoginRequiredMixin, ListView):
    model = BusinessPlan
    template_name = 'dashboard/business-plan/business-plan.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BusinessPlanView, self).get_context_data()
        context['businesses'] = BusinessPlan.objects.all().order_by('-id')
        return context


class AddBusinessPlan(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = BusinessPlaneForm
    template_name = 'dashboard/business-plan/add-business-plan.html'
    success_url = reverse_lazy('dashboards:business-plan')
    success_message = 'Məlumatlar uğurla əlavə edildi!'

    def get_context_data(self, **kwargs):
        context = super(AddBusinessPlan, self).get_context_data()
        return context


class UpdateBusinessPlan(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
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
    business_plan = BusinessPlan.objects.get(id=business_plan_id)
    try:
        business_plan.delete()
        messages.success(request, 'Biznes plan silindi!')

    except ProtectedError:
        messages.error(request, 'Xəta baş verdi!')
    return redirect('dashboards:business-plan')


# PARTNERS
class PartnersListView(LoginRequiredMixin, ListView):
    model = Partners
    template_name = 'dashboard/partner/partners-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PartnersListView, self).get_context_data()
        context['partners'] = Partners.objects.all().order_by('-id')
        return context


class CreatePartner(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = PartnersForm
    template_name = 'dashboard/partner/create-partner.html'
    success_url = reverse_lazy('dashboards:partners-list')
    success_message = 'Məlumatlar uğurla əlavə edildi!'

    def get_context_data(self, **kwargs):
        context = super(CreatePartner, self).get_context_data()
        return context


class UpdatePartner(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
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
    partner = Partners.objects.get(id=partner_id)
    try:
        partner.delete()
        messages.success(request, 'Biznes plan silindi!')

    except ProtectedError:
        messages.error(request, 'Xəta baş verdi!')
    return redirect('dashboards:partners-list')


# PORTFOLIO
class PortfolioListView(LoginRequiredMixin, ListView):
    model = Portfolio
    template_name = 'dashboard/portfolio/portfolio-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PortfolioListView, self).get_context_data()
        context['portfolios'] = Portfolio.objects.all().order_by('-create_at')
        context['portfolio_counter'] = Portfolio.objects.count()
        return context


class CreatePortfolio(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Portfolio
    form_class = PortfolioForm
    template_name = 'dashboard/portfolio/create-portfolio.html'
    success_url = reverse_lazy('dashboards:portfolio-list')
    success_message = 'Layihə uğurla əlavə edildi!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_form'] = PortfolioImageForm(self.request.POST, self.request.FILES)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        image_form = context['image_form']

        if form.is_valid() and image_form.is_valid():
            self.object = form.save()

            for image in self.request.FILES.getlist('image'):
                PortfolioImage.objects.create(portfolio=self.object, image=image)

            return HttpResponseRedirect(self.get_success_url())
        return self.render_to_response(self.get_context_data(form=form))


class UpdatePortfolio(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Portfolio
    form_class = PortfolioForm
    template_name = 'dashboard/portfolio/update-portfolio.html'
    success_url = reverse_lazy('dashboards:portfolio-list')
    success_message = 'Layihə uğurla yeniləndi!'

    def get_context_data(self, **kwargs):
        context = super(UpdatePortfolio, self).get_context_data()
        context['images'] = self.object.portfolio_image.all()
        context['image_form'] = PortfolioImageForm()
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        images_to_delete = self.request.POST.getlist('delete_images')
        for image_id in images_to_delete:
            try:
                image = PortfolioImage.objects.get(id=image_id)
                if image:
                    image.delete()
            except PortfolioImage.DoesNotExist:
                raise Http404('Şəkil yoxdur!')

        # Привязываем изображения к объекту Portfolio
        images = self.request.FILES.getlist('image')
        for image in images:
            portfolio_image = PortfolioImage(image=image, portfolio=self.object)
            portfolio_image.save()

        # Сохраняем объект Portfolio
        self.object.save()
        return super().form_valid(form)


@csrf_exempt
def delete_portfolio(request, portfolio_id):
    portfolio = Portfolio.objects.get(id=portfolio_id)
    try:
        portfolio.delete()
        messages.success(request, 'Layihə uğurla silindi!')

    except ProtectedError:
        messages.error(request, 'Xəta baş verdi!')
    return redirect('dashboards:portfolio-list')


# CATEGORY
class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'dashboard/portfolio/category-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data()
        context['categories'] = Category.objects.all().order_by('name')
        return context


class CreateCategory(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CategoryForm
    template_name = 'dashboard/portfolio/create-category.html'
    success_url = reverse_lazy('dashboards:category-list')
    success_message = 'Kateqoriya uğurla əlavə edildi!'

    def get_context_data(self, **kwargs):
        context = super(CreateCategory, self).get_context_data()
        return context


class UpdateCategory(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'dashboard/portfolio/update-category.html'
    success_url = reverse_lazy('dashboards:category-list')
    success_message = 'Kateqoriya uğurla yeniləndi!'

    def get_context_data(self, **kwargs):
        context = super(UpdateCategory, self).get_context_data()
        return context


@csrf_exempt
def category_delete(request, category_id):
    category = Category.objects.get(id=category_id)
    try:
        category.delete()
        messages.success(request, 'Kateqoriya uğurla silindi!')

    except ProtectedError:
        response_data = {'error': 'Kateqoriya aktiv layihə ilə əlaqədədir!'}
        return JsonResponse(response_data)
    return redirect('dashboards:category-list')


# SLIDER
class SliderView(LoginRequiredMixin, ListView):
    model = Slider
    template_name = 'dashboard/sliders/slider-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SliderView, self).get_context_data()
        context['sliders'] = Slider.objects.all().order_by('-id')
        return context


class CreateSlider(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = SliderForm
    template_name = 'dashboard/sliders/create-slider.html'
    success_url = reverse_lazy('dashboards:slider-list')
    success_message = 'Slayder uğurla əlavə edildi!'

    def get_context_data(self, **kwargs):
        context = super(CreateSlider, self).get_context_data()
        return context


class UpdateSlider(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Slider
    form_class = SliderForm
    template_name = 'dashboard/sliders/update-slider.html'
    success_url = reverse_lazy('dashboards:slider-list')
    success_message = 'Slayder uğurla yeniləndi!'

    def get_context_data(self, **kwargs):
        context = super(UpdateSlider, self).get_context_data()
        return context


@csrf_exempt
def slider_delete(request, slider_id):
    slider = Slider.objects.get(id=slider_id)
    try:
        slider.delete()
        messages.success(request, 'Slayder uğurla silindi!')

    except ProtectedError:
        messages.error(request, 'Xəta baş verdi!')
    return redirect('dashboards:slider-list')


# SERVICES
class UpdateService(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'dashboard/services/service.html'
    success_message = 'Məlumatlar uğurla yeniləndi!'

    def get_success_url(self):
        return reverse_lazy('dashboards:service', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return Service.objects.get(pk=pk)


class ServiceTypeView(LoginRequiredMixin, ListView):
    model = ServiceType
    template_name = 'dashboard/services/service-type-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ServiceTypeView, self).get_context_data()
        context['services_types'] = ServiceType.objects.all().order_by('-id')
        return context


class CreateServiceType(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ServiceTypeForm
    template_name = 'dashboard/services/create-service-type.html'
    success_url = reverse_lazy('dashboards:services-type-list')
    success_message = 'Xidmət növü uğurla əlavə edildi!'

    def get_context_data(self, **kwargs):
        context = super(CreateServiceType, self).get_context_data()
        return context


class UpdateServiceType(LoginRequiredMixin, UpdateView):
    model = ServiceType
    form_class = ServiceTypeForm
    template_name = 'dashboard/services/update-service-type.html'
    success_url = reverse_lazy('dashboards:services-type-list')
    success_message = 'Xidmət növü uğurla yeniləndi!'

    def get_context_data(self, **kwargs):
        context = super(UpdateServiceType, self).get_context_data()
        return context


@csrf_exempt
def service_type_delete(request, services_type_id):
    service_type = ServiceType.objects.get(id=services_type_id)
    try:
        service_type.delete()
        messages.success(request, 'Xidmət növü uğurla silindi!')

    except ProtectedError:
        messages.error(request, 'Xəta baş verdi!')
    return redirect('dashboards:services-type-list')


# TEAM
class TeamView(LoginRequiredMixin, ListView):
    model = Team
    template_name = 'dashboard/team/team-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TeamView, self).get_context_data()
        context['teams'] = Team.objects.all().order_by('-id')
        return context


class CreateTeam(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = TeamForm
    template_name = 'dashboard/team/create-team.html'
    success_url = reverse_lazy('dashboards:team-list')
    success_message = 'Əməkdaş uğurla əlavə edildi!'

    def get_context_data(self, **kwargs):
        context = super(CreateTeam, self).get_context_data()
        return context


class UpdateTeam(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Team
    form_class = TeamForm
    template_name = 'dashboard/team/update-team.html'
    success_url = reverse_lazy('dashboards:team-list')
    success_message = 'Əməkdaşın məlumatları uğurla yeniləndi!'

    def get_context_data(self, **kwargs):
        context = super(UpdateTeam, self).get_context_data()
        return context


@csrf_exempt
def team_delete(request, team_id):
    team = Team.objects.get(id=team_id)
    try:
        team.delete()
        messages.success(request, 'Əməkdaş uğurla silindi!')

    except ProtectedError:
        messages.error(request, 'Xəta baş verdi!')
    return redirect('dashboards:team-list')


# ARRANGEMENTS
#     ICONS
class IconView(LoginRequiredMixin, ListView):
    model = Icons
    template_name = 'dashboard/arrangements/icons/icon-lists.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IconView, self).get_context_data()
        context['icons'] = Icons.objects.all().order_by('name')
        return context


class CreateIcon(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = IconForm
    template_name = 'dashboard/arrangements/icons/create-icon.html'
    success_url = reverse_lazy('dashboards:icon-lists')
    success_message = 'Ikon uğurla əlavə edildi!'

    def get_context_data(self, **kwargs):
        context = super(CreateIcon, self).get_context_data()
        return context


class UpdateIcon(LoginRequiredMixin, UpdateView):
    model = Icons
    form_class = IconForm
    template_name = 'dashboard/arrangements/icons/update-icon.html'
    success_url = reverse_lazy('dashboards:icon-lists')
    success_message = 'Ikon uğurla yeniləndi!'

    def get_context_data(self, **kwargs):
        context = super(UpdateIcon, self).get_context_data()
        return context


@csrf_exempt
def icon_delete(request, icon_id):
    icon = Icons.objects.get(id=icon_id)
    try:
        icon.delete()
        messages.success(request, 'Ikon uğurla silindi!')

    except ProtectedError:
        messages.error(request, 'Xəta baş verdi!')
    return redirect('dashboards:icon-lists')

    # PHONE NUMBERS


class PhoneView(LoginRequiredMixin, ListView):
    model = Phone
    template_name = 'dashboard/arrangements/phone/phone-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PhoneView, self).get_context_data()
        context['phones'] = Phone.objects.all().order_by('-id')
        return context


class CreatePhone(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = PhoneForm
    template_name = 'dashboard/arrangements/phone/create-phone.html'
    success_url = reverse_lazy('dashboards:phone-list')
    success_message = 'Telefon nömrəsi uğurla əlavə edildi!'

    def get_context_data(self, **kwargs):
        context = super(CreatePhone, self).get_context_data()
        return context


class UpdatePhone(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Phone
    form_class = PhoneForm
    template_name = 'dashboard/arrangements/phone/update-phone.html'
    success_url = reverse_lazy('dashboards:phone-list')
    success_message = 'Telefon nömrəsi uğurla yeniləndi!'

    def get_context_data(self, **kwargs):
        context = super(UpdatePhone, self).get_context_data()
        return context


@csrf_exempt
def phone_delete(request, phone_id):
    phone = Phone.objects.get(id=phone_id)
    try:
        phone.delete()
        messages.success(request, 'Nömrə uğurla silindi!')

    except ProtectedError:
        messages.error(request, 'Xəta baş verdi!')
    return redirect('dashboards:phone-list')

    # EMAIL


class EmailView(ListView):
    model = Email
    template_name = 'dashboard/arrangements/email/email-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EmailView, self).get_context_data()
        context['emails'] = Email.objects.all().order_by('-id')
        return context


class CreateEmail(SuccessMessageMixin, CreateView):
    form_class = EmailForm
    template_name = 'dashboard/arrangements/email/create-email.html'
    success_url = reverse_lazy('dashboards:email-list')
    success_message = 'Email ünvanı uğurla əlavə edildi!'

    def get_context_data(self, **kwargs):
        context = super(CreateEmail, self).get_context_data()
        return context


class UpdateEmail(SuccessMessageMixin, UpdateView):
    model = Email
    form_class = EmailForm
    template_name = 'dashboard/arrangements/email/update-email.html'
    success_url = reverse_lazy('dashboards:email-list')
    success_message = 'Email ünvan uğurla yeniləndi!'

    def get_context_data(self, **kwargs):
        context = super(UpdateEmail, self).get_context_data()
        return context


@csrf_exempt
def email_delete(request, email_id):
    email = Email.objects.get(id=email_id)
    try:
        email.delete()
        messages.success(request, 'Email ünvan silindi!')

    except ProtectedError:
        messages.error(request, 'Xəta baş verdi!')
    return redirect('dashboards:email-list')

    # SOCICON


class SocIconView(ListView):
    model = SocIcon
    template_name = 'dashboard/arrangements/social-network/social-network-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SocIconView, self).get_context_data()
        context['networks'] = SocIcon.objects.all().order_by('-id')
        return context


class SocIconCreate(SuccessMessageMixin, CreateView):
    form_class = SocialNetworkForm
    template_name = 'dashboard/arrangements/social-network/create-social-network.html'
    success_url = reverse_lazy('dashboards:social-network-list')
    success_message = 'Sosial şəbəkə uğurla əlavə edildi!'

    def get_context_data(self, **kwargs):
        context = super(SocIconCreate, self).get_context_data()
        return context


class SocIconUpdate(SuccessMessageMixin, UpdateView):
    model = SocIcon
    form_class = SocialNetworkForm
    template_name = 'dashboard/arrangements/social-network/update-social-network.html'
    success_url = reverse_lazy('dashboards:social-network-list')
    success_message = 'Sosial şəbəkə uğurla yeniləndi!'

    def get_context_data(self, **kwargs):
        context = super(SocIconUpdate, self).get_context_data()
        return context


@csrf_exempt
def network_delete(request, network_id):
    network = SocIcon.objects.get(id=network_id)
    try:
        network.delete()
        messages.success(request, 'Sosial şəbəkə silindi!')

    except ProtectedError:
        messages.error(request, 'Xəta baş verdi!')
    return redirect('dashboards:social-network-list')

    # CONTACT


class AddContact(SuccessMessageMixin, UpdateView):
    model = Arrangements
    form_class = ContactForm
    template_name = 'dashboard/arrangements/contact/update-contact.html'
    success_message = 'Məlumatlar uğurla yeniləndi!'

    def get_success_url(self):
        return reverse_lazy('dashboards:update-contact', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return Arrangements.objects.get(pk=pk)
