from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (CreateView, UpdateView, DeleteView, DetailView,
                                  TemplateView, ListView)
from company.models import CompanyModel, Job
from job_seeker.models import Jobs, UserModel, Skill, Project, Award, Certification
from django.contrib.auth.models import User
from company.forms import CompanyProfileForm, JobForm

# Create your views here.

class CompanyProfileListView(ListView):
    context_object_name = 'companymodel_list'
    template_name = 'company_dashboard.html'

    def get_queryset(self):
        return CompanyModel.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(CompanyProfileListView, self).get_context_data(**kwargs)
        context['job_list'] = Job.objects.filter(user = self.request.user)
        return context

class CompanyProfileView(CreateView):
    form_class = CompanyProfileForm
    model = CompanyModel
    template_name = 'companymodel_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CompanyProfileUpdateView(UpdateView):
    model = CompanyModel
    template_name = 'companymodel_form.html'
    form_class = CompanyProfileForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CompanyProfileDetailView(DetailView):
    context_object_name = 'company_detail'
    model = CompanyModel
    template_name = 'companymodel_detail.html'


#Views related to the Jobs Created

class JobCreateView(CreateView):
    print("My name is Ravi")
    model = Job
    form_class = JobForm
    template_name = 'job_form.html'

    def form_valid(self, form):
        print("My name is Ravi")
        form.instance.user = self.request.user
        return super().form_valid(form)

