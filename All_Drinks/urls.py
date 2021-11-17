from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from users.views import CustomAuthToken
from django.urls import path, include, re_path
from django.views.generic import TemplateView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('all_drinks/', include('drink.urls')),
    path('featured/products/', include('featured.urls')),
    path('banners/', include('banners.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/users/', include('users.urls')),
    path('ordersanditems/', include('orders.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('token-auth/', CustomAuthToken.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# where i include templates from  react build folder
urlpatterns += [
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
    
    # password reset confirm url
    #  re_path(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     PasswordResetConfirmView.as_view(),
    #     name='password_reset_confirm'),
    ]