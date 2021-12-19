# Generated by Django 3.2.6 on 2021-08-27 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('subject', models.CharField(max_length=264)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subcribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=254)),
                ('subcribe_day', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('author', models.CharField(max_length=250)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('content', models.TextField()),
                ('public_day', models.DateField()),
                ('image', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='stories.category')),
            ],
        ),
    ]
