import os
import django
import pandas as pd

# IMPORTANT: change this to your project settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from jobSearch.models import Occupation

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "files", "Occupation Data.csv")
df = pd.read_csv(file_path)

for _, row in df.iterrows():
    Occupation.objects.create(
        SOC=row["O*NET-SOC Code"],
        jobTitle=row["Title"]
    )

print("Import complete")