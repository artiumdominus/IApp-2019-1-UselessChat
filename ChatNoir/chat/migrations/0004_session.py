# Generated by Django 2.1.7 on 2019-06-23 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_message_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=44)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Person')),
            ],
        ),
    ]
