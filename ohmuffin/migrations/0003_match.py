# Generated by Django 3.2.10 on 2021-12-10 02:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ohmuffin', '0002_auto_20211208_2039'),
    ]

    operations = [
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
