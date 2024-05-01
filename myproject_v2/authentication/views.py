from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
import json

User = get_user_model()


def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        if not username or not password:
            return JsonResponse({'error': 'Username and password are required'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username is already taken'}, status=400)

        user = User.objects.create_user(
            username=username, password=password, email=email)
        return JsonResponse({'success': 'User created successfully'})

    return JsonResponse({'error': 'Method not allowed'}, status=405)


def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            # User is authenticated, you can perform further actions here
            return JsonResponse({'success': 'Login successful'})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)

    return JsonResponse({'error': 'Method not allowed'}, status=405)
