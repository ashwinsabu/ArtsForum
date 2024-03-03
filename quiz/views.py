from django.shortcuts import render

# Create your views here.
def QuizPageView(request):
    return render(request, 'users/quiz.html')