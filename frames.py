# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import extract_frames

@csrf_exempt  # For simplicity, you can handle CSRF in a better way in production
def extract_frames_view(request):
    if request.method == 'POST' and request.FILES.get('video'):
        video_file = request.FILES['video']
        output_folder = 'output_frames'
        
        # Save the uploaded video file to a temporary location
        with open('temp_video.mp4', 'wb+') as destination:
            for chunk in video_file.chunks():
                destination.write(chunk)
        
        # Call the extract_frames function
        try:
            extract_frames('temp_video.mp4', output_folder)
            response = {'message': 'Frames extraction complete.'}
            status = 200
        except Exception as e:
            response = {'error': str(e)}
            status = 500
        
        # Clean up the temporary video file
        os.remove('temp_video.mp4')
        
        return JsonResponse(response, status=status)
    else:
        return JsonResponse({'error': 'Please upload a video file.'}, status=400)
