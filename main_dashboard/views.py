# main_dashboard/views.py
from django.shortcuts import render

def dashboard(request):
    # Since dashboard.html is directly under main_dashboard/templates,
    # we reference it simply as "dashboard.html"
    return render(request, "index.html")