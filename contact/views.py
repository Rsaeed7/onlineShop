from django.shortcuts import render,redirect
from .models import ContactUs
from django.contrib import messages

# Create your views here.
def contactUs(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactUs.objects.create(name=name, email=email, message=message)
        messages.success(request, 'Thank you! you have successfully sent your message!')
        return redirect('contact:contactus')

    return render(request,'core/countact.html')
