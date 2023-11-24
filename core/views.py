from django.http import request
from django.shortcuts import HttpResponse, render

from .forms import SignupForm


def home(request: request) -> HttpResponse:
    context: dict = {}

    form = SignupForm(request.POST or None)

    if form.is_valid():
        form.save()

    context['form'] = form

    return render(request=request, template_name="index.html", context=context)
