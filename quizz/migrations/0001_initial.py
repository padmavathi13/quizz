# Generated by Django 3.0.6 on 2020-05-24 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=150)),
                ('choice1', models.CharField(max_length=150)),
                ('choice2', models.CharField(max_length=150)),
                ('choice3', models.CharField(max_length=150)),
                ('choice4', models.CharField(max_length=150)),
                ('answer', models.CharField(max_length=150)),
            ],
        ),
    ]
