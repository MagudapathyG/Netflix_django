# Generated by Django 4.2.1 on 2023-06-03 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflixapp', '0005_delete_myperson_delete_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='age_limit',
            field=models.CharField(choices=[('Mens', 'Mens'), ('Kids', 'Kids')], max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age_limit',
            field=models.CharField(choices=[('Mens', 'Mens'), ('Kids', 'Kids')], max_length=10),
        ),
    ]