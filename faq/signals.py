# from django.core.cache import cache
# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from googletrans import Translator
# from .models import FAQ  # Import your FAQ model

# # Initialize the translator
# translator = Translator()

# @receiver(pre_save, sender=FAQ)
# def auto_translate_faq(sender, instance, **kwargs):
#     # Generate cache keys for translations
#     cache_key_question_hi = f"translation_question_hi_{instance.question}"
#     cache_key_answer_hi = f"translation_answer_hi_{instance.answer}"
#     cache_key_question_bn = f"translation_question_bn_{instance.question}"
#     cache_key_answer_bn = f"translation_answer_bn_{instance.answer}"

#     # Check cache first
#     instance.question_hi = cache.get(cache_key_question_hi)
#     instance.answer_hi = cache.get(cache_key_answer_hi)
#     instance.question_bn = cache.get(cache_key_question_bn)
#     instance.answer_bn = cache.get(cache_key_answer_bn)

#     # If not in cache, translate and cache the result
#     if not instance.question_hi:
#         instance.question_hi = translator.translate(instance.question, dest='hi').text
#         cache.set(cache_key_question_hi, instance.question_hi, timeout=60*60*24)  # Cache for 1 day
#     if not instance.answer_hi:
#         instance.answer_hi = translator.translate(instance.answer, dest='hi').text
#         cache.set(cache_key_answer_hi, instance.answer_hi, timeout=60*60*24)
#     if not instance.question_bn:
#         instance.question_bn = translator.translate(instance.question, dest='bn').text
#         cache.set(cache_key_question_bn, instance.question_bn, timeout=60*60*24)
#     if not instance.answer_bn:
#         instance.answer_bn = translator.translate(instance.answer, dest='bn').text
#         cache.set(cache_key_answer_bn, instance.answer_bn, timeout=60*60*24)