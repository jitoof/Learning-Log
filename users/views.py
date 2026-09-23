from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
	"""Regstra un nuevo usuario"""
	if request.method !='POST':
		#Muestra formulario de registro en blanco
		form = UserCreationForm()
	else:
		#Procesa un formulario complementado
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			#Inicia la sesion del usuario y lo redirige a la pagina de inicio.
			login(request, new_user)
			return redirect('learning_logs:index')

	#Muestra un formulario no valido
	context = {'form': form}
	return render(request, 'registration/register.html', context)