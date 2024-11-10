# Generated by Django 4.2.16 on 2024-11-09 23:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FoodDonation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("food_name", models.CharField(max_length=255)),
                (
                    "quantity",
                    models.IntegerField(
                        help_text="Quantity in servings or weight (e.g., 5 kg)"
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Vegetarian", "Vegetarian"),
                            ("Non-Vegetarian", "Non-Vegetarian"),
                            ("Vegan", "Vegan"),
                            ("Dessert", "Dessert"),
                            ("Other", "Other"),
                        ],
                        max_length=50,
                    ),
                ),
                ("expiry_date", models.DateField()),
                ("location", models.CharField(max_length=255)),
                (
                    "food_image",
                    models.ImageField(blank=True, null=True, upload_to="food_images/"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]