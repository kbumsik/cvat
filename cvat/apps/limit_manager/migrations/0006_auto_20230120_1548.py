# Generated by Django 3.2.16 on 2023-01-20 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('limit_manager', '0005_limitation_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='limitation',
            name='job_export_dataset',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='limitation',
            name='project_export_dataset',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='limitation',
            name='task_export_dataset',
            field=models.PositiveIntegerField(null=True),
        ),
    ]