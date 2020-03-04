from django.shortcuts import render
from django.template.loader import get_template
from .models import Post, Postimg
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from myblog import models, forms, mestoimg
import json
import urllib
from django.conf import settings
from io import BytesIO
from django.core.files.uploadedfile import File
from django.core.files.uploadedfile import InMemoryUploadedFile


def index(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)


def post2db(request):
    pmess = Postimg.objects.all()

    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            if result['success']:

                message = "您的訊息已儲存，要等管理者啟用後才看得到喔。"
                post_form.save()

                newest = Post.objects.all()
                postid = '#'+str(newest[0].id)
                words = newest[0].text
                line, word = mestoimg.wordwrap(postid, words)
                i = mestoimg.picture(line, word)

                byt = BytesIO()
                i.save(byt, 'png')

                imgs = Postimg()
                image_file = InMemoryUploadedFile(
                    byt, None, 'test.png', 'image/png', byt.getbuffer().nbytes, None)
                imgs.img.save(str(newest[0].id)+'.png', image_file)
                imgs.text = newest[0].text
                imgs.imgname = str(newest[0].id)+'.png'
                imgs.save()
                return HttpResponseRedirect('/post2db/')
            else:
                message = "reCAPTCHA驗證失敗，請再確認."
        else:
            message = '如要張貼訊息，則每一個欄位都要填...'
    else:
        post_form = forms.PostForm()
        message = '如要張貼訊息，則每一個欄位都要填...'
    return render(request, 'post2db.html', locals())


def wordtoimg(request):

    showimg = Postimg.objects.all()
    return render(request, 'images.html', locals())


def profile(request):
    return render(request, 'profile.html', locals())
