from django.urls import path

from . import views

urlpatterns = [
    #ex: /home/
    path('',views.index,name="index"),
    path('chat',views.chat,name="chat"),
    path('add',views.add,name="add"),
    path('comercos',views.comercos,name="comercos"),
    path('compra_venta',views.compra_venta,name="compra_venta"),
    path('mapa_lloc',views.mapa_lloc,name="mapa_lloc"),
    path('mercat_croat',views.mercat_croat,name="mercat_croat"),
    path('noticies',views.noticies,name="noticies"),
    path('register/',views.register,name="register"),
    path('signin/',views.signin,name="signin"),
    #path('login', views.login , name="singin"),
    path('logout',views.logout_v,name="logout"),
    ]



