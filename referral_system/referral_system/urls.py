from django.urls import path
from referral_system.views import AuthView, VerifyCodeView, ProfileView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path(
        'auth/',
        AuthView.as_view(),
        name='auth'
    ),
    path(
        'verify/',
        VerifyCodeView.as_view(),
        name='verify'
    ),
    path(
        'profile/<str:phone>/',
        ProfileView.as_view(),
        name='profile'
    ),
    path(
        'api/schema/',
        SpectacularAPIView.as_view(),
        name='schema'
    ),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),

]
