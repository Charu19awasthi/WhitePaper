from django.shortcuts import render, redirect
from .models import Note
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

# Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the homepage after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def note_list(request):
    notes = Note.objects.filter(user=request.user)  # Filter notes by logged-in user
    return render(request, 'notepad/note_list.html', {'notes': notes})
