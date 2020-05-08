# Generated by Django 3.0.5 on 2020-05-08 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dessert',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=512)),
                ('category', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=16)),
                ('imageUrl', models.URLField()),
                ('notes', models.CharField(blank=True, max_length=512)),
                ('isAvailable', models.BooleanField(default=True, verbose_name='Is Available?')),
                ('spiceLevel', models.CharField(choices=[('NONE', 'None'), ('LOW', 'Low'), ('MED', 'Medium'), ('HIGH', 'High')], default='NONE', max_length=4)),
                ('allergens', models.ManyToManyField(blank=True, related_name='dessertallergens_ingredients', to='dishes.Ingredient')),
                ('ingredients', models.ManyToManyField(blank=True, related_name='dessertingredients_ingredient', to='dishes.Ingredient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Desert',
        ),
    ]
