# Generated by Django 4.2.11 on 2024-05-06 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0005_attributes_category_care_guide_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attributes',
            name='category',
        ),
        migrations.RemoveField(
            model_name='care_guide',
            name='category',
        ),
        migrations.RemoveField(
            model_name='scientific_classification',
            name='category',
        ),
    ]
