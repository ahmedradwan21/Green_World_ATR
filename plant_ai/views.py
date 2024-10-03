from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Inquiry
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from langdetect import detect
from deep_translator import GoogleTranslator
import difflib

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip().lower()
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word.isalnum() and word not in stop_words]
    return " ".join(filtered_text)

def detect_language(text):
    try:
        return detect(text)
    except:
        return 'en'  

@login_required
def process_question(request):
    if request.method == 'POST':
        user_question = request.POST.get('question')
        
        if not user_question:
            return HttpResponseBadRequest("Invalid question")
        
        question_language = detect_language(user_question)
        
        if question_language != 'en':
            translated_question = GoogleTranslator(source=question_language, target='en').translate(user_question)
            processed_user_question = preprocess_text(translated_question)
        else:
            processed_user_question = preprocess_text(user_question)
        
        try:
            inquiries = Inquiry.objects.all()
            best_match_score = 0
            best_match_answer = None
            
            for inquiry in inquiries:
                processed_stored_question = preprocess_text(inquiry.question)
                
                similarity_ratio = difflib.SequenceMatcher(None, processed_user_question, processed_stored_question).ratio()
                if similarity_ratio > best_match_score:
                    best_match_score = similarity_ratio
                    best_match_answer = inquiry.answer
            
            similarity_threshold = 0.8  # Adjust this value as needed
            
            if best_match_answer and best_match_score >= similarity_threshold:
                if question_language != 'en':
                    best_match_answer = GoogleTranslator(source='en', target=question_language).translate(best_match_answer)
                return JsonResponse({'answer': best_match_answer})
            else:
                answer = "Sorry, there is no available answer for this question at the moment."
                if question_language != 'en':
                    answer = GoogleTranslator(source='en', target=question_language).translate(answer)
                return JsonResponse({'answer': answer})

        except Inquiry.DoesNotExist:
            answer = "Sorry, there is no available answer for this question at the moment."
            if question_language != 'en':
                answer = GoogleTranslator(source='en', target=question_language).translate(answer)
            return JsonResponse({'answer': answer})

    return render(request, 'plant_ai/process_question.html')








