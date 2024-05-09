from django.shortcuts import render,redirect
from django.conf import settings
from .models import *

# Create your views here.
def index(r):
    obj = person.objects.all()
    return render(r,'index.html',{'obj':obj})

def addemployee(r):
    if r.method=='POST':
        n1=r.POST.get('firstname')
        n2=r.POST.get('lastname')
        a=r.POST.get('address')
        e=r.POST.get('email')
        p=r.POST.get('phonenumber')
        dob=r.POST.get('dateofbirth')
        q=r.POST.get('qualifications')
        g=r.POST.get('gender')
        m=r.POST.get('maritalstatus')
        i=r.POST.get('interests')
        obj = person.objects.create(firstname = n1,
                                    lastname = n2,
                                    address = a,
                                    email = e,
                                    phonenumber = p,
                                    dateofbirth = dob,
                                    qualifications = q,
                                    gender = g,
                                    maritalstatus = m,
                                    interests = i,)
        obj.save()
        return redirect(index)
    return render(r,'addemployee.html')

def editemployee(r,wal):
    obj = person.objects.filter(id=wal).first()
    return render(r,'editemployee.html',{'obj':obj})

def editemployee2(r,wal):
    obj = person.objects.get(id=wal)
    if r.method=='POST':
        obj.firstname=r.POST.get('firstname')
        obj.lastname=r.POST.get('lastname')
        obj.address=r.POST.get('address')
        obj.email=r.POST.get('email')
        obj.phonenumber=r.POST.get('phonenumber')
        obj.dateofbirth=r.POST.get('dateofbirth')
        obj.qualifications=r.POST.get('qualifications')
        obj.gender=r.POST.get('gender')
        obj.maritalstatus=r.POST.get('maritalstatus')
        obj.interests=r.POST.get('interests')
        obj.save()
        return redirect(index)
    return render(r,'editemployee.html',{'obj':obj})

def deleteemployee(r,wal):
    obj = person.objects.filter(id=wal).first()
    obj.delete()
    return redirect(index)


