"""
URL configuration for webpage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from basic.views import Carlist, CreateProfile, ProductProfile, home,about,contact,service,sample,sample1,sample2,sample3,filter_views,manual_pagination,Pagination_data,new_pagination_data,Createuser, CreateProduct
from newapp.views import MovieTickets, MovienewTickets
from registration.views import CheckingDetails, CourseDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('service/',service, name='service'),
    path('sample/',sample),
    path('sample1/',sample1),
    path('sample2/',sample2),
    path('sample3/',sample3),
    path('filterviews/', filter_views),
    path('manualpages/', manual_pagination),
    path('paginationdata/',Pagination_data ),
    path('new_pagination/',new_pagination_data),
    path('userdata/',Createuser),
    path("products/", CreateProduct),
    path("user/", CreateProfile),
    path('product/', ProductProfile),
    path('carpro/', Carlist),
    path('movie/', MovieTickets),
    path("mo/", MovienewTickets),
    path("Registration/",CourseDetails),
    path("Registrations/",CheckingDetails)
]




