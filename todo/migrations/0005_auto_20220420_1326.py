# Generated by Django 2.2.24 on 2022-04-20 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20220420_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='is_active',
            field=models.CharField(choices=[('A', 'active'), ('D', 'done')], default='A', max_length=20),
        ),
    ]
