from django.db.models.base import Model
from django.http.response import HttpResponse
from Registerapp.models import Registerform
from django.shortcuts import redirect, render
from django.http import request
from Registerapp.forms import ContactForm

def Renter_details(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/view_reg')
    return render(request, 'registerapp/Render_form.html', {'form': form})
    
def view(request):
    Model = Registerform.objects.all()
    return render(request, 'registerapp/index.html', {'model': Model})

def deletion(request, id):
    Model = Registerform.objects.get(id=id)
    Model.delete()
    return redirect('/view_reg')
