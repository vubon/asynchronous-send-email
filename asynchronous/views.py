from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView

from asynchronous.forms import FeedbackForm
from asynchronous.tasks import send_feedback_email_task


class SendEmail(FormView):
    template_name = 'index.html'
    form_class = FeedbackForm
    success_url = '/'

    def form_valid(self, form):
        form.send_email()
        return super(SendEmail, self).form_valid(form)


# def index(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             msg = form.cleaned_data['message']
#             # The delay is used to asynchronously process the task
#             send_feedback_email_task().delay(name, email, msg)
#             return HttpResponseRedirect('/')
#     else:
#         form = FeedbackForm
#     return render(request, 'index.html', {'form': form})
