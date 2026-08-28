import csv
import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "backend.settings"
)

django.setup()

from jobSearch.models import Occupation

csv_path = os.path.join(
    "files",
    "Occupation Data.csv"
)

with open(csv_path, encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:

        Occupation.objects.get_or_create(
            jobTitle=row["Title"]
        )


print("Occupations loaded")