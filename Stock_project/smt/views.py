from django.shortcuts import render, redirect
from .forms import forr, Tips_Form
from .models import trails
# Create your views here.


def home(request):
    form = forr()
    tips_form = Tips_Form()
    if request.method == 'POST':
        form = forr(request.POST)
        if form.is_valid():
            form.save()
        if 'email' in request.POST: 
            tips_home = Tips_Form(request.POST)
            if tips_home.is_valid():
                tips_home.save()
        return redirect('home')
    return render(request, 'index.html', {'form': form, 'tips_form':tips_form})

