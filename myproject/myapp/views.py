from django.shortcuts import render, redirect
from .models import User


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        # Basic validation - you may want to add more robust validation
        if not (username and password and email):
            return render(request, 'signup.html', {'error': 'All fields are required. Please try again.'})

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already taken. Please choose another.'})

        # If everything is valid, create the user
        user = User.objects.create(
            username=username, password=password, email=email)
        return render(request, 'signup_success.html', {'username': username})

    return render(request, 'signup.html')
