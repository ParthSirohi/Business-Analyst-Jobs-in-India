import os
import json

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Job Listings</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f8f9fa; padding: 20px; }
        h1 { text-align: center; color: #333; }
        .job-card { background-color: white; margin: 10px auto; padding: 15px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); width: 80%; border-radius: 8px; }
        .job-title { font-size: 1.5em; color: #007bff; }
        .job-company { font-weight: bold; color: #555; }
        .job-location { color: #888; margin: 5px 0; }
        .job-description { margin: 10px 0; }
        .job-link { display: inline-block; padding: 5px 10px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px; }
        .job-link:hover { background-color: #0056b3; }
    </style>
</head>
<body>
    <h1>Latest Job Listings</h1>
    {jobs}
</body>
</html>
"""

def generate_html():
    jobs_folder = 'jobs'
    job_html = ""

    if not os.path.exists(jobs_folder):
        print(f"No '{jobs_folder}' folder found.")
        return

    for file in os.listdir(jobs_folder):
        if file.endswith('.json'):
            with open(os.path.join(jobs_folder, file), 'r') as json_file:
                try:
                    job = json.load(json_file)
                    job_html += f"""
                    <div class="job-card">
                        <div class="job-title">{job['title']}</div>
                        <div class="job-company">{job['company']}</div>
                        <div class="job-location">{job['location']}</div>
                        <div class="job-description">{job['description'][:300]}...</div>
                        <a class="job-link" href="{job['link']}" target="_blank">View on LinkedIn</a>
                    </div>
                    """
                except json.JSONDecodeError:
                    continue

    with open("index.html", "w", encoding="utf-8") as html_file:
        html_file.write(HTML_TEMPLATE.replace("{jobs}", job_html))

    print("✅ index.html generated successfully!")

if __name__ == "__main__":
    generate_html()
