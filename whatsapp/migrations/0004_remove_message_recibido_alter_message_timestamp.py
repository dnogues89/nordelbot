# Generated by Django 4.2.3 on 2023-08-09 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsapp', '0003_message_recibido_alter_message_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='recibido',
        ),
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
