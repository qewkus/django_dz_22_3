from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название поста",
        help_text="Введите название поста",
    )
    content = models.TextField(
        verbose_name="Текст поста",
        help_text="Введите текст поста",
        blank=True,
        null=True,
    )
    preview_image = models.ImageField(
        upload_to="products/image",
        verbose_name="Изображение для поста",
        blank=True,
        null=True,
        help_text="Загрузите изображение поста",
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    views_count = models.IntegerField(
        default=0, verbose_name="Количество просмотров"
    )

    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
