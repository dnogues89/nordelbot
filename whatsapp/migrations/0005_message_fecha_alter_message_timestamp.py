# Generated by Django 4.2.3 on 2023-08-09 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsapp', '0004_remove_message_recibido_alter_message_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.IntegerField(),
        ),
    ]
