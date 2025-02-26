from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

translator = Translator()

def translate_text(text, dest_lang):
    try:
        return translator.translate(text, dest=dest_lang).text
    except:
        return text


    
  
class FAQ(models.Model):
    question = models.TextField()  # Original question in English
    answer = models.TextField()    # Original answer in English
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation
    answer_hi = models.TextField(blank=True, null=True)    # Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation
    answer_bn = models.TextField(blank=True, null=True)    # Bengali translation
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    def get_translated_question(self, lang='en'):
        return getattr(self, f'question_{lang}', self.question)

    def get_translated_answer(self, lang='en'):
        return getattr(self, f'answer_{lang}', self.answer)

    def __str__(self):
        return self.question
    def save(self, *args, **kwargs):
        if not self.question_hi:
            self.question_hi = translate_text(self.question, 'hi')
        if not self.question_bn:
            self.question_bn = translate_text(self.question, 'bn')
        if not self.answer_hi:
            self.answer_hi = translate_text(self.answer, 'hi')
        if not self.answer_bn:
            self.answer_bn = translate_text(self.answer, 'bn')
        super().save(*args, **kwargs)