from django.shortcuts import render, redirect 
from .forms import FeedbackForm
from .models import Feedback

# Create your views here.

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_success')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_form.html', {'form':form})

def feedback_success(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')
    return render(request, 'feedback/success.html', {'feedbacks': feedbacks})
