# Generated by Django 4.1.1 on 2022-09-29 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='KitchenTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('weight', models.FloatField(max_length=20)),
                ('ingredient1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingr1', to='restoraunt_app.ingredients')),
                ('ingredient2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingr2', to='restoraunt_app.ingredients')),
                ('ingredient3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingr3', to='restoraunt_app.ingredients')),
                ('kitchen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restoraunt_app.kitchentypes')),
            ],
        ),
    ]
