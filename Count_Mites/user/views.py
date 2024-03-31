from django.contrib import messages
from django.contrib.auth import login
from django.db import IntegrityError
from django.shortcuts import render, redirect

from user.forms import SignUpForm


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
