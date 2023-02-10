from django.db import models


# Create your models here.


class CategoryCV(models.Model):
    """
    Категория резюме
    """

    class Meta:
        verbose_name = "Категория Резюме"
        verbose_name_plural = "Категории Резюме"

    def __str__(self):
        return self.type

    type = models.CharField(max_length=100)


class CV(models.Model):
    """
    Резюме который заполняет пользоваетель
    """

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"

    def __str__(self):
        return self.Name

    Image = models.ImageField(upload_to='cv_photo/', blank=True)
    Name = models.CharField(max_length=100)
    Surname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    salary = models.BigIntegerField(blank=True)
    proffession = models.CharField(max_length=255, blank=True)
    work_exp = models.TextField(blank=True)
    education = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    about = models.TextField(blank=True)
    hobby = models.TextField(blank=True)


    type_cv = models.ForeignKey(CategoryCV, on_delete=models.CASCADE, null=True, )

    # Скрыты данные от пользователя на которые он не может повлиять
    date_of_creation = models.DateTimeField(auto_now_add=True)
