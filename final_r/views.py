from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def home(request):
    return render(request,'resume.html')

def thanks(request):
    return render(request,'thanks.html')


def send_email(request):
    name = request.POST.get('name')
    subject = 'RESPONSE FROM '+name
    message = request.POST.get('message')
    from_email = request.POST.get('email')
    if subject and message and from_email:
        try:
            send_mail(subject, message,from_email, ['gopinaath16@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/thanks')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')