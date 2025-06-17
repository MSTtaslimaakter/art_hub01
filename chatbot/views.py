
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import openai
from django.http import JsonResponse
import json

openai.api_key = 'your-openai-api-key-here'

@csrf_exempt
def chat_response(request):
    if request.method == 'POST':
        user_input = json.loads(request.body).get('message')
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        answer = response['choices'][0]['message']['content']
        return JsonResponse({'reply': answer})
    return JsonResponse({'reply': 'Invalid request'}, status=400)

def chatbot_ui(request):
    return render(request, 'chatbot/chat_ui.html')

# Create your views here.
