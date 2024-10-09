from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(UserContactApplication)
class UserContactApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'is_check', 'phone_number')
    search_fields = ('full_name', 'phone_number')
    list_filter = ('is_check', 'phone_number')


@admin.register(ForWhom)
class ForWhomAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    search_fields = ('title', 'course')
    list_filter = ('title', 'course')


@admin.register(ComputerFeatures)
class ComputerFeaturesAdmin(admin.ModelAdmin):
    list_display = ('protcessor', 'cpu', 'video_card', 'display')
    search_fields = ('protcessor', 'cpu', 'video_card', 'display')
    list_filter = ('protcessor', 'cpu', 'video_card', 'display')


@admin.register(CourseModul)
class CourseModulAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    search_fields = ('title', 'course')
    list_filter = ('title', 'course')


@admin.register(ModulInfo)
class ModulInfoAdmin(admin.ModelAdmin):
    list_display = ('modul_lesson', 'course_modul')
    search_fields = ('modul_lesson', 'course_modul')
    list_filter = ('modul_lesson', 'course_modul')


@admin.register(WhyUs)
class WhyUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(OurProgram)
class OurProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(OurProgramInfo)
class OurProgramInfoAdmin(admin.ModelAdmin):
    list_display = ('order', 'inform')
    search_fields = ('order', 'inform')
    list_filter = ('inform',)


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer',)
    search_fields = ('question', 'answer')
    list_filter = ('question', 'answer')


@admin.register(FeadBack)
class FeadBackAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'profession', 'image')
    search_fields = ('full_name', 'profession')
    list_filter = ('full_name', 'profession')


@admin.register(CoursePlan)
class CoursePlanAdmin(admin.ModelAdmin):
    list_display = ('total_duration', 'time_for_theory', 'for_practice')
    search_fields = ('total_duration', 'time_for_theory', 'for_practice')
    list_filter = ('total_duration', 'time_for_theory', 'for_practice')


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'profession', 'image', 'mentor_achievement')
    search_fields = ('full_name', 'profession')
    list_filter = ('full_name', 'profession')


@admin.register(MentorWorkPlace)
class MentorWorkPlaceAdmin(admin.ModelAdmin):
    list_display = ('logo', 'mentor')
    search_fields = ('logo',)
    list_filter = ('logo',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job_title', 'image')
    search_fields = ('full_name', 'job_title')
    list_filter = ('full_name', 'job_title')
