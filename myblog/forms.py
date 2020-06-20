from django import forms
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from . import models
from captcha.fields import CaptchaField


class PostForm(forms.ModelForm):
    #captcha = CaptchaField()

    class Meta:
        model = models.Post
        fields = [
            "text",
            "name",
        ]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = "暱稱"
        self.fields["text"].label = "留言"
        #self.fields["captcha"].label = "我不是機器人"
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
