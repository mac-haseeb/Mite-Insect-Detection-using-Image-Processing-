from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            # Associate the uploaded video with the currently logged-in user
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            return redirect('user_uploaded_videos')  # Redirect to a page showing the list of uploaded videos
    else:
        form = VideoForm()

    print(form)
    return render(request, 'video/upload_video.html', {'form': form})