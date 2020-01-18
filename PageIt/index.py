from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Page
import random


def index(request) -> HttpResponse:
    unique = False
    page_id = None
    while not unique:
        page_id = generate_page_id()
        unique = not page_exist(page_id)

    new_page = Page(id=page_id)
    new_page.save()

    return render(request, "index.html", {"data": {"new_id": page_id}})


def generate_page_id() -> str:
    options = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"
    s = ""
    for _ in range(8):
        c = options[random.randrange(0, len(options))]
        s += c
    return s


def load(request, page_id) -> HttpResponse:
    return render(request, "index.html", {"data": {"id": page_id}})


def data_load(request, page_id) -> HttpResponse:
    try:
        data = Page.objects.get(id=page_id).data
        return HttpResponse(data)
    except Page.DoesNotExist:
        return HttpResponseNotFound()


def save(request) -> HttpResponse:
    page = request.POST["page"][1:]
    data = request.POST["doc"]
    Page.objects.filter(id=page).update(data=data)
    return HttpResponse("")


def page_exist(id: str) -> bool:
    try:
        Page.objects.get(id=id)
        return True
    except Page.DoesNotExist:
        return False
