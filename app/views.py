from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import AllowAny

from app.models import WhyUs, UserContactApplication, Course, Partner, OurProgram, OurProgramInfo, FeadBack, Mentor, \
    Faq, ForWhom, CoursePlan, CourseModul, ModulInfo, MentorWorkPlace, ComputerFeatures, Team
from .serializers import WhyUsModelSerializer, UserContactApplicationModelSerializer, CourseModelSerializer, \
    PartnersModelSerializer, OurProgramModelSerializer, OurProgramInfoModelSerializer, FeadBackModelSerializer, \
    MentorModelSerializer, FaqModelSerializer, ForWhomModelSerializer, CoursePlanModelSerializer, CourseSerializer, \
    ModulInfoModelSerializer, ComputerFeaturesModelSerializer, TeamModelSerializer


# Create your views here.


class WhyUsAPIView(ListAPIView):
    queryset = WhyUs.objects.all()
    serializer_class = WhyUsModelSerializer
    permission_classes = (AllowAny,)


class UserContactApplicationAPIView(CreateAPIView):
    queryset = UserContactApplication.objects.all()
    serializer_class = UserContactApplicationModelSerializer
    permission_classes = (AllowAny,)


class CoursesAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (AllowAny,)


class PartnersAPIView(ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnersModelSerializer
    permission_classes = (AllowAny,)


class OurProgramsAPIView(ListAPIView):
    queryset = OurProgram.objects.all()
    serializer_class = OurProgramModelSerializer
    permission_classes = (AllowAny,)


class OurProgramInfoAPIView(RetrieveAPIView):
    queryset = OurProgramInfo.objects.all()
    serializer_class = OurProgramInfoModelSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'id'


class StudentFeadBackAPIView(ListAPIView):
    queryset = FeadBack.objects.all()
    serializer_class = FeadBackModelSerializer
    permission_classes = (AllowAny,)


class OurMentorsAPIView(ListAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorModelSerializer
    permission_classes = (AllowAny,)


class FAQAPIView(ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqModelSerializer
    permission_classes = (AllowAny,)


class ForWhomAPIView(ListAPIView):
    queryset = ForWhom.objects.all()
    serializer_class = ForWhomModelSerializer
    permission_classes = (AllowAny,)


class CoursePlanAPIView(ListAPIView):
    queryset = CoursePlan.objects.all()
    serializer_class = CoursePlanModelSerializer
    permission_classes = (AllowAny,)


class CourseModulAPIView(ListAPIView):
    queryset = CourseModul.objects.all()
    serializer_class = CourseModelSerializer
    permission_classes = (AllowAny,)


class ModulInfoAPIView(RetrieveAPIView):
    queryset = ModulInfo.objects.all()
    serializer_class = ModulInfoModelSerializer
    permission_classes = (AllowAny,)


class AboutMentorAPIView(RetrieveAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorModelSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'id'


class ComputerFeaturesAPIView(RetrieveAPIView):
    queryset = ComputerFeatures.objects.all()
    serializer_class = ComputerFeaturesModelSerializer
    permission_classes = (AllowAny,)


class TeamAPIView(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamModelSerializer
    permission_classes = (AllowAny,)
