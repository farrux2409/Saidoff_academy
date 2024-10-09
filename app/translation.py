from modeltranslation.translator import translator, TranslationOptions
from .models import (Course, UserContactApplication, ForWhom, ComputerFeatures, CourseModul, ModulInfo, WhyUs,
                     OurProgram, OurProgramInfo, Faq, FeadBack, Mentor, Team)


class CourseTranslation(TranslationOptions):
    fields = ('title', 'description')


class UserContactApplicationTranslation(TranslationOptions):
    fields = ('full_name',)


class ForWhomTranslation(TranslationOptions):
    fields = ('title',)


class ComputerFeaturesTranslation(TranslationOptions):
    fields = ('protcessor', 'cpu', 'video_card', 'display')


class CourseModulTranslation(TranslationOptions):
    fields = ('title',)


class ModulInfoTranslation(TranslationOptions):
    fields = ('modul_lesson',)


class WhyUsTranslation(TranslationOptions):
    fields = ('title', 'description', 'image')


class OurProgramTranslation(TranslationOptions):
    fields = ('title', 'description', 'image')


class OurProgramInfoTranslation(TranslationOptions):
    fields = ('inform',)


class FaqTranslation(TranslationOptions):
    fields = ('question', 'answer')


class FeadBackTranslation(TranslationOptions):
    fields = ('full_name', 'message', 'profession')


class MentorTranslation(TranslationOptions):
    fields = ('full_name', 'profession', 'position', 'mentor_achievement')


class TeamTranslation(TranslationOptions):
    fields = ('full_name', 'job_title')


for a, b in [(Course, CourseTranslation), (UserContactApplication, UserContactApplicationTranslation),
             (ForWhom, ForWhomTranslation), (ComputerFeatures, ComputerFeaturesTranslation),
             (ModulInfo, ModulInfoTranslation), (WhyUs, WhyUsTranslation), (OurProgramInfo, OurProgramInfoTranslation),
             (OurProgram, OurProgramTranslation), (Faq, FaqTranslation), (FeadBack, FeadBackTranslation),
             (Mentor, MentorTranslation), (Team, TeamTranslation), (CourseModul, CourseModulTranslation)]:
    translator.register(a, b)
