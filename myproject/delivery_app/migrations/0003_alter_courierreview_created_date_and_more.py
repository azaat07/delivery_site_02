# Generated by Django 5.1.3 on 2024-11-26 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_app', '0002_category_category_name_en_category_category_name_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courierreview',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='storereview',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
