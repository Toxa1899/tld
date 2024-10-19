from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi




schema_view = get_schema_view(
   openapi.Info(
      title="WIT digital recorder",
      default_version='v1',


   ),
   public=True,
)



urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/v1/account/', include('applications.account.urls')),
    path('api/v1/company/', include('applications.company.urls')),
    path('api/v1/chat/', include('applications.messagesandchat.urls')),
    path('api/v1/map/', include('applications.map.urls')),
    path('api/v1/statisticsdriver/', include('applications.statisticsdriver.urls')),
    path('api/v1/', include('applications.driver.urls')),
    path('swagger/', schema_view.with_ui('swagger')),

 
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

