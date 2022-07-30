# Generated by Django 4.0.6 on 2022-07-30 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_topic_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='text',
            new_name='name',
        ),
        migrations.AddField(
            model_name='topic',
            name='description',
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]