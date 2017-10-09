from django.shortcuts import render

# retrieve
# GET -- template home.html
def home(request):
    return render(request, "home.html", {})