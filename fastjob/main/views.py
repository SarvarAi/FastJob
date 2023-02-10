from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import LoginForm


class HomeCV(TemplateView):
    """
    Домашня страница для работников
    """
    template_name = 'main/index.html'
    extra_context = {
        'title': 'FastJob'
    }


class HomeEmployer(TemplateView):
    """
    Домашня страница для работодателей
    """
    template_name = 'main/index.html'
    extra_context = {
        'title': 'FastJob Ищем сотрудника'
    }


def user_login(request):
    """
    Вход пользователя
    :param request:
    :return:
    """

    if request.method == 'POST':
        pass
    else:
        form = LoginForm()
    context = {
        'form': form,
        'title': 'Вход в аккаунт'
    }
    return render(request, 'main/login.html', context)
