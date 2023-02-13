from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import login, logout
from django.views import View


class UsersOperations:
    """
    In this class we are working with user operations
    which are not related to the rendering articles or other things
    """

    @staticmethod
    def login(request):
        """
        This method is responsible for logging in the user
        :param:
        :return:
        """
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = form.get_user()
                if user:
                    login(request, user)
                    return redirect('home')
                else:
                    return redirect('login')
            else:
                return redirect('login')
        else:
            form = LoginForm()

        context = {
            'form': form,
            'title': 'Вход в аккаунт'
        }

        return render(request, 'main/login.html', context=context)

    @staticmethod
    def register(request):
        """
        Registration of user
        :param request:
        :return:
        """
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('login')
            else:
                return redirect('register')
        else:
            form = RegistrationForm()

        context = {
            'form': form,
            'title': 'Регистрация'
        }
        return render(request, 'main/register.html', context=context)


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


class AboutUs(TemplateView):
    template_name = 'main/about.html'
    extra_context = {
        'title': 'О нас'
    }
