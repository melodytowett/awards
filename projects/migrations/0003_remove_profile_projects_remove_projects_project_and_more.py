# Generated by Django 4.0.3 on 2022-04-08 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_profile_user_projects_project_alter_profile_projects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Projects',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='project',
        ),
        migrations.AddField(
            model_name='projects',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projects',
            name='link',
            field=models.URLField(),
        ),
    ]
