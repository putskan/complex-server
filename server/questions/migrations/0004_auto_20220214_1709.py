# Generated by Django 3.2.12 on 2022-02-14 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20220212_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='solution_text',
            field=models.TextField(blank=True),
        ),
    ]
