# Generated by Django 5.2 on 2025-06-09 12:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_question_is_approved'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='voted_user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
