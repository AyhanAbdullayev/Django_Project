# Generated by Django 5.1.1 on 2024-10-26 21:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Calory', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Calory',
                'verbose_name_plural': 'Calories',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=190, null=True)),
                ('Image', models.ImageField(upload_to='Images/')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rating', models.FloatField(null=True)),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
            },
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=180, null=True)),
            ],
            options={
                'verbose_name': 'Type',
                'verbose_name_plural': 'Types',
            },
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Name', models.CharField(max_length=200)),
                ('Count', models.IntegerField()),
                ('Price', models.IntegerField()),
                ('Image', models.ImageField(upload_to='Images/')),
                ('Calories', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Menu.calories')),
                ('Categorie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Menu.categories')),
                ('Rating', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Menu.ratings')),
                ('Type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Menu.types')),
            ],
            options={
                'verbose_name': 'Meal',
                'verbose_name_plural': 'Meals',
                'ordering': ['Created_at'],
            },
        ),
        migrations.CreateModel(
            name='Meal_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='Images/')),
                ('Meal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image', to='Menu.meals')),
            ],
            options={
                'verbose_name': 'Meal_Image',
                'verbose_name_plural': 'Meal_Images',
            },
        ),
    ]