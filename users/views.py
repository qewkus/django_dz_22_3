from config.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class RegisterView(CreateView):
    template_name = "users/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        messages.success(self.request, 'Регистрация прошла успешно! Проверьте почту.')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш магазин'
        message = 'Спасибо, что зарегистрировались в нашем магазине'
        from_email = EMAIL_HOST_USER
        recipient_list = [user_email,]
        send_mail(subject, message, from_email, recipient_list)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = "users/edit_profile.html"
    success_url = reverse_lazy("catalog:home")

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Профиль успешно обновлен!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при обновлении профиля.')
