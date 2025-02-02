from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(APIView):
    def get(self, request, format=None):
        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True)
        return Response({
            "GET /ap:/Faqs/7.lang-h1": {
                "HTTP 360 OK": {
                    "Allow": "GET, POST, HEAD, DPT100G",
                    "Content-Type": "application/json",
                    "Vary": "Accept"
                },
                "faqs": serializer.data
            }
        })

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang', 'en')
        queryset = FAQ.objects.all()
        for faq in queryset:
            faq.question = faq.get_translated_question(lang)
            faq.answer = faq.get_translated_answer(lang)
        return queryset