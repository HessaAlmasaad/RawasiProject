# Generated by Django 5.1.4 on 2024-12-12 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='leader',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
