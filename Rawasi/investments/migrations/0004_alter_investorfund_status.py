# Generated by Django 4.2.16 on 2024-12-17 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("investments", "0003_alter_voting_unique_together_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="investorfund",
            name="status",
            field=models.CharField(
                choices=[("Completed", "Completed"), ("Pending", "Pending")],
                default="Completed",
                max_length=100,
            ),
        ),
    ]
