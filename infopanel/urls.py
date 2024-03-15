from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from panel import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', views.index, name='index'),
    path('news-list/', views.news_list, name='news-list'),
    path('pravila/', views.pravila, name='pravila'),
    path('pushkin/', views.pushkin, name='pushkin'),
    path('qr-code-list/', views.qr, name='qr-code-list'),
    path('events-list/', views.events_list, name='events-list'),
    path('krujki-list/', views.krujki_list, name='krujki-list'),
    path('reglament-list/', views.reglament_list, name='reglament-list'),
    path('reglament/<int:pk>/', views.reglament_detail, name='reglament'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('krujki/<int:pk>/', views.krujok_detail, name='krujok_detail'),
    path('services/', views.services_list, name='services_list'),
    path('shedule/', views.shedule_list, name='shedule_list'),
]

if settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
