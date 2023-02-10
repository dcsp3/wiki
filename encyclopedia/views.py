import random

from django.shortcuts import render, redirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):

    if title in util.list_entries():
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": util.get_entry(title)
        })

    else:
        return render(request, "encyclopedia/error_invalid.html", {
        })

def new_entry(request):
    if request.method == "POST":
        d = request.POST.dict()
        title = d["title"]
        content = d["content"]
        if title not in util.list_entries():
            util.save_entry(title, content)
            return redirect("entry", title)
        else:
            return render(request, "encyclopedia/error_same.html", {
        })
    return render(request, "encyclopedia/new_entry.html")

def random_entry(request):
    entries = util.list_entries()
    return redirect("entry", random.choice(entries))