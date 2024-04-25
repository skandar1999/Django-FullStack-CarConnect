from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


def profile_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('login')  # Redirect to the login page after logout

    return render(request, 'views/profile.html')

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'You are now logged in as {username}.')
                return redirect('/')  
            else:
                # Display error message for invalid credentials
                messages.error(request, 'Invalid username or password.')
        else:
            # Display error message for invalid form submission
            messages.error(request, 'Invalid form submission.')
    else:  # GET request
        login_form = AuthenticationForm()

    return render(request, 'views/login.html', {'login_form': login_form})


