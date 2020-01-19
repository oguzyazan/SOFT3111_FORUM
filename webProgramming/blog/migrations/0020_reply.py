# Generated by Django 3.0 on 2019-12-24 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_delete_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('replyId', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.User')),
            ],
        ),
    ]