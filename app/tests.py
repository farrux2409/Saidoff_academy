from django.test import TestCase

from app.models import Course, UserContactApplication, Faq, WhyUs
from django.core.files.uploadedfile import SimpleUploadedFile


# class CourseTestCase(TestCase):
#     def setUp(self):
#         self.test_image = SimpleUploadedFile(name='test.jpg', content=open('test.jpg', 'rb').read(),
#                                              content_type='image/jpeg')
#
#         self.course = Course.objects.create(
#             title='Test Course',
#             description='Test Courses',
#             image=self.test_image
#
#         )
#
#     def test_course(self):
#         self.assertEqual(self.course.title, 'Test Course')
#         self.assertEqual(self.course.description, 'Test Courses main')
#         self.assertEqual(self.course.image, self.test_image)
#         self.assertEqual(self.course.title, 'Test Course')
#

class FaqTestCase(TestCase):
    def setUp(self):
        self.faq = Faq.objects.create(
            question='Test Faq',
            answer='Test Answer',

        )

    def test_faq_creation(self):
        self.assertEqual(self.faq.question, 'Test Faq')
        self.assertEqual(self.faq.answer, 'Test Answer')


