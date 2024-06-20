from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from .forms import RegisterForm

# Представление для регистрации пользователя
class RegisterView(View):
    template_name = 'users/register.html'
    form_class = RegisterForm

    # Перенаправление аутентифицированных пользователей
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="contacts:root")
        return super().dispatch(request, *args, **kwargs)

    # Обработка GET-запроса для отображения формы регистрации
    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    # Обработка POST-запроса для обработки формы регистрации
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Welcome, {username}. Your account has been successfully created")
            return redirect(to="users:signin")
        return render(request, self.template_name, {"form": form})

# Представление для сброса пароля
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    html_email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'users/password_reset_subject.txt'

