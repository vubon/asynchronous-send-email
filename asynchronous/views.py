from django.http import HttpResponseRedirect
from django.shortcuts import render

from asynchronous.forms import FeedbackForm
from asynchronous.tasks import send_feedback_email_task


def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            msg = form.cleaned_data['message']
            # The delay is used to asynchronously process the task
            send_feedback_email_task().delay(name, email, msg)
            return HttpResponseRedirect('/')
    else:
        form = FeedbackForm
    return render(request, 'index.html', {'form': form})
