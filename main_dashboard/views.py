# main_dashboard/views.py
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def dashboard(request):
    # Since dashboard.html is directly under main_dashboard/templates,
    # we reference it simply as "dashboard.html"
    return render(request, "index.html")




@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        # Check if the file is provided in the request
        if 'file' not in request.FILES:
            return JsonResponse({'success': False, 'error': 'No file provided.'})
        
        # Get the file from request.FILES. No conversion is done—the file is used as is.
        uploaded_file = request.FILES['file']
        
        # Save the file using Django's FileSystemStorage
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)
        
        return JsonResponse({'success': True, 'file_url': file_url})
    
    return JsonResponse({'success': False, 'error': 'Invalid request method.'}) 