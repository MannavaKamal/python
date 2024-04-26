"""
URL configuration for smsproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('index3', views.index3, name="index3"),
    path('bookedrooms',views.bookedrooms,name="bookedrooms"),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contact',views.contactfunction,name='contact'),
    path('userSignup',views.userSignup,name='userSignup'),
    path('userLogin',views.userLogin,name='userLogin'),
    path('user0',views.user0,name='user0'),
    path('user1',views.user1,name='user1'),
    path('user2',views.user2,name='user2'),
    path('adminDetails',views.adminDetails,name='adminDetails'),
    path('adminDetailsId',views.adminDetailsId,name='adminDetailsId'),
    path('Admin1',views.Admin1,name='Admin1'),
    path('roomEntry',views.roomEntry,name='roomEntry'),
    path('Admin2',views.Admin2,name='Admin2'),
    path('deleteAdminrooms',views.deleteAdminRooms,name='deleteAdminRooms'),
    path('Admin3', views.Admin3, name='Admin3'),
    path('userBookedId',views.userBookedId,name='userBookedId'),
    path('userDetails',views.userDetails,name='userDetails'),
    path('deleteLiveRoom',views.deleteLiveRoom,name='deleteLiveRoom'),
    path('bookingProcess',views.bookingProcess,name='bookingProcess'),
    path('roomConformed',views.roomConformed,name='roomConformed'),
    path('hotelSelect',views.hotelSelect,name='hotelSelect'),
    path('adminOrUserChoice',views.adminOrUserChoice,name='adminOrUserChoice'),
    path('defaultNavbar', views.defaultNavbar, name='defaultNavbar'),
    path('defaultNavbar', views.defaultNavbar, name='defaultNavbar'),
    path('AdminRoomsNotAvailable', views.AdminRoomsNotAvailable, name='AdminRoomsNotAvailable'),
    path('AdminLiveRoomsNotAvailable', views.AdminLiveRoomsNotAvailable, name='AdminLiveRoomsNotAvailable'),
    path('AdminsNotAvailable', views.AdminsNotAvailable, name='AdminsNotAvailable'),
    path('RoomsBookedNotAvailable', views.RoomsBookedNotAvailable, name='RoomsBookedNotAvailable'),
    path('RoomsNotAvailable', views.RoomsNotAvailable, name='RoomsNotAvailable'),
    #admin pages
    path('adminSignup',views.adminSignup,name='adminSignup'),
    path('adminLogin',views.adminLogin,name='adminLogin'),

    #path("",include("studentapp.urls")),
    #path("",include("adminapp.urls")),

]
if settings.DEBUG:
    print(settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)