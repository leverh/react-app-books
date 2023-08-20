from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
    path('api/', include('reviews.urls')),
    path('api/', include('comments.urls')),
    path('api/', include('favorites.urls')),
    path('api/', include('subscriptions.urls')),
    path('api/', include('profiles.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
