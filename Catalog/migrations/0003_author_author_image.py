# Generated by Django 4.1.6 on 2023-02-24 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0002_bookinstance_borrower'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='author_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
