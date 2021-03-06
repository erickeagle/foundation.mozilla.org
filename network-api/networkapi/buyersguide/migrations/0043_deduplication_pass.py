# Generated by Django 2.2.12 on 2020-04-09 20:09

from django.db import migrations, models
import django.db.models.deletion

def deduplicate(apps, schema_editor):
    models = [
        apps.get_model("buyersguide", "BaseRangeProductVote"),
        apps.get_model("buyersguide", "BaseBooleanProductVote"),
    ]

    for Model in models:
        for instance in Model.objects.filter(votes=0):
            if Model.objects.filter(product=instance.product).count() > 1:
                instance.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('buyersguide', '0042_auto_20200416_1946'),
    ]

    operations = [
        migrations.RunPython(deduplicate, migrations.RunPython.noop),
    ]
