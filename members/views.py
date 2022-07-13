from email.headerregistry import Address
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members
from django.contrib import messages

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('myfirst.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def enroll(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('first.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def adminpage(request):
  template = loader.get_template('adminlogin.html')
  return HttpResponse(template.render({}, request))

def adminlogin(request):
  l = request.POST['pass']
  if (l==""):
    messages.info(request, "Please Enter ACCESSED PASSCODE!")
    return HttpResponseRedirect(reverse('adminpage'))
  elif (l=="jkt"):
    messages.info(request, 'ACCESS PASSED!')
    return HttpResponseRedirect(reverse('index'))
  else:
    messages.info(request, 'ACCESS DENIED!')
  return HttpResponseRedirect(reverse('adminpage'))
  
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))
  
def addrecord(request):
  a = request.POST['first']
  b = request.POST['last']
  c = request.POST['fathername']
  d=request.POST['age']
  e=request.POST['address']
  f=request.POST['education']
  g=request.POST['hobby']
  h=request.POST['email']
  if (a=="" or b=="" or c=="" or d=="" or e=="" or f=="" or g=="" or h==""):
    messages.info(request, "All fields are required!")
    return HttpResponseRedirect(reverse('add'))

  else:
    member = Members(firstname=a, lastname=b,fathername=c,age=d,address=e,education=f,hobby=g,email=h)
    member.save()
    messages.info(request, 'You have successfully enrolled!')
    return HttpResponseRedirect(reverse('enroll')) 

    

  

def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))


def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  fathername=request.POST['fathername']
  age=request.POST['age']
  address=request.POST['address']
  email=request.POST['email']
  education=request.POST['education']
  hobby=request.POST['hobby']


  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.fathername = fathername
  member.age = age
  member.address = address
  member.email = email
  member.education = education
  member.hobby = hobby
  
  member.save()
  return HttpResponseRedirect(reverse('index'))