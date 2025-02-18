from django.shortcuts import render

# Create your views here.
def login_page(request):
    return render(request, 'index_login.html')

