# Generated by Django 4.2.16 on 2024-12-15 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("investment_fund", "0005_investmentfund_join_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="investmentfund",
            name="category",
            field=models.CharField(
                choices=[("Stocks", "أسهم"), ("Real Estate", "عقارات")],
                default="Stocks",
                max_length=50,
            ),
        ),
    ]