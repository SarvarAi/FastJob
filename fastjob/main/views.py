from django.views.generic import TemplateView


class HomeCV(TemplateView):
    template_name = 'main/index.html'
    extra_context = {
        'title': 'FastJob'
    }


class HomeEmployer(TemplateView):
    template_name = 'main/index.html'
    extra_context = {
        'title': 'FastJob Ищем сотрудника'
    }
