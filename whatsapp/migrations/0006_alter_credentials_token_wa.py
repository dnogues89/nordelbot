# Generated by Django 4.2.3 on 2023-08-10 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsapp', '0005_message_fecha_alter_message_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentials',
            name='token_wa',
            field=models.CharField(max_length=500),
        ),
    ]
