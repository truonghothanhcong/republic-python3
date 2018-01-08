from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from app_download import models
from app_download.forms import VideoForm
from app_download.models import Video


class IndexView(generic.FormView):
    form_class = VideoForm
    model = Video
    template_name = 'app_download/index.html'

    def form_valid(self, form):
        videos = models.objects.all()
        context = self.get_context_data()
        return render(self.request, self.template_name, context)


def index(request):
    return render(request, 'index.html')
    #return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

