from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# Here i will be adding different urls pattern

urlpatterns = [
    path('signup/', views.register_user, name='signup_page'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
                    template_name = 'accounts/password_reset.html'
                    ), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
                    template_name = 'accounts/password_reset_done.html'
                    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
                    template_name = 'accounts/password_reset_confirm.html'
                    ), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
                    template_name = 'accounts/password_reset_complete.html'
                    ), name='password_reset_complete'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('wallet/', views.walletView, name='wallet'),
    path('create_wallet/', views.createWallet, name='addwallet'),
    path('update_wallet/<str:pk>/', views.updateWallet, name='update_wallet'),
    path('delete_wallet/<str:pk>/', views.deleteWallet, name='delete_wallet'),
]

