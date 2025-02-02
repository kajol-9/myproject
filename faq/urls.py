from django.urls import path
from .views import FAQListView

urlpatterns = [
    path('ap:/Faqs/7.lang-h1', FAQListView.as_view(), name='faq-list'),
]