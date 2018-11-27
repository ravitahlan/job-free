from django.conf.urls import url
from job_seeker import views

app_name = "job_seeker"

urlpatterns = [
    # url(r'^$', views.UserDashBoard.as_view(), name = "user_dashboard"),
    url(r'^$', views.UserModelList.as_view(), name = "usermodel_list"),
    url(r'^(?P<pk>\d+)/$', views.UserProfileDetailView.as_view(), name = "detail"),
    url(r'^personal/$', views.UserProfileCreateView.as_view(), name = "user_profile_form"),
    url(r'^update/(?P<pk>\d+)/$', views.UserProfileUpdateView.as_view(), name = "update_profile_form"),

    url(r'^pro/(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name = "project_detail"),
    url(r'^pro_update/(?P<pk>\d+)/$', views.ProjectUpdateView.as_view(), name = "project_update"),
    url(r'^project/$', views.ProjectCreateView.as_view(), name = "create_project"),
    url(r'^delete/(?P<pk>\d+)/$', views.ProjectDeleteView.as_view(), name = "project_delete"),

    url(r'^skill/$', views.SkillCreateView.as_view(), name = "create_skill"),
    url(r'^skill_update/(?P<pk>\d+)/$', views.SkillUpdateView.as_view(), name = "skill_update"),
    url(r'^skill/(?P<pk>\d+)/$', views.SkillDetailView.as_view(), name = "skill_detail"),
    url(r'^skill_delete/(?P<pk>\d+)/$', views.SkillDeleteView.as_view(), name = "skill_delete"),

    url(r'^award/$', views.AwardCreateView.as_view(), name = "create_award"),
    url(r'^award_update/(?P<pk>\d+)/$', views.AwardUpdateView.as_view(), name = "award_update"),
    url(r'^award/(?P<pk>\d+)/$', views.AwardDetailView.as_view(), name = "award_detail"),
    url(r'^award_delete/(?P<pk>\d+)/$', views.AwardDeleteView.as_view(), name = "award_delete"),

    url(r'^certification/$', views.CertificationCreateView.as_view(), name = "create_certification"),
    url(r'^certification_update/(?P<pk>\d+)/$', views.CertificationUpdateView.as_view(), name = "certification_update"),
    url(r'^certification/(?P<pk>\d+)/$', views.CertificationDetailView.as_view(), name = "certification_detail"),
    url(r'^certification_delete/(?P<pk>\d+)/$', views.CertificationDeleteView.as_view(), name = "certification_delete"),

    url(r'^review1/$', views.Res1.as_view(), name = 'res1'),
    url(r'^review2/$', views.Res2.as_view(), name = 'res2'),
    url(r'^review3/$', views.Res3.as_view(), name = 'res3'),
    url(r'^review4/$', views.Res4.as_view(), name = 'res4'),
    url(r'^review5/$', views.Res5.as_view(), name = 'res5'),

    url(r'^dash/$', views.JobDisplay.as_view(), name = 'job_display'),
    url(r'job_detail/(?P<pk>\d+)/$', views.JobDetailView.as_view(), name = 'job_detail'),
    url(r'apply/(?P<job_id>\d+)', views.JobApply, name = "job_apply"),
    url(r'^cancel_application/(?P<pk>\d+)/$', views.JobsDeleteView.as_view(), name = 'cancel_job'),
    url(r'^all_jobs/$', views.AllJobs.as_view(), name = "all_jobs"),
    url(r'^resume_page/$', views.ResumePage.as_view(), name = "resume_page"),
    url(r'^user_analysis_page/$', views.UserAnalysisPage.as_view(), name = "user_analysis")

]
