from django.shortcuts import render

def UserCreateView(request):
    return render(request, 'create_user.html')