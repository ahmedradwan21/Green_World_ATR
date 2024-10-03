# Generated by Django 4.2.11 on 2024-05-06 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_categoryplant_alter_plants_types_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryplant',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='categoryplant',
            name='image_of_category',
        ),
        migrations.AddField(
            model_name='categoryplant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_images/'),
        ),
        migrations.AlterField(
            model_name='categoryplant',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
