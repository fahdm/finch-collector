# Generated by Django 4.2.11 on 2024-04-25 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feeding'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=40)),
                ('size', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='finch',
            name='cages',
            field=models.ManyToManyField(to='main_app.cage'),
        ),
    ]