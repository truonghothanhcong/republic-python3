from django.forms import forms


class VideoForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(VideoForm, self).__init__(*args, **kwargs)
