# Generated by Django 3.2.10 on 2021-12-10 06:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Interest',
                'verbose_name_plural': 'Interests',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('slack_id', models.CharField(max_length=200)),
                ('interests', models.ManyToManyField(related_name='interests', to='ohmuffin.Interest')),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('interests', models.ManyToManyField(related_name='matches', to='ohmuffin.Interest')),
                ('profiles', models.ManyToManyField(related_name='matches', to='ohmuffin.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
