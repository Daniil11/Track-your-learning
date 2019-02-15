"""learning_logs!!!
"""
from django.urls import path
from . import views
app_name = 'learning_logs'
urlpatterns = [
	# Домашняя страница
	path('', views.index, name='index'),
	path('topics/',views.topics,name='topics'),
	#Ну хз если честно
	path('topics/(<topic_id>)',views.topic,name='topic'),
	path('new_topic',views.new_topic,name='new_topic'),
]