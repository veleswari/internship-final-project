from django.shortcuts import render,redirect
from django.http import HttpResponse
from Hospital.forms import UsgForm,DoList,PoList,ApoList
from Hospital.models import Doctor,Patient,Appoinment
from django.contrib.auth.decorators import login_required 

# Create your views here.
def home(request):
	return render(request,'app/home.html')



def usrreg(request):
	if request.method == "POST":
		d = UsgForm(request.POST)
		if d.is_valid():
			d.save()
			return redirect('/login')
	d = UsgForm()
	return render(request,'app/usrregister.html',{'t':d})


@login_required
def doclist(request):
	y = Doctor.objects.all()
	if request.method == "POST":
		t = DoList(request.POST)
		if t.is_valid():
			t.save()
			return redirect('/adlist')
	t = DoList()
	return render(request,'app/doclist.html',{'q':t,'a':y})
@login_required
def docupd(request,m):
	k = Doctor.objects.get(id=m)
	if request.method == "POST":
		e = DoList(request.POST,instance=k)
		if e.is_valid():
			e.save()
			return redirect('/docvw')
	e = DoList(instance=k)
	return render(request,'app/doctupdate.html',{'x':e})
@login_required
def docdlt(request,n):
	v = Doctor.objects.get(id=n)
	if request.method == "POST":
		v.delete()
		return redirect('/docvw')
	return render(request,'app/doctdelete.html',{'q':v})
@login_required
def docview(request):
	l = Doctor.objects.all()
	return render(request,'app/docview.html',{'s':l})



@login_required
def palist(request):
	x = Patient.objects.all()
	if request.method == "POST":
		v = PoList(request.POST)
		if v.is_valid():
			v.save()
			return redirect('/pdlist')
	v = PoList()
	return render(request,'app/palist.html',{'k':v,'l':x})
@login_required
def paview(request):
	l = Patient.objects.all()
	return render(request,'app/paview.html',{'s':l})

@login_required
def patupd(request,m):
	k = Patient.objects.get(id=m)
	if request.method == "POST":
		e = PoList(request.POST,instance=k)
		if e.is_valid():
			e.save()
			return redirect('/pavw')
	e = PoList(instance=k)
	return render(request,'app/patupdate.html',{'x':e})

@login_required
def patdlt(request,n):
	v = Patient.objects.get(id=n)
	if request.method == "POST":
		v.delete()
		return redirect('/docvw')
	return render(request,'app/patdelete.html',{'q':v})


@login_required
def aplist(request):
	x = Appoinment.objects.all()
	if request.method == "POST":
		v = ApoList(request.POST)
		if v.is_valid():
			v.save()
			return redirect('/aplist')
	v = ApoList()
	return render(request,'app/aplist.html',{'k':v,'l':x})

@login_required
def apview(request):
	l = Appoinment.objects.all()
	return render(request,'app/apview.html',{'s':l})

@login_required
def aptupd(request,m):
	k = Appoinment.objects.get(id=m)
	if request.method == "POST":
		e = ApoList(request.POST,instance=k)
		if e.is_valid():
			e.save()
			return redirect('/apvw')
	e = ApoList(instance=k)
	return render(request,'app/aptupdate.html',{'x':e})

@login_required
def aptdlt(request,n):
	v = Appoinment.objects.get(id=n)
	if request.method == "POST":
		v.delete()
		return redirect('/apvw')
	return render(request,'app/aptdelete.html',{'q':v})
