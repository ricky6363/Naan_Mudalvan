

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0002_song_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='credit',
            field=models.CharField(default='', max_length=100000),
        ),
    ]
