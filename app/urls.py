from django.urls import path
from . import views

urlpatterns = [
    path('why-us/', views.WhyUsAPIView.as_view(), ),
    path('user-contact/', views.UserContactApplicationAPIView.as_view()),
    path('courses/', views.CoursesAPIView.as_view()),
    path('course/<int:pk>/', views.CourseDetailAPIView.as_view()),
    path('partners/', views.PartnersAPIView.as_view()),
    path('our-programs/', views.OurProgramsAPIView.as_view()),
    path('our-program-info/<int:pk>/', views.OurProgramInfoAPIView.as_view()),
    path('student-feadback/', views.StudentFeadBackAPIView.as_view()),
    path('our-mentors/', views.OurMentorsAPIView.as_view()),
    path('faq/', views.FAQAPIView.as_view()),
    path('for-whom', views.ForWhomAPIView.as_view()),
    path('course-plan/', views.CoursePlanAPIView.as_view()),
    path('course-module/', views.CourseModulAPIView.as_view()),
    path('course-module-info/', views.ModulInfoAPIView.as_view()),
    path('about-mentor/<int:pk>/', views.AboutMentorAPIView.as_view()),
    path('computer-features/', views.ComputerFeaturesAPIView.as_view()),
    path('team/', views.TeamAPIView.as_view()),

]
