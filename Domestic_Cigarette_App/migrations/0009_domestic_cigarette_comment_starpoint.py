# Generated by Django 3.0.8 on 2020-07-15 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Domestic_Cigarette_App', '0008_remove_domestic_cigarette_comment_starpoint'),
    ]

    operations = [
        migrations.AddField(
            model_name='domestic_cigarette_comment',
            name='StarPoint',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
