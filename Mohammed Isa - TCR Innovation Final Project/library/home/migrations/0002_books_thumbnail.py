# Generated by Django 4.2.5 on 2023-10-05 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='thumbnail',
            field=models.ImageField(default="{% static 'Default_Thumbnail.jpg' %}", upload_to='images/'),
        ),
    ]