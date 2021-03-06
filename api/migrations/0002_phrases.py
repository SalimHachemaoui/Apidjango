# Generated by Django 3.0.2 on 2021-03-28 22:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phrases',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Francais')),
                ('phrase', models.CharField(max_length=500, verbose_name='Kabyle')),
            ],
        ),
    ]
