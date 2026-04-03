import requests
import pandas as pd

# 🔴 your values
url = "https://dchqhzztbqruurinnvsh.supabase.co"
key = "sb_publishable_H8PYEnlLYWKTJuIf0-CsYg_G8ZmMi6G"

def run_load():
    df = pd.read_csv("data/clean_jobs.csv")

    print(f"Loaded {len(df)} rows from CSV")

    # Convert skills string → list
    df['skills'] = df['skills'].apply(lambda x: eval(x) if isinstance(x, str) else [])

    data = df.to_dict(orient="records")

    headers = {
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "Prefer": "resolution=ignore-duplicates"
    }

    response = requests.post(
        f"{url}/rest/v1/jobs",
        headers=headers,
        json=data
    )

    print("Status:", response.status_code)
    print("Response:", response.text)

if __name__ == "__main__":
    run_load()