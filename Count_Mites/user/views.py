from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.db import IntegrityError
from django.shortcuts import render, redirect

from user.forms import SignUpForm, LoginForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()  # Save the user to the database
                print("User saved successfully:", user)
                login(request, user)  # Log in the user after successful signup
                return redirect('signup_success')  # Redirect to signup success page
            except IntegrityError:
                form.add_error('username', 'This username is already taken. Please choose a different one.')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})


def signup_success(request):
    return render(request, 'video/upload_video.html')


def login_view(request):
    error_message = None
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # return redirect('login_success')
                return redirect('user_uploaded_videos')

        # messages.error(request, 'Invalid username or password. Please try again.')
        error_message = 'Invalid username or password'
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form, 'error_message': error_message})


def login_success(request):
    return render(request, 'video/uploaded_videos.html')

