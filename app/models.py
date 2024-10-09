from django.db import models
from app.validator import uzbek_phone_validator


# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title


class UserContactApplication(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, validators=[uzbek_phone_validator])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_check = models.BooleanField(default=False)


class ForWhom(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='for_whom')


class ComputerFeatures(models.Model):
    protcessor = models.CharField(max_length=100)
    cpu = models.CharField(max_length=100)
    video_card = models.FileField(upload_to='media/')
    display = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='computer_features')

    def __str__(self):
        return self.protcessor


class CourseModul(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='moduls')

    def __str__(self):
        return self.title


class ModulInfo(models.Model):
    modul_lesson = models.CharField(max_length=100)
    course_modul = models.ForeignKey(CourseModul, on_delete=models.CASCADE, related_name='modul_lesson')

    def __str__(self):
        return self.modul_lesson


class WhyUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title


class Partner(models.Model):
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.image.name


class OurProgram(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title


class OurProgramInfo(models.Model):
    inform = models.TextField()
    our_program = models.ForeignKey(OurProgram, on_delete=models.CASCADE, related_name='program_info')
    order = models.IntegerField()


class Faq(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question


class FeadBack(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    message = models.TextField()
    profession = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class CoursePlan(models.Model):
    total_duration = models.IntegerField()
    time_for_theory = models.IntegerField()
    time_for_practice = models.IntegerField()
    for_theory = models.IntegerField()
    for_practice = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_plan')

    def __str__(self):
        return self.course


class Mentor(models.Model):
    full_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    experience = models.IntegerField()
    mentor_achievement = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='mentor')

    def __str__(self):
        return self.full_name


class MentorWorkPlace(models.Model):
    logo = models.ImageField(upload_to='media/')
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='mentor_workplace')


class Team(models.Model):
    full_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.full_name
