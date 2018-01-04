from django.http import HttpResponse
from django.shortcuts import render

from app_download.models import Video


def index(request):
    videos = Video.objects.all()[:5]
    output = ', '.join([q.name for q in videos])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

