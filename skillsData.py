import os
import django
import pandas as pd
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

django.setup()

from jobSearch.models import Skills

DATA_DIR = Path(__file__).resolve().parent / "files"

files = [
    ("Essential Skills.csv", "Essential"),
    ("Software Skills.csv", "Software"),
    ("Transferable Skills.csv", "Transferable"),
]

# Keep track of skills already imported
seen_skills = set()

for filename, category in files:
    file_path = DATA_DIR / filename
    df = pd.read_csv(file_path)

    for _, row in df.iterrows():
        skill_name = str(row["Element Name"]).strip()

        # Skip duplicate skill names
        #if skill_name in seen_skills:
        #    continue

        #seen_skills.add(skill_name)

        Skills.objects.get_or_create(
            eleID=skill_name,
            #skillType=row["Element Name"],
            #title=row["Title"]
            #defaults={
            #    "skillType": skill_name,
            #    "category": category,
            #    "title": row["Title"],
            #}
            skillType=skill_name,
            category=category,
            title=row["Title"]
        )

    print(f"Imported {filename}")

print("All files imported successfully!")