# Generated by Django 4.1.1 on 2022-12-13 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_customer_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='imagen',
            field=models.ImageField(default=None, null=True, upload_to='static/assets/user/'),
        ),
    ]
