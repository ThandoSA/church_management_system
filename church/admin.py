from django.contrib import admin
from .models import *  # Assuming all your models are defined in models.py

# Register all models in the admin site
models = [
    'Model1',  # Replace with your actual model names
    'Model2',  # Add more model names as needed
    # Add more models as needed
]

for model in models:
    admin.site.register(model)