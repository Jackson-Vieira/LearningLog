# Generated by Django 4.0.6 on 2022-07-30 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0007_topic_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static'),
        ),
    ]
