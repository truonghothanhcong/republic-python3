from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context
from django.views import generic

from app_download import models
from app_download.forms import VideoForm
from app_download.models import Video


def index(request):
    videos = models.Video.objects.values()
    return render(request, 'app_download/index.html', {'videos': videos})


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

