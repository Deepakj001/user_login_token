from django.urls import path
from account.views import *
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
    path('delete/<int:user_id>', DeleteAccountView.as_view(), name='delete-account'),
    path('total-registered-users/', TotalRegisteredUsersView.as_view(), name='total-registered-users'),

]