from django.urls import path
from .views import index, AddAbout, AddBusinessPlan, BusinessPlanView, delete_business_plan, UpdateBusinessPlan, \
    PartnersListView, CreatePartner, delete_partner, UpdatePartner, PortfolioListView, CreatePortfolio, UpdatePortfolio, \
    delete_portfolio, CategoryListView, CreateCategory, UpdateCategory, category_delete, SliderView, CreateSlider, \
    UpdateSlider, slider_delete, UpdateService, ServiceTypeView, CreateServiceType, UpdateServiceType, \
    service_type_delete, TeamView, CreateTeam, UpdateTeam, team_delete, IconView, CreateIcon, UpdateIcon, icon_delete, \
    PhoneView, CreatePhone, UpdatePhone, phone_delete, EmailView, CreateEmail, UpdateEmail, email_delete, SocIconView, \
    SocIconCreate, SocIconUpdate, network_delete, AddContact

app_name = 'dashboards'
urlpatterns = [
    path('', index, name='index'),
    # BOUT
    path('about/<int:pk>/', AddAbout.as_view(), name='about'),
    # BUSINESS PLAN
    path('business-plan/', BusinessPlanView.as_view(), name='business-plan'),
    path('add-business-plan/', AddBusinessPlan.as_view(), name='add-business-plan'),
    path('update-business-plan/<int:pk>/', UpdateBusinessPlan.as_view(), name='update-business-plan'),
    path('business_plan_delete/<int:business_plan_id>/', delete_business_plan, name='business_plan_delete'),
    # PARTNERS
    path('partners-list/', PartnersListView.as_view(), name='partners-list'),
    path('create-partner/', CreatePartner.as_view(), name='create-partner'),
    path('update-partner/<int:pk>/', UpdatePartner.as_view(), name='update-partner'),
    path('partner_delete/<int:partner_id>/', delete_partner, name='partner_delete'),
    # PORTFOLIO
    path('portfolio-list/', PortfolioListView.as_view(), name='portfolio-list'),
    path('create-portfolio/', CreatePortfolio.as_view(), name='create-portfolio'),
    path('update-portfolio/<int:pk>/', UpdatePortfolio.as_view(), name='update-portfolio'),
    path('portfolio_delete/<int:portfolio_id>/', delete_portfolio, name='portfolio_delete'),
    # CATEGORY
    path('category-list/', CategoryListView.as_view(), name='category-list'),
    path('create-category/', CreateCategory.as_view(), name='create-category'),
    path('update-category/<int:pk>/', UpdateCategory.as_view(), name='update-category'),
    path('category_delete/<int:category_id>/', category_delete, name='category_delete'),
    # SLIDER
    path('slider-list/', SliderView.as_view(), name='slider-list'),
    path('create-slider/', CreateSlider.as_view(), name='create-slider'),
    path('update-slider/<int:pk>/', UpdateSlider.as_view(), name='update-slider'),
    path('slider_delete/<int:slider_id>/', slider_delete, name='slider_delete'),
    # SERVICE
    path('dashboard/service/<int:pk>/', UpdateService.as_view(), name='service'),

    path('services-type-list/', ServiceTypeView.as_view(), name='services-type-list'),
    path('create-services-type/', CreateServiceType.as_view(), name='create-services-type'),
    path('update-services-type/<int:pk>/', UpdateServiceType.as_view(), name='update-services-type'),
    path('service_type_delete/<int:services_type_id>/', service_type_delete, name='service_type_delete'),
    # TEAM
    path('team-list/', TeamView.as_view(), name='team-list'),
    path('create-team/', CreateTeam.as_view(), name='create-team'),
    path('update-team/<int:pk>/', UpdateTeam.as_view(), name='update-team'),
    path('team_delete/<int:team_id>/', team_delete, name='team_delete'),
    # ARRANGEMENTS
    #     ICONS
    path('icon-lists/', IconView.as_view(), name='icon-lists'),
    path('create-icon/', CreateIcon.as_view(), name='create-icon'),
    path('update-icon/<int:pk>/', UpdateIcon.as_view(), name='update-icon'),
    path('icon_delete/<int:icon_id>/', icon_delete, name='icon_delete'),
        # PHONE
    path('phone-list/', PhoneView.as_view(), name='phone-list'),
    path('create-phone/', CreatePhone.as_view(), name='create-phone'),
    path('update-phone/<int:pk>/', UpdatePhone.as_view(), name='update-phone'),
    path('phone_delete/<int:phone_id>/', phone_delete, name='phone_delete'),
        # EMAIL
    path('email-list/', EmailView.as_view(), name='email-list'),
    path('create-email/', CreateEmail.as_view(), name='create-email'),
    path('update-email/<int:pk>/', UpdateEmail.as_view(), name='update-email'),
    path('email_delete/<int:email_id>/', email_delete, name='email_delete'),
        # SOCIAL NETWORK
    path('social-network-list/', SocIconView.as_view(), name='social-network-list'),
    path('create-social-network/', SocIconCreate.as_view(), name='create-social-network'),
    path('update-social-network/<int:pk>/', SocIconUpdate.as_view(), name='update-social-network'),
    path('network_delete/<int:network_id>/', network_delete, name='network_delete'),
        # CONTACT
    path('dashboard/update-contact/<int:pk>/', AddContact.as_view(), name='update-contact'),
]






