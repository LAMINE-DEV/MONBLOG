"""MONBLOG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from AppBlog import views
urlpatterns = [

path('',views.PostView,name='post-view'),
path('detailviewpub/<int:slug>/',views.post_detail,name='detail-view'),
path('categoryview/<str:cat_id>/',views.CategoryView,name='category'),
path('contactme/',views.Contact_view,name='contact-view'),
path('CoursView/',views.CoursView,name="cours-view"),
path('searchdata/',views.Search_view,name='search-view'),
path('userinformation/',views.Userinformation_View,name='userinformation-view'),
path('UpdateProfile/',views.updateProfile,name='update-view'),
path('UpdateProfilePic/',views.UploadImage_view,name='upload-view'),
path('AdminDeletePost/<int:pk>/',views.Deleteview.as_view(),name='admindeletepost-view'),
path('deletepage/<int:pk>/',views.Delete,name='deletepage-view'),
path('passwordupdate/',views.change_password,name='passwordupdate-view')


]