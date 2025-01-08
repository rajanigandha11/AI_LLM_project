from django.shortcuts import render,HttpResponse,redirect
from .models import Blog
from .forms import BlogForm,SignUpForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect


def home(request):
	return render(request,'app/index.html')

def contact(request):
	return render(request,'app/contact.html')

def faq(request):
	return render(request,'app/faq.html')

def feature(request):
	return render(request,'app/feature.html')

def index(request):
	return render(request,'app/index.html')

def project(request):
	return render(request,'app/project.html')

def service(request):
	return render(request,'app/service.html')

def team(request):
	return render(request,'app/team.html')

def testimonial(request):
	return render(request,'app/testimonial.html')

def page404(request):
	return render(request,'app/404.html')

def about(request):
	return render(request,'app/about.html')



def dashboard(request):
	posts=Blog.objects.all()
	return render(request,'app/dashboard.html',{'posts':posts})
	

def add_post(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			fm=BlogForm(request.POST)
			if fm.is_valid():
				title=fm.cleaned_data['title']
				discription=fm.cleaned_data['discription']
				author=fm.cleaned_data['author']
				pst=Blog(title=title,discription=discription,author=author)
				pst.save()
				fm=BlogForm()
		else:
			fm=BlogForm()
		return render(request,'app/add_post.html',{'form':fm})
	else:
		return redirect('/login/')


def update_post(request,id):
	if request.user.is_authenticated:
		if request.method=='POST':
			pi=Blog.objects.get(pk=id)
			fm=BlogForm(request=request.POST,instance=pi)
			if fm.is_valid():
				fm.save()
		else:
			pi=Blog.objects.get(pk=id)
			fm=BlogForm(instance=pi)
		return render(request,'app/updatepost.html',{'form':fm})
	else:
		return redirect('/login/')


def delete_post(request,id):
	if request.user.is_authenticated:
		if request.method=='POST':
			pi=Blog.objects.get(pk=id)
			pi.delete()
		return HttpResponse('/addpost/')
	return redirect('/login/')


def sign_up(request):
	if request.method == 'POST':
		form=SignUpForm(request.POST)
		if form.is_valid():
			messages.success(request,'Congratulations !! You have Become an Author !')
			form.save()
			
	else:
		form=SignUpForm()
	return render(request,'app/signup.html',{'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Congratulations !! logged in successfully !')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'app/login.html', {'form': form})
    else:
        return redirect('/dashboard/') 
		


def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')


