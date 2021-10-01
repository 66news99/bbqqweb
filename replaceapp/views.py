from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class BasicTemplateView(TemplateView):
    template_name = 'replaceapp/base.html'


def show_news(request):
    if request.mehtond == "POST":
        return render(request, 'replaceapp/base.html', context={'text':'다음 기사를 수정해보세요.'})
    else:
        return render(request, 'replaceapp/base.html', context={'text':'다음 기사를 수정해보세요.'})