# Generated by Django 5.1.7 on 2025-03-25 15:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('completed_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(blank=True, choices=[('active', 'Active'), ('pending', 'Pending'), ('cancelled', 'Cancelled'), ('completed', 'Completed'), ('on_hold', 'On Hold'), ('failed', 'Failed')], max_length=25, null=True)),
                ('task_type', models.CharField(choices=[('bug', 'Bug'), ('feature', 'Feature'), ('improvement', 'Improvement'), ('task', 'Task')], max_length=20, null=True)),
                ('users', models.ManyToManyField(related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
