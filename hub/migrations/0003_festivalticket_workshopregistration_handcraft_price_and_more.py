# Generated by Django 5.1.3 on 2025-06-15 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='FestivalTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tickets', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkshopRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='handcraft',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='handcraft',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='handcraft',
            name='image',
            field=models.ImageField(upload_to='handcraft_images/'),
        ),
        migrations.AlterField(
            model_name='handcraft',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
