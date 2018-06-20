from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={'rows': 5}))
