from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
     list_display = ('question', 'question_hi', 'question_bn', 'created_at')
     search_fields = ('question', 'question_hi', 'question_bn')