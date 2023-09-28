from django.urls import path
from .views import index, AddAbout, AddBusinessPlan, BusinessPlanView, delete_business_plan, UpdateBusinessPlan, \
    PartnersListView, CreatePartner, delete_partner, UpdatePartner, PortfolioListView, CreatePortfolio

app_name = 'dashboards'
urlpatterns = [
    path('dashboard/', index, name='index'),
    # BOUT
    path('dashboard/about/<int:pk>/', AddAbout.as_view(), name='about'),
    # BUSINESS PLAN
    path('dashboard/business-plan/', BusinessPlanView.as_view(), name='business-plan'),
    path('dashboard/add-business-plan/', AddBusinessPlan.as_view(), name='add-business-plan'),
    path('dashboard/update-business-plan/<int:pk>/', UpdateBusinessPlan.as_view(), name='update-business-plan'),
    path('business_plan_delete/<int:business_plan_id>/', delete_business_plan, name='business_plan_delete'),
    # PARTNERS
    path('dashboard/partners-list/', PartnersListView.as_view(), name='partners-list'),
    path('dashboard/create-partner/', CreatePartner.as_view(), name='create-partner'),
    path('dashboard/update-partner/<int:pk>/', UpdatePartner.as_view(), name='update-partner'),
    path('partner_delete/<int:partner_id>/', delete_partner, name='partner_delete'),
    # PORTFOLIO
    path('dashboard/portfolio-list/', PortfolioListView.as_view(), name='portfolio-list'),
    path('dashboard/create-portfolio/', CreatePortfolio.as_view(), name='create-portfolio')
]
