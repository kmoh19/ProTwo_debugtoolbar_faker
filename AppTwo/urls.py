from django.conf.urls import url
from AppTwo import views

urlpatterns=[
             url(r'^help/$',views.index,name='index'),
             url(r'^users/$',views.users,name='users'),
             url(r'^userform/$',views.user_form_view,name='users_form_view'),
             ]