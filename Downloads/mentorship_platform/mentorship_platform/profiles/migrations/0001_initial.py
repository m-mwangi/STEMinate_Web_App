# Generated by Django 5.0.7 on 2024-08-01 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('expertise', models.CharField(blank=True, max_length=255, null=True)),
                ('goals', models.CharField(blank=True, max_length=255, null=True)),
                ('mentorship_preferences', models.CharField(blank=True, max_length=255, null=True)),
                ('availability', models.CharField(blank=True, max_length=255, null=True)),
                ('preferred_communication_methods', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
