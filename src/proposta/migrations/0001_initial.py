# Generated by Django 5.1.6 on 2025-02-18 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proposta',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('component_id', models.IntegerField(unique=True)),
                ('created_at', models.DateTimeField(default='2000-01-01 00:00:00.000000')),
                ('updated_at', models.DateTimeField(default='2000-01-01 00:00:00.000000')),
                ('votes_count', models.IntegerField(default=0)),
                ('title', models.CharField(default='Proposal not found', max_length=1000)),
                ('body', models.CharField(default='Proposal not found', max_length=50000)),
                ('comments_count', models.IntegerField(default=0)),
                ('topic', models.CharField(default='Proposal not found', max_length=1000)),
            ],
        ),
    ]
