# Generated by Django 3.0.7 on 2020-06-25 13:31

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('projects', '0001_squashed_0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='stack',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]