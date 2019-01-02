from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "link_items":("aa","bb")
    }
    return render(request, "category_x/index.html", context)


def static_render(request, template_name):
    context = {"template_name": template_name}
    return render(request,
                  "category_x/{}.html".format(template_name),
                  context)
