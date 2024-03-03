from django.shortcuts import render

# Create your views here.
def IndexPageView(request):
    return render(request, 'users/index.html')

# def QuizPageView(request):
#     return render(request, 'users/quiz.html')

def ContactPageView(request):
    return render(request, 'users/contact.html')

def AboutPageView(request):
    return render(request, 'users/about.html')
