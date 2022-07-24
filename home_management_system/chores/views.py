from django.shortcuts import render
from .models import Chore
def index(request):
    chores = Chore.objects.all()
    context = {"Chores": chores}
    return render(request, "chores/index.html", context)


# Create your views here.
