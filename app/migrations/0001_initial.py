# Generated by Django 4.1.7 on 2023-03-20 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('uid', models.CharField(max_length=100)),
                ('room_name', models.CharField(max_length=100)),
            ],
        ),
    ]
