from django.shortcuts import render


def simple_view(request):
    data = {"content": "Gfg is the best"}
    return render(request, "learn_docker/index.html", data)
