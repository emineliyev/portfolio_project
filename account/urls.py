from django.urls import path
from .views import login, registration, logout_view, profile, UserView, user_delete

app_name = 'accounts'
urlpatterns = [
    path('', login, name='login'),
    path('user-list/', UserView.as_view(), name='user-list'),
    path('user_delete/<int:user_id>/', user_delete, name='user_delete'),
    path('registration/', registration, name='registration'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
]