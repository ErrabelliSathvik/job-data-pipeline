import pandas as pd
import json
import os
from collections import Counter

def run_transform():
    # Load raw data
    with open("data/raw_jobs.json", "r") as f:
        jobs = json.load(f)

    df = pd.DataFrame(jobs)

    # ---- CLEANING ----

    # Lowercase everything
    df['title'] = df['title'].str.lower()
    df['company'] = df['company'].str.lower()
    df['location'] = df['location'].str.lower()

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Handle skills (convert string → list)
    def clean_skills(skill_str):
        if not skill_str:
            return []
        skills = skill_str.lower().split(",")
        skills = [s.strip() for s in skills if s.strip()]
        return list(set(skills))

    df['skills'] = df['skills'].apply(clean_skills)

    # Remove rows with missing important data
    df.dropna(subset=['title', 'company'], inplace=True)

    # ---- TOP SKILLS ANALYSIS ----
    all_skills = [skill for sublist in df['skills'] for skill in sublist]
    print("Top 10 skills:")
    print(Counter(all_skills).most_common(10))

    # ---- SAVE CLEAN DATA ----
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/clean_jobs.csv", index=False)

    print(f"Transformed {len(df)} clean jobs!")

if __name__ == "__main__":
    run_transform()