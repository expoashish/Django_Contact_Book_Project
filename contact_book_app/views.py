from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import ContactDetail
from django.core.mail import BadHeaderError, send_mail
from .forms import CreateUserForm, ContactFormMessage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.db import IntegrityError


def loginPage(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password1']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' wecome {username} !!')
			return redirect('contact_book_app:index')
		else:
			messages.info(request, f'account done not exit plz sign in')
	form = CreateUserForm()
	return render(request, 'contact_book_app/loginpage.html', {'form':form, 'title':'log in'})


def registerPage(request):
	if request.method == 'POST':
	        form = CreateUserForm(request.POST)
	        if form.is_valid():
	            form.save()
	            messages.success(request, f'Your account has been created. You can log in now!')    
	            return redirect('contact_book_app:index')
	else:
		form = CreateUserForm()
	return render(request, 'contact_book_app/registerpage.html', {'form' : form})

@login_required
def logoutUser(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("contact_book_app:index")


def index(request):
	# Contact's of Authenticated User
	if request.user.is_authenticated:
		latest_contact_list = ContactDetail.objects.filter(user=request.user.id).order_by()[:10]
	else:
		latest_contact_list = {}
	return render(request,'contact_book_app/index.html',{'latest_contact_list':latest_contact_list})



# Home Page Send Message to Admin
def index_message(request):
	if request.method == 'POST':
		form = ContactFormMessage(request.POST)
		if form.is_valid():
			p = form.save()
			messages.success(request, 'Contact request submitted successfully.')
			return redirect('contact_book_app:index')
		else:
			messages.error(request, 'Invalid form submission.')
			messages.error(request, form.errors)
	else:
		form = ContactFormMessage()
		return render(request, 'contact_book_app/index.html')



def new_contact( request):
	if request.method == 'POST':
		form = ContactDetailForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			try:
				obj = form.save(commit=False)
				obj.user = request.user
				obj.save()
				messages.success(request, "Successfully created")
				return redirect('contact_book_app:index')
			except IntegrityError as err:
				print('err => ', err)
		else:
			form = ContactDetailForm()
	return render(request,'contact_book_app/add.html',{ 'form':ContactDetailForm() })


def submit_contact(request):
	if request.method =='POST':
		profile = ContactDetailForm(request.POST, request.FILES)
		if profile.is_valid(): 
			profile.save() 
			return redirect('success') 
		return HttpResponseRedirect('contact_book_app/index.html')


def image_upload_view(request):
    if request.method == 'POST':
        profile = ContactDetailForm(request.POST, request.FILES)
        if profile.is_valid(): 
            profile.save() 
            return redirect('success') 
    else: 
        profile = ContactDetailForm() 
    return render(request, 'index.html', {'profile' : profile}) 


def edit_contact(request,id):
	if request.method =='POST':
		selected=ContactDetail.objects.get(id=id)
		profile = ContactDetailForm(request.POST, instance = selected)
		if profile.is_valid(): 
			profile.save()
			messages.success(request, 'Contact successfully updated!!.') 
			return redirect('contact_book_app:index')
		else:
			 messages.error(request, 'Something Went Wrong.')
			 messages.error(request, form.errors)
	else:
		selected=ContactDetail.objects.get(id=id)
		profile = ContactDetailForm(instance=selected)
	return render(request, 'contact_book_app/edit.html',{'profile':profile})


def delete_contact(request,id):
	contact= ContactDetail.objects.get(id=id)
	if request.method == 'POST':
		contact.delete()
		messages.success(request, 'Contact Successfully Deleted!.')
		return redirect('contact_book_app:index')
	else:
		messages.error(request,"Something Went Wrong")


def detail_contact(request,id):
	selected=ContactDetail.objects.get(id=id)
	return render(request, 'contact_book_app/detail.html',{'contacts':selected})


def contact_page( request):
  if request.method == 'POST':
    form = ContactFormMessage(request.POST)
    if form.is_valid():
        p = form.save()
        messages.success(request, 'Contact request submitted successfully.')
        return HttpResponseRedirect('/contactus')
    else:
    	messages.error(request, 'Invalid form submission.')
    	messages.error(request, form.errors)
  else:
  	form = ContactFormMessage()
  	return render(request, 'contact_book_app/contactus.html', {'form': form})


def about_page( request):
	return render(request, 'contact_book_app/aboutus.html')

@login_required
def UserProfile(request):
	return render(request, 'contact_book_app/UserProfile.html')

