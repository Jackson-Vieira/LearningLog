# Generated by Django 4.1.1 on 2022-09-07 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0015_alter_topic_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='heading',
            field=models.CharField(blank=True, max_length=50, verbose_name='heading'),
        ),
    ]
