from django.shortcuts import render
from django.views.generic import View, CreateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from registration.forms import UserForm
from django.contrib.auth.models import User
from django.contrib import messages
from company.models import CompanyModel, Job
from job_seeker.models import UserModel
# Create your views here.

def HomePage(request):
    companies = CompanyModel.objects.all()
    users = UserModel.objects.all()
    jobs = Job.objects.all()

    c_number = len(companies)
    u_number = len(users)
    j_number = len(jobs)

    return render(request, 'index.html', context = {'c_number':c_number, 'u_number':u_number, 'j_number':j_number})

def UserDashBoard(request):
    return render(request, "user_index.html", {})

def CompanyDashBoard(request):
    return render(request, "company_index.html", {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(HomePage))

def cancel_registration(request):
    return HttpResponseRedirect(reverse(HomePage))

class UserLogin(View):
    template_name = "user_login.html"

    def get(self, request):
        return render(request, self.template_name, context = {})

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username = username, password = password)
        if(user):
            if(user.is_active):
                login(request, user)
                # return HttpResponseRedirect(reverse(UserDashBoard))
                return HttpResponseRedirect(reverse(HomePage))
            else:
                return HttpResponse("User not active")
        else:
            return render(request, "user_login.html", context = {"message":"invalid details!"})


class CompanyLogin(View):
    template_name = "company_login.html"
    def get(self, request):
        return render(request, self.template_name, context = {})

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username = username, password = password)
        if(user):
            if(user.is_active):
                login(request, user)
                # return HttpResponseRedirect(reverse(CompanyDashBoard))
                return HttpResponseRedirect(reverse(HomePage))
            else:
                return HttpResponse("User not active")
        else:
            return render(request, "company_login.html", context = {"message":"invalid details!"})

def UserSignUp(request):
    if(request.method == "POST"):
        form1 = UserForm(request.POST)
        if(form1.is_valid()):
            username = form1.cleaned_data['username']
            email = form1.cleaned_data['email']
            password = form1.cleaned_data['password']
            retype_password = form1.cleaned_data['confirm_password']
            User.objects.create_user(username = username, email = email, password = password, first_name = "job_seeker")
            messages.success(request, 'user registration successful')
            usr = authenticate(username = username, password = password)
            login(request, usr)
            return HttpResponseRedirect(reverse(HomePage))
    else:
        form1 = UserForm()
    return render(request, 'user_signup.html', {'reg_form':form1})


def CompanySignUp(request):
    if(request.method == "POST"):
        form1 = UserForm(request.POST)
        if(form1.is_valid()):
            username = form1.cleaned_data['username']
            email = form1.cleaned_data['email']
            password = form1.cleaned_data['password']
            retype_password = form1.cleaned_data['confirm_password']
            User.objects.create_user(username = username, email = email, password = password, first_name = "company")
            messages.success(request, 'user registration successful')
            usr = authenticate(username = username, password = password)
            login(request, usr)
            return HttpResponseRedirect(reverse(HomePage))
    else:
        form1 = UserForm()
    return render(request, 'company_signup.html', {'reg_form':form1})
