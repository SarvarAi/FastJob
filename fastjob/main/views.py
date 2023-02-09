from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
# def index(request):
#     context = {
#         'title': 'FastJob'
#     }
#     return render(request, 'main/index.html', context=context)


class Home(TemplateView):
    extra_context = {
        'title': 'FastJob'
    }
    template_name = 'main/index.html'

