# Generated by Django 4.1.3 on 2022-12-03 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evcars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='decision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(max_length=100)),
                ('primary', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
