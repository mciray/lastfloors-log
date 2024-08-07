# Generated by Django 5.0.3 on 2024-04-16 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0004_logentry_response_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='logentry',
            name='exception',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='logentry',
            name='file_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='logentry',
            name='function_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='logentry',
            name='ip_address',
            field=models.CharField(blank=True, max_length=45),
        ),
        migrations.AddField(
            model_name='logentry',
            name='line_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='logentry',
            name='query_params',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='logentry',
            name='traceback',
            field=models.TextField(blank=True),
        ),
    ]
