# Generated by Django 4.2.11 on 2024-05-06 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPlant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Vegetables', 'Vegetables'), ('Leaf Plants', 'Leaf Plants'), ('Flowers', 'Flowers'), ('Fruits', 'Fruits'), ('Succulents', 'Succulents'), ('Weeds', 'Weeds'), ('Trees', 'Trees'), ('Toxic Plants', 'Toxic Plants')], max_length=200, verbose_name='name_of_category')),
                ('image_of_category', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='plants_types',
            name='category',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plants.categoryplant'),
        ),
    ]
