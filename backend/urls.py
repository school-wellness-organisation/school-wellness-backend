from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # urls.py
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),

    path('api/users/', include('users.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
