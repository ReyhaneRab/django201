# Generated by Django 5.1 on 2024-08-15 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category_name'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
