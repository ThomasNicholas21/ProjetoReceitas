from django.shortcuts import render, redirect
from django.http import Http404

from .forms import RegisterForm


def register_view(request):
    post_data = request.session.get("post_data")
    form = RegisterForm(post_data)
    context = {"form": form,}
    return render(request, "authors/pages/register.html", context)


def register_create(request):
    if not request.POST:
        raise Http404()

    post_data = request.POST
    request.session["post_data"] = post_data

    form = RegisterForm(post_data)

    return redirect("authors:register")
