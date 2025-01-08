from django.urls import path
from app import views

urlpatterns=[
	path('',views.home,name='home'),
	path('about/',views.home,name='about'),
	path('contact/',views.contact,name='contact'),
	path('faq/',views.faq,name='faq'),
	path('feature/',views.feature,name='feature'),
	path('index/',views.index,name='index'),
	path('project/',views.project,name='project'),
	path('service',views.service,name='service'),
	path('team/',views.team,name='team'),
	path('testimonial/',views.testimonial,name='testimonial'),
	path('404page/',views.page404,name='404page'),
	path('addpost/',views.add_post,name='addpost'),
	path('updatepost/<int:id>',views.update_post,name='updatepost'),
	path('deletepost/<int:id>',views.delete_post,name='deletepost'),
	path('dashboard/',views.dashboard,name='dashboard'),
	
	path('logout/',views.user_logout,name='logout'),
	path('signup/',views.sign_up,name='signup'),
	path('login/',views.user_login,name='login'),


]