# Generated by Django 5.1.2 on 2024-10-22 14:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=30, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=100, verbose_name='Название')),
                ('recipe_description', models.TextField(verbose_name='Описание')),
                ('ingredients', models.TextField(verbose_name='Ингредиенты')),
                ('stages_preparation', models.TextField(verbose_name='Этапы приготовления')),
                ('time_preparation', models.IntegerField(verbose_name='Время приготовления, мин.')),
                ('food_image', models.ImageField(blank=True, upload_to='food_images', verbose_name='Изображение')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.user', verbose_name='Автор')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.categories', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
    ]
