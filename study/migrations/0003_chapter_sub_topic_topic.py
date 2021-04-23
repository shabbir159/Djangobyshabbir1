# Generated by Django 3.2 on 2021-04-14 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_qa_ans'),
    ]

    operations = [
        migrations.CreateModel(
            name='chapter',
            fields=[
                ('id', models.CharField(blank=True, max_length=25, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='sub_topic',
            fields=[
                ('t_id', models.CharField(blank=True, max_length=25)),
                ('s_id', models.CharField(blank=True, max_length=25, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('meaning', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='topic',
            fields=[
                ('id', models.CharField(blank=True, max_length=25)),
                ('t_id', models.CharField(blank=True, max_length=25, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('meaning', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
    ]
