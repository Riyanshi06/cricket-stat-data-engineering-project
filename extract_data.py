import requests
import csv

url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen'
headers = {
     "X-RapidAPI-Key": "33f26feceamshb79997f8d5ab7dbp1c1f6bjsn8d43281039e6", # Replace with your RapidAPI key
    'X-RapidAPI-Host': 'cricbuzz-cricket.p.rapidapi.com'
}
params = {
    'formatType': 'odi'
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json().get('rank', [])  # Extracting the 'rank' data
    csv_filename = 'batsmen_rankings.csv'

    if data:
        field_names = ['rank', 'name', 'country']  # Specify required field names

        # Write data to CSV file with only specified field names
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            #writer.writeheader()
            for entry in data:
                writer.writerow({field: entry.get(field) for field in field_names})

        print(f"Data fetched successfully and written to '{csv_filename}'")
    else:
        print("No data available from the API.")

else:
    print("Failed to fetch data:", response.status_code)