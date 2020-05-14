from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('test/<pk>',views.nextQues,name='test'),
    path('save/<pk>',views.saveSelected,name='save'),
    path('result/',views.result,name='result'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.signin,name='login'),
    path('logout/', views.signout, name='logout'),
    path('profile/', views.userProfile, name='profile'),
    path('update/', views.updateProfile, name='update'),
    path('updatePic/', views.changePic, name = 'changePic'),
]