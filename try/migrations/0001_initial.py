# Generated by Django 4.0.3 on 2022-04-06 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchingBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(max_length=150, verbose_name='Название_ru')),
                ('title_ru_low', models.CharField(max_length=150, verbose_name='Название_ru')),
                ('title_en', models.CharField(max_length=150, verbose_name='Название_en')),
                ('title_en_low', models.CharField(max_length=150, verbose_name='Название_en')),
                ('book_author', models.CharField(max_length=150, verbose_name='Автор')),
                ('anons', models.CharField(max_length=250, verbose_name='Превью')),
                ('icon', models.ImageField(blank=True, upload_to='try/Textonator/media/')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
