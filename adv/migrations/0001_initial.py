# Generated by Django 4.0.3 on 2022-04-07 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название статьи')),
                ('anons', models.CharField(max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Полный текст')),
                ('date', models.DateField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Статья от рекламодателя',
                'verbose_name_plural': 'Статьи от рекламодателя',
            },
        ),
    ]
