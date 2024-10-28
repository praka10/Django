from django.shortcuts import render

# Create your views here.
# users/views.py
from django.shortcuts import render
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Retrieve the username from the form
            username = form.cleaned_data['username']
            # Pass the username to the success template
            return render(request, 'registration_success.html', {'username': username})
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
