
from django.urls import path,include
from . import views
from .views import authView, home,subscribe_view,payment_success,payment_fail,publication1,unit21,exam12,allsub,allunit,allexam
app_name = 'epathsala'
from .views import upload_units,upload_exam,views_contact,views_exam,del_units,edit_units,del_comments,del_exam,edit_exam,user_view
urlpatterns = [
    # baira ko 
    path('',views.index,name='index'),
    path('index',views.index),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", authView, name="authView"),

    # vitra ko
    path("home", home, name="home"),
    path('contact', views.contact),
    path('about', views.about),
    path('term', views.term),
    path('privacy', views.privacy),



    path('subscribe/', subscribe_view, name='subscribe'),
    path('payment-success/', payment_success, name='payment_success'),
    path('payment-fail/', payment_fail, name='payment_fail'),

    #main content
    path('for12/<major>/', views.for12, name='for12'),
    path('subject/<id>/<tpye>/', views.subject1, name='subject'),
    path('subject12/<id>/<tpye>/<major>/', views.subject12, name='subject12'),
    path('publication/<sub>/<id>/<tpye>/<major>', publication1, name='publication'),
    path('unit/<pub>/<sub>/<id>/<tpye>/<major>', unit21, name='unit21'),
    path('unit2/<uid>/<pub>/<sub>/<id>/', views.unit22, name='unit2'),
    path('major/', views.major, name='major'),
    path('exam2/<eid>/<pub>/<sub>/<id>/', exam12, name='exam'),
    path('allsub/<pub>/<id>/<major>/', allsub, name='allsub'),
    path('allunit/<sub>/<pub>/<id>/', allunit, name='allunit'),
    path('allexam/<id>/<major>/', allexam, name='allexam'),
    path('user_view/', user_view, name='user_view'),
    



    #staff urls

    path('upload_unit/', upload_units, name='upload_units'),
    path('upload_exam/', upload_exam, name='upload_exam'),
    path('views_contact/', views_contact, name='views_contact'),
    path('view_exam/', views_exam, name='views_exam'),
    path('del_unit/<id>', del_units, name='del_unit'),
    path('edit_unit/<id>', edit_units, name='edit_unit'),
    path('del_comments/<id>', del_comments, name='del_comments'),
    path('del_exam/<id>', del_exam, name='del_exam'),
    path('edit_exam/<id>', edit_exam, name='edit_exam'),








]