# Generated by Django 4.1.4 on 2023-01-21 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0002_lead_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='converted',
            field=models.BooleanField(default=False),
        ),
    ]
