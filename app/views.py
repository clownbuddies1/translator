from django.shortcuts import render
from django.http import HttpResponse
from googletrans import Translator
# Create your views here.

def home(request):
    return render(request, 'home.html')

def translated(request):
    text = request.GET.get('text')
    lang = request.GET.get('lang')
    
    print('Text : ', text, 'Lang : ', lang)
    
    translator = Translator()

    dt = translator.detect(text)
    dt2 = dt.lang
    
    translated = translator.translate(text, lang)
    tr = translated.text
    
    return render(request, 'translated.html', {'translated': tr, 'u_lang': dt2, 't_lang': lang})