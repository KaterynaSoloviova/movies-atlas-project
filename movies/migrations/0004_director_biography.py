# Generated by Django 5.1.2 on 2024-11-02 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_alter_actor_birthday_alter_director_birthday"),
    ]

    operations = [
        migrations.AddField(
            model_name="director",
            name="biography",
            field=models.TextField(null=True),
        ),
    ]