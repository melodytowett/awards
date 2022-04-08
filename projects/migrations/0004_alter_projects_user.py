# Generated by Django 4.0.3 on 2022-04-08 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_remove_profile_projects_remove_projects_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL),
        ),
    ]