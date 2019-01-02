from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"yes": 0}
    return render(request, "category_x/index.html", context)