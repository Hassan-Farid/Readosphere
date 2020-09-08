# Generated by Django 3.0.3 on 2020-09-06 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=255)),
                ('author_info', models.TextField(blank=True, null=True)),
                ('profile', models.FileField(upload_to='author/')),
            ],
            options={
                'db_table': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher_name', models.CharField(max_length=255)),
                ('publisher_loc', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'publishers',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=45)),
                ('isbn', models.IntegerField()),
                ('language', models.CharField(blank=True, max_length=45, null=True)),
                ('edition', models.CharField(blank=True, max_length=45, null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('cover', models.FileField(upload_to='cover/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Publisher')),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]