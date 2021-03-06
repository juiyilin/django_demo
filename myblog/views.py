from django.shortcuts import render
from django.template.loader import get_template
from .models import Post
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from myblog import models, forms
import json
import urllib
from django.conf import settings
'''from io import BytesIO
from django.core.files.uploadedfile import File
from django.core.files.uploadedfile import InMemoryUploadedFile'''


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', locals())


def message(request):
    posts = Post.objects.all()

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

                post_form.save()

                '''newest = Post.objects.all()
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
                imgs.save()'''
                return HttpResponseRedirect('/message/')
            else:
                message = "reCAPTCHA驗證失敗，請再確認."
        else:
            message = '如要張貼訊息，則每一個欄位都要填'
    else:
        post_form = forms.PostForm()
        message = '如要張貼訊息，則每一個欄位都要填'
    return render(request, 'message.html', locals())


def autobiography(request):
    return render(request, 'autobiography.html', locals())


def portfolio(request):
    return render(request, 'portfolio.html', locals())


def text_to_image(request):
    return render(request, 'portfolios/text_to_image.html', locals())


def official_document_classify(request):
    return render(request, 'portfolios/official-document-classify.html', locals())


def web_crawler(request):
    return render(request, 'portfolios/web_crawler.html', locals())


def covid19(request):
    return render(request, 'portfolios/covid19.html', locals())


def newsletter_banner(request):
    return render(request, 'portfolios/newsletter_banner.html', locals())


def unsubscribe_email(request):
    return render(request, 'portfolios/unsubscribe_email.html', locals())


def iphone(request):
    return render(request, 'portfolios/iphone.html', locals())
