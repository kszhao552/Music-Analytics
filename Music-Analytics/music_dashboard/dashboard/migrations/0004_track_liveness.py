# Generated by Django 3.2.3 on 2021-05-20 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_rename_dancibility_track_danceability'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='liveness',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=7),
            preserve_default=False,
        ),
    ]