from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse
from django.views.generic import TemplateView

from replaceapp.models import NewModel


def challenge(request):
    if request.method == "post":
        temp = request.POST.get("input_text")

        model_instance = NewModel()
        model_instance.text = temp
        model_instance.save()

        data_list = NewModel.objects.all()

        return HttpResponseRedirect(reverse('replaceapp:challenge'))
    else:
        data_list = NewModel.objects.all()
        return render(request, 'replaceapp/base.html',
                      context={'data_list': data_list})


class BasicTemplateView(TemplateView):
    template_name = 'replaceapp/base.html'




