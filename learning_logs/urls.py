"""Define patrones de URL para learning_logs"""
from django.urls import path
from . import views
app_name = 'learning_logs'
urlpatterns = [
	#Pagina de inicio
	path('',views.index, name='index'),
	#Pagina que muestra todos los temas
	path('topics/',views.topics,name='topics'),
	#Pagina de detalles sobre un tema individual
	path('topics/<int:topic_id>/', views.topic, name='topic'),
	#Pagina para añadir un tema nuevo
	path('new_topic/', views.new_topic, name='new_topic'),
	#Pagina para añadir una nueva entrada
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
	#Pagina para editar una entrada
	path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
	#Pagina para temas publicos.
	path('public/', views.public_topics, name='public_topics'),
	#Pagina para borrar una entrada
	path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
	#Pagina para borrar un tema
	path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic')

]

