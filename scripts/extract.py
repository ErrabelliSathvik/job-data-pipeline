import requests
import json
import os

def run_extract():
    url = "https://remotive.com/api/remote-jobs"

    response = requests.get(url)
    data = response.json()

    jobs = []

    for job in data['jobs'][:30]:
        jobs.append({
            "title": job['title'],
            "company": job['company_name'],
            "location": job['candidate_required_location'],
            "skills": ", ".join(job['tags'])
        })

    os.makedirs("data", exist_ok=True)

    with open("data/raw_jobs.json", "w") as f:
        json.dump(jobs, f, indent=4)

    print(f"Extracted {len(jobs)} jobs!")

if __name__ == "__main__":
    run_extract()