class JobUpdateView(UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'job_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JobDetailView(DetailView):
    context_object_name = 'job_detail'
    model = Job
    template_name = 'job_detail2.html'

class JobDeleteView(DeleteView):
    model = Job
    template_name = 'job_confirm_delete.html'
    success_url = reverse_lazy('company:company_dashboard')

def CompanyJobsDashboard(request):

    #creating the list for the post tab
    post_list = Job.objects.filter(user = request.user)

    #creating the list for the applicants tab
    company = CompanyModel.objects.get(user = request.user)
    applied_jobs = Jobs.objects.filter(company_user = company)

    applicants = list()

    for applicant in applied_jobs:
        applicant_detail = list()
        user = applicant.user
        skills = []
        user_skills = Skill.objects.filter(user = user)
        for i in user_skills:
            skills.append(i.skill_name)

        # job_detail = applicant.job
        candidate = UserModel.objects.get(user = user)

        applicant_detail.append(candidate)
        applicant_detail.append(applicant)
        applicant_detail.append(skills)

        applicants.append(applicant_detail)

    #creating the list for all candidates tab
    candidates = dict()
    job_seekers = User.objects.filter(first_name__startswith="job_seeker")
    for candidate in job_seekers:
        skills = []
        user = UserModel.objects.get(user = candidate)
        user_skills = Skill.objects.filter(user = candidate)
        for skill in user_skills:
            skills.append(skill)
        candidates[user] = skills

    return render(request, 'company_jobs_dashboard.html', context = {'post_list':post_list, 'applicants':applicants, 'candidates':candidates})


def ShowCandidateDetail(request, candidate_id):
    Jobs.objects.filter(id = candidate_id).update(job_status = "Reviewed")
    job_object = Jobs.objects.get(id = candidate_id)

    user = job_object.user

    user_detail = UserModel.objects.get(user = user)
    skills = Skill.objects.filter(user = user)
    project_list = Project.objects.filter(user = user)
    award_list = Award.objects.filter(user = user)
    certification_list = Certification.objects.filter(user = user)

    hobies = user_detail.hobies
    hobies_list = hobies.split(',')


    extra = user_detail.extra_curriculam
    extra_list = extra.split(',')

    return render(request, 'usermodel_detail.html', context = {'user_detail':user_detail, 'skills':skills, 'project_list':project_list, 'award_list':award_list, 'certification_list':certification_list, 'hobies_list':hobies_list, 'extra_list':extra_list})
    # return redirect('job_seeker:detail', pk=user_object.id)

def Selected(request, job_id):
    Jobs.objects.filter(id = job_id).update(job_status = "Selected")
    return redirect('company:company_jobs_dashboard')

def Rejected(request, job_id):
    Jobs.objects.filter(id = job_id).update(job_status = "Rejected")
    return redirect('company:company_jobs_dashboard')

def AllApplicantsView(request):
    #creating the list for the post tab
    post_list = Job.objects.filter(user = request.user)

    #creating the list for the applicants tab
    company = CompanyModel.objects.get(user = request.user)
    applied_jobs = Jobs.objects.filter(company_user = company)

    applicants = list()

    for applicant in applied_jobs:
        applicant_detail = list()
        user = applicant.user
        skills = []
        user_skills = Skill.objects.filter(user = user)
        for i in user_skills:
            skills.append(i.skill_name)

        # job_detail = applicant.job
        candidate = UserModel.objects.get(user = user)

        applicant_detail.append(candidate)
        applicant_detail.append(applicant)
        applicant_detail.append(skills)

        applicants.append(applicant_detail)

    #creating the list for all candidates tab
    candidates = dict()
    job_seekers = User.objects.filter(first_name__startswith="job_seeker")
    for candidate in job_seekers:
        skills = []
        user = UserModel.objects.get(user = candidate)
        user_skills = Skill.objects.filter(user = candidate)
        for skill in user_skills:
            skills.append(skill)
        candidates[user] = skills

    return render(request, 'company_jobs_dashboard1.html', context = {'post_list':post_list, 'applicants':applicants, 'candidates':candidates})

def AllCandidatesView(request):
    post_list = Job.objects.filter(user = request.user)

    #creating the list for the applicants tab
    company = CompanyModel.objects.get(user = request.user)
    applied_jobs = Jobs.objects.filter(company_user = company)

    applicants = list()

    for applicant in applied_jobs:
        applicant_detail = list()
        user = applicant.user
        skills = []
        user_skills = Skill.objects.filter(user = user)
        for i in user_skills:
            skills.append(i.skill_name)

        # job_detail = applicant.job
        candidate = UserModel.objects.get(user = user)

        applicant_detail.append(candidate)
        applicant_detail.append(applicant)
        applicant_detail.append(skills)

        applicants.append(applicant_detail)

    #creating the list for all candidates tab
    candidates = dict()
    job_seekers = User.objects.filter(first_name__startswith="job_seeker")
    for candidate in job_seekers:
        skills = []
        user = UserModel.objects.get(user = candidate)
        user_skills = Skill.objects.filter(user = candidate)
        for skill in user_skills:
            skills.append(skill)
        candidates[user] = skills

    return render(request, 'company_jobs_dashboard2.html', context = {'post_list':post_list, 'applicants':applicants, 'candidates':candidates})

def CandidateDisplay(request, key_id):
    user_model = UserModel.objects.get(id = key_id)
    user = user_model.user

    user_detail = UserModel.objects.get(user = user)
    skills = Skill.objects.filter(user = user)
    project_list = Project.objects.filter(user = user)
    award_list = Award.objects.filter(user = user)
    certification_list = Certification.objects.filter(user = user)

    hobies = user_detail.hobies
    hobies_list = hobies.split(',')


    extra = user_detail.extra_curriculam
    extra_list = extra.split(',')

    return render(request, 'usermodel_detail.html', context = {'user_detail':user_detail, 'skills':skills, 'project_list':project_list, 'award_list':award_list, 'certification_list':certification_list, 'hobies_list':hobies_list, 'extra_list':extra_list})

def GetResume(request, user_id):

    user = User.objects.get(id = user_id)
    user_data = UserModel.objects.get(user = user)
    project_list = Project.objects.filter(user = user)
    skill_list = Skill.objects.filter(user = user)
    award_list = Award.objects.filter(user = user)
    certification_list = Certification.objects.filter(user = user)

    return render(request, 'resumes/res1.html', context = {'user_data': user_data,'project_list': project_list,'skill_list':skill_list,'award_list':award_list,'certification_list':certification_list})


class AnalysisPage(TemplateView):
    template_name = 'company_analysis_page.html'

    def get_context_data(self, **kwargs):
        context = super(AnalysisPage, self).get_context_data(**kwargs)

        user = self.request.user
        company_model = CompanyModel.objects.get(user = user)
        jobs = Jobs.objects.filter(company_user = company_model)

        total = len(jobs)
        selected = 0
        rejected = 0
        reviewed = 0
        for job in jobs:
            if(job.job_status == "Reviewed"):
                reviewed += 1
            elif(job.job_status == "Selected"):
                selected += 1
            elif(job.job_status == "Rejected"):
                rejected += 1

        print("selected {}, rejected {}, reviewed {}".format(selected, rejected, reviewed))
        selected = (selected/total)*100
        rejected = (rejected/total)*100
        reviewed = (reviewed/total)*100

        print("selected {}, rejected {}, reviewed {}".format(selected, rejected, reviewed))
        context['total'] = int(total)
        context['selected'] = int(selected)
        context['rejected'] = int(rejected)
        context['reviewed'] = int(reviewed)

        # for the second progressbar

        job_prof = {
            'Business Development (Sales)':0,
            'Web Development':0,'Graphic Design':0,
            'Content Writing':0,'Operations':0,'Mobile App Development':0,
            'Social Media Marketing':0,
            'Marketing':0,'Digital Marketing':0,
             'Human Resources (HR)':0,'Law/ Legal':0,'Campus Ambassador':0
            }

        all_jobs = Job.objects.all()
        for one in all_jobs:
            job_prof[one.job_profile] += 1

        context['job_prof'] = job_prof
        print(job_prof)

        return context
