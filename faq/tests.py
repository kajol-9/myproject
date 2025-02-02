from django.test import TestCase
from .models import FAQ

class FAQTestCase(TestCase):
    def setUp(self):
        FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")

    def test_faq_translation(self):
        faq = FAQ.objects.get(question="What is Django?")
        self.assertEqual(faq.get_translated_question('hi'), faq.question_hi)