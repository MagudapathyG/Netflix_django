# Generated by Django 4.2.1 on 2023-06-01 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netflixapp', '0003_remove_customer_contactinfo_ptr_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='myperson',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='netflixapp.person')),
            ],
            bases=('netflixapp.person',),
        ),
    ]