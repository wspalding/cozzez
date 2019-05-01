# Generated by Django 2.1.7 on 2019-05-01 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affiliation', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('title', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('source_url', models.URLField(null=True)),
                ('media_url', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news_collector.Article')),
            ],
            options={
                'ordering': ['-score'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('articles', models.ManyToManyField(related_name='related_articles', to='news_collector.Article')),
                ('label1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='top_label', to='news_collector.Label')),
                ('label2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='middle_label', to='news_collector.Label')),
                ('label3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bottom_label', to='news_collector.Label')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='topic',
            field=models.ManyToManyField(to='news_collector.Topic'),
        ),
    ]
