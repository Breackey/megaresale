from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'


urlpatterns = [
# previous login view
# path('login/', views.user_login, name='login'),
path('login/', auth_views.LoginView.as_view(), name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]


""" from django.urls import path
from . views import register
from . import views


app_name = 'accounts'

urlpatterns = [
    path('register/' , views.register , name='register') , 
    path('' , views.user_login , name='user_login') , 

    # path('password_change/' , auth_views.PasswordChangeView.as_view() , name='password_change') , 
    # path('password_change/done/' , auth_views.PasswordChangeDoneView.as_view() , name='password_change_done') , 
    # path('password_reset/' , auth_views.PasswordResetView.as_view() , name='password_reset') , 
    # path('password_reset/done/' , auth_views.PasswordResetDoneView.as_view() , name='password_reset_done') , 


# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']

] """