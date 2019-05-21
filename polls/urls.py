from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('test/', views.test, name='test'),
	path('template/', views.template, name='template'),
	path('post/message/', views.post_message, name='post_message'),
	path('<int:question_id>/vote/', views.vote, name='vote'),
]
