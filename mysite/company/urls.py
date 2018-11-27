from django.conf.urls import url
from company import views

app_name = "company"

urlpatterns = [

    url(r'^$', views.CompanyProfileListView.as_view(), name = "company_dashboard"),
    url(r'^jobs_dashboard/$', views.CompanyJobsDashboard, name='company_jobs_dashboard'),
    url(r'^companyprofile/$', views.CompanyProfileView.as_view(), name = "company_profile_form"),
    url(r'^company_update/(?P<pk>\d+)/$', views.CompanyProfileUpdateView.as_view(), name = 'company_update'),
    url(r'^(?P<pk>\d+)/$', views.CompanyProfileDetailView.as_view(), name = 'company_detail'),
    url(r'^job_dash/$',  views.CompanyJobsDashboard, name = 'company_dash'),

    url(r'^job_create/$', views.JobCreateView.as_view(), name = 'job_create'),
    url(r'^job_update/(?P<pk>\d+)/$', views.JobUpdateView.as_view(), name = 'job_update'),
    url(r'^job_detail/(?P<pk>\d+)/$', views.JobDetailView.as_view(), name = 'job_detail'),
    url(r'^job_delete/(?P<pk>\d+)/$', views.JobDeleteView.as_view(), name = 'job_delete'),
    url(r'^user_object_detail/(?P<candidate_id>\d+)/$', views.ShowCandidateDetail, name = 'user_detail'),
    url(r'^selected/(?P<job_id>\d+)/$', views.Selected, name = "selected"),
    url(r'^rejected/(?P<job_id>\d+)/$', views.Rejected, name = "rejected"),
    url(r'^applicants/$', views.AllApplicantsView, name = "all_applicants"),
    url(r'^candidates/$', views.AllCandidatesView, name = "all_candidates"),
    url(r'^candidate_detail/(?P<key_id>\d+)/$', views.CandidateDisplay, name = "candidate_detail"),
    url(r'^download_resume/(?P<user_id>\d+)/$', views.GetResume, name = "get_resume"),
    url(r'^analysis_page/$', views.AnalysisPage.as_view(), name = "analysis_page")
]
