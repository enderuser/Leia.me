from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def DivulgarCreateView(request):
    if request.method == "GET":
        return render(request, 'create_livro.html')

def DivulgarUpdateView(request):
    pass

def DivulgarListView(request):
    pass

