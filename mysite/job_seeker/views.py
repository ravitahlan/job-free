from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (CreateView, UpdateView, DeleteView,
                                 TemplateView, DetailView, ListView)
from job_seeker.forms import (UserModelForm, ProjectForm, SkillForm, AwardForm,
                              CertificationForm)
from job_seeker.models import UserModel, Project, Award, Skill, Certification, Jobs
from company.models import Job,CompanyModel


# from urllib import request

class Res1(TemplateView):
    template_name = 'resumes/res1.html'

    def get_context_data(self, **kwargs):
        context = super(Res1, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['user_data'] = UserModel.objects.get(user = self.request.user)
        context['project_list'] = Project.objects.filter(user = self.request.user)
        context['skill_list'] = Skill.objects.filter(user = self.request.user)
        context['award_list'] = Award.objects.filter(user = self.request.user)
        context['certification_list'] = Certification.objects.filter(user = self.request.user)
        return context

class Res1(TemplateView):
    template_name = 'resumes/res1.html'

    def get_context_data(self, **kwargs):
        context = super(Res1, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['user_data'] = UserModel.objects.get(user = self.request.user)
        context['project_list'] = Project.objects.filter(user = self.request.user)
        context['skill_list'] = Skill.objects.filter(user = self.request.user)
        context['award_list'] = Award.objects.filter(user = self.request.user)
        context['certification_list'] = Certification.objects.filter(user = self.request.user)
        return context

class Res2(TemplateView):
    template_name = 'resumes/res2.html'

    def get_context_data(self, **kwargs):
        context = super(Res2, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['user_data'] = UserModel.objects.get(user = self.request.user)
        context['project_list'] = Project.objects.filter(user = self.request.user)
        context['skill_list'] = Skill.objects.filter(user = self.request.user)
        context['award_list'] = Award.objects.filter(user = self.request.user)
        context['certification_list'] = Certification.objects.filter(user = self.request.user)
        return context

class Res3(TemplateView):
    template_name = 'resumes/res3.html'

    def get_context_data(self, **kwargs):
        context = super(Res3, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['user_data'] = UserModel.objects.get(user = self.request.user)
        context['project_list'] = Project.objects.filter(user = self.request.user)
        context['skill_list'] = Skill.objects.filter(user = self.request.user)
        context['award_list'] = Award.objects.filter(user = self.request.user)
        context['certification_list'] = Certification.objects.filter(user = self.request.user)
        return context

class Res4(TemplateView):
    template_name = 'resumes/res4.html'

    def get_context_data(self, **kwargs):
        context = super(Res4, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['user_data'] = UserModel.objects.get(user = self.request.user)
        context['project_list'] = Project.objects.filter(user = self.request.user)
        context['skill_list'] = Skill.objects.filter(user = self.request.user)
        context['award_list'] = Award.objects.filter(user = self.request.user)
        context['certification_list'] = Certification.objects.filter(user = self.request.user)
        return context


class Res5(TemplateView):
    template_name = 'resumes/res5.html'

    def get_context_data(self, **kwargs):
        context = super(Res5, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['user_data'] = UserModel.objects.get(user = self.request.user)
        context['project_list'] = Project.objects.filter(user = self.request.user)
        context['skill_list'] = Skill.objects.filter(user = self.request.user)
        context['award_list'] = Award.objects.filter(user = self.request.user)
        context['certification_list'] = Certification.objects.filter(user = self.request.user)
        return context

# User's personal details related classes

class UserModelList(ListView):
    context_object_name = 'user_models'
    # model = UserModel
    template_name = 'usermodel_list.html'

    def get_queryset(self):
        return UserModel.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(UserModelList, self).get_context_data(**kwargs)
        context['project_list'] = Project.objects.filter(user = self.request.user)
        context['skill_list'] = Skill.objects.filter(user = self.request.user)
        context['award_list'] = Award.objects.filter(user = self.request.user)
        context['certification_list'] = Certification.objects.filter(user = self.request.user)
        return context

class UserProfileDetailView(DetailView):
    context_object_name = 'user_detail'
    template_name = 'usermodel_detail.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super(UserProfileDetailView, self).get_context_data(**kwargs)
        context['skills'] = Skill.objects.filter(user = self.request.user)
        context['project_list'] = Project.objects.filter(user = self.request.user)
        context['award_list'] = Award.objects.filter(user = self.request.user)
        context['certification_list'] = Certification.objects.filter(user = self.request.user)
        user_model = UserModel.objects.get(user = self.request.user)
        hobies = user_model.hobies
        hobies_list = hobies.split(',')
        context['hobies_list'] = hobies_list

        extra = user_model.extra_curriculam
        extra_list = extra.split(',')
        context['extra_list'] = extra_list

        return context

class UserProfileCreateView(CreateView):
    model = UserModel
    template_name = 'usermodel_form.html'
    form_class = UserModelForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserProfileUpdateView(UpdateView):
    model = UserModel
    template_name = 'usermodel_form.html'
    form_class = UserModelForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Project related classes

class ProjectCreateView(CreateView):
    model = Project
    context_object_name = 'projects'
    template_name = 'project_form.html'
    form_class = ProjectForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(UpdateView):
    template_name = 'project_form.html'
    model = Project
    form_class = ProjectForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProjectDetailView(DetailView):
    context_object_name = 'project_detail'
    template_name = 'project_detail.html'
    model = Project

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project_confirm_delete.html'
    success_url = reverse_lazy('job_seeker:usermodel_list')


# Skill related classes

class SkillCreateView(CreateView):
    model = Skill
    template_name = 'skill_form.html'
    form_class = SkillForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SkillUpdateView(UpdateView):
    form_class = SkillForm
    template_name = 'skill_form.html'
    model = Skill

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SkillDetailView(DetailView):
    context_object_name = 'skills'
    model = Skill
    template_name = 'skill_detail.html'


class SkillDeleteView(DeleteView):
    model = Skill
    template_name = 'skill_confirm_delete.html'
    success_url = reverse_lazy('job_seeker:usermodel_list')


# Awards related classes

class AwardCreateView(CreateView):
    model = Award
    template_name = 'award_form.html'
    form_class = AwardForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AwardUpdateView(UpdateView):
    form_class = AwardForm
    template_name = 'award_form.html'
    model = Award

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AwardDetailView(DetailView):
    context_object_name = 'awards'
    model = Award
    template_name = 'award_detail.html'


class AwardDeleteView(DeleteView):
    model = Award
    template_name = 'award_confirm_delete.html'
    success_url = reverse_lazy('job_seeker:usermodel_list')


# Project related classes

class CertificationCreateView(CreateView):
    model = Certification
    context_object_name = 'certifications'
    template_name = 'certification_form.html'
    form_class = CertificationForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CertificationUpdateView(UpdateView):
    template_name = 'certification_form.html'
    model = Certification
    form_class = CertificationForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CertificationDetailView(DetailView):
    context_object_name = 'certifications'
    template_name = 'certification_detail.html'
    model = Certification

class CertificationDeleteView(DeleteView):
    model = Certification
    template_name = 'certification_confirm_delete.html'
    success_url = reverse_lazy('job_seeker:usermodel_list')


#### views related to the job_status and available jobs ####

class JobDisplay(TemplateView):
    template_name = 'job_display.html'


    def get_context_data(self, **kwargs):
        context = super(JobDisplay, self).get_context_data(**kwargs)
        context['applied_job_list'] = Jobs.objects.filter(user = self.request.user)

        applied_job_list = Jobs.objects.filter(user=self.request.user)
        full_job_list = Job.objects.all()

        applied_jobs = []
        for job in applied_job_list:
            applied_jobs.append(job.job)

        job_list = []

        for job in full_job_list:
            if(job not in applied_jobs):
                job_list.append(job)

        context['job_list'] = job_list

        return context

class JobDetailView(DetailView):
    print("Job Detail View")
    context_object_name = 'job_detail'
    model = Job
    template_name = 'job_detail.html'


class JobsDeleteView(DeleteView):
    model = Jobs
    context_object_name = 'jobs_applied'
    template_name = 'CancelJob_confirm_delete.html'
    success_url = reverse_lazy('job_seeker:job_display')


def JobApply(request, job_id):
    #print("job id is :{}".format(job_id))
    # return redirect('job_seeker:job_detail', pk = job_id)

    job_detail_object = Job.objects.get(id = job_id)
    company_object = job_detail_object.user
    c_user = CompanyModel.objects.get(user = company_object)
    j_user = request.user
    job_object = Jobs(job = job_detail_object, company_user = c_user, user = j_user, job_status = "Applied")
    job_object.save()

    applied_job_list = Jobs.objects.filter(user=j_user)
    full_job_list = Job.objects.all()

    applied_jobs = []
    for job in applied_job_list:
        applied_jobs.append(job.job)

    job_list = []

    for job in full_job_list:
        if(job not in applied_jobs):
            job_list.append(job)

    return render(request, 'job_display.html', context = {'applied_job_list':applied_job_list, 'job_list':job_list})

class AllJobs(TemplateView):
    template_name = 'job_display1.html'

    def get_context_data(self, **kwargs):
        context = super(AllJobs, self).get_context_data(**kwargs)
        context['applied_job_list'] = Jobs.objects.filter(user = self.request.user)

        applied_job_list = Jobs.objects.filter(user=self.request.user)
        full_job_list = Job.objects.all()

        applied_jobs = []
        for job in applied_job_list:
            applied_jobs.append(job.job)

        job_list = []

        for job in full_job_list:
            if(job not in applied_jobs):
                job_list.append(job)

        context['job_list'] = job_list

        return context

class ResumePage(TemplateView):
    template_name = 'job_display2.html'


def WebsiteAnalysis(request):
    companies = CompanyModel.objects.all()
    users = UserModel.objects.all()
    jobs = Job.objects.all()

    c_number = len(companies)
    u_number = len(users)
    j_num = len(jobs)

    return render(request, 'index.html', context = {'c_number':c_number, 'u_number':u_number, 'j_number':j_number})


class UserAnalysisPage(TemplateView):
    template_name = 'job_seeker_analysis.html'

    def get_context_data(self, **kwargs):
        context = super(UserAnalysisPage, self).get_context_data(**kwargs)
        user = self.request.user
        jobs = Jobs.objects.filter(user = user)

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
