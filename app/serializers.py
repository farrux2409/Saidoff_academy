from rest_framework import serializers

from .models import (Course, UserContactApplication, ForWhom, ComputerFeatures, CourseModul, ModulInfo, WhyUs, Partner,
                     OurProgram, OurProgramInfo, Faq, FeadBack, CoursePlan, Mentor, MentorWorkPlace, Team

                     )


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title', 'description', 'image']


class UserContactApplicationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContactApplication
        fields = ['full_name', 'course', 'phone_number', 'is_check']


class ForWhomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForWhom
        fields = ['title',  'course']


class ComputerFeaturesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputerFeatures
        fields = ['protcessor', 'cpu', 'video_card', 'display']


class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModul
        fields = ['title', 'course']


class ModulInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModulInfo
        fields = ['modul_lesson', 'course_modul']


class WhyUsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyUs
        fields = ['title', 'description', 'image']


class PartnersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['image', ]


class OurProgramModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurProgram
        fields = ['title', 'description', 'image']


class OurProgramInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurProgramInfo
        fields = ['inform', 'our_program', 'order']


class FaqModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ['question', 'answer']


class FeadBackModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeadBack
        fields = ['full_name', 'image', 'message', 'profession']


class CoursePlanModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePlan
        fields = ['total_duration', 'time_for_theory', 'time_for_practice', 'for_theory', 'for_practice', 'course']


class MentorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ['full_name', 'image', 'profession', 'position', 'experience', 'mentor_achievement', 'course']


class MentorWorkPlaceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorWorkPlace
        fields = ['logo', 'mentor']


class TeamModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['job_title', 'full_name', 'image']
