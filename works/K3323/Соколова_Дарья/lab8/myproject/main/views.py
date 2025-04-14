from django.shortcuts import render
from .forms import FeedbackForm
from .models import Feedback

# Create your views here.
def home(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/contact.html', {'success': True})
    else:
        form = FeedbackForm()
    
    return render(request, 'main/contact.html', {'form': form})