"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myblog import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

portfolio_url = [
    path('', views.portfolio, name='portfolio'),
    path('official-document-classify/',
         views.official_document_classify, name='official'),
    path('text_to_image/', views.text_to_image, name='image'),
    path('web_crawler/', views.web_crawler, name='crawler'),
    path('covid19/', views.covid19, name='covid'),
    path('newsletter_banner/', views.newsletter_banner, name='banner'),
    path('unsubscribe_email/', views.unsubscribe_email, name='unsubscribe'),
    path('cssiphone/', views.iphone, name='iphone'),

]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('message/', views.message),
    path('autobiography/', views.autobiography, name='autobiography'),
    path('portfolio/', include(portfolio_url)),
    path("captcha/", include("captcha.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
