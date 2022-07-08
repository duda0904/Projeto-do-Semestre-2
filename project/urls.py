from django.contrib import admin
from django.urls import path, include
from .views import homepage, adminpage
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('users.urls','users'), namespace='users')),
    path('tutorials/', include(('tutorials.urls','tutorials'), namespace='tutorials')),
    path('aplicacao/', include(('aplicacao.urls','aplicacao'), namespace='aplicacao')),
    path('admin-site/', adminpage, name="admin-page"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', homepage, name="homepage"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)