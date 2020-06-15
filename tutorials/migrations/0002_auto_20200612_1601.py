# Generated by Django 3.0.7 on 2020-06-12 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='Image',
            field=models.ImageField(default='', upload_to='image/'),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='code',
            field=tinymce.models.HTMLField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='highlighted',
            field=models.TextField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutorials', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
