# Generated by Django 4.1.3 on 2022-11-23 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='example',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('meaning', models.CharField(max_length=30)),
                ('example', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='new_thing_ithink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new', models.CharField(max_length=30)),
                ('example', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='new_thing_me_too',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new', models.CharField(max_length=30)),
                ('example', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='phrase_afraid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phrase', models.CharField(max_length=30)),
                ('meaning', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='phrase_off',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phrase', models.CharField(max_length=30)),
                ('meaning', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='phrase_say',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phrase', models.CharField(max_length=30)),
                ('meaning', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='verb_airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verb', models.CharField(max_length=30)),
                ('meaning', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='verb_court',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verb', models.CharField(max_length=30)),
                ('meaning', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='verb_hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verb', models.CharField(max_length=30)),
                ('meaning', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='verb_restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verb', models.CharField(max_length=30)),
                ('meaning', models.CharField(max_length=30)),
            ],
        ),
    ]
