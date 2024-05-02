from django.shortcuts import render

def EmprestarListView(request):
    if request.method == "GET":
        return render(request, 'emprestar_list.html')