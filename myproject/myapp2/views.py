from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login user and redirect to a success page
            login(request, user)
            # Change 'home' to the name of your home page URL
            return redirect('home')
        else:
            # Invalid login
            return render(request, 'login.html', {'error': 'Invalid username or password.'})

    return render(request, 'login.html')
