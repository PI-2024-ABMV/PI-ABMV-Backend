# Generated by Django 5.0.6 on 2024-11-23 01:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_remove_filme_categoria_ingresso_filme_categoria"),
    ]

    operations = [
        migrations.CreateModel(
            name="Carrinho",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("quantidade", models.IntegerField()),
                ("ingresso", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="core.ingresso")),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="carrinho",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="core.carrinho"),
        ),
    ]
