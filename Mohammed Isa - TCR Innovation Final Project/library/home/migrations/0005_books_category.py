# Generated by Django 4.2.5 on 2023-10-11 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_books_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.CharField(choices=[('Novels', 'Novels'), ('Mangas', 'Mangas'), ('Short Stories', 'Short Stories'), ('Biography', 'Biography'), ('Self Help', 'Self Help')], default='Novels', max_length=20),
        ),
    ]
