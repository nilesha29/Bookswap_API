# Generated by Django 2.1.7 on 2019-05-06 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name_plural': 'Books'},
        ),
        migrations.AlterModelOptions(
            name='trades',
            options={'verbose_name_plural': 'Trades'},
        ),
        migrations.AddField(
            model_name='books',
            name='thumbnail',
            field=models.CharField(default='https://vinniefisher.com/wp-content/uploads/2016/07/CEOMindset-Book-Thumbnail-Listings.png', max_length=1000),
        ),
    ]
