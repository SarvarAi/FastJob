# Generated by Django 4.1.6 on 2023-02-09 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryCV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Категория Резюме',
                'verbose_name_plural': 'Категории Резюме',
            },
        ),
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(blank=True, upload_to='cv_photo/')),
                ('Name', models.CharField(max_length=100)),
                ('Surname', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('salary', models.BigIntegerField(blank=True)),
                ('proffession', models.CharField(blank=True, max_length=255)),
                ('work_exp', models.TextField(blank=True)),
                ('education', models.TextField(blank=True)),
                ('skills', models.TextField(blank=True)),
                ('about', models.TextField(blank=True)),
                ('hobby', models.TextField(blank=True)),
                ('date_of_creation', models.DateTimeField(auto_now_add=True)),
                ('type_cv', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.categorycv')),
            ],
            options={
                'verbose_name': 'Резюме',
                'verbose_name_plural': 'Резюме',
            },
        ),
    ]