from django.urls import path

from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('about.html',views.about, name='about'),
    path('Decision-Factors.html',views.Decision,name='Decision'),
    path('report.html', views.report, name='report'),
    path('index.html', views.index, name='index'),
    path('signup.html', views.signup, name='signup'),

]