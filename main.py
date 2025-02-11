import csv
from datetime import datetime

input_file = 'NetflixViewingHistory.csv'
output_file = 'letterboxd_import.csv'

def process_netflix_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8-sig') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        fieldnames = ['Title', 'Year', 'WatchedDate']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in reader:
            title, date = row[0], row[1]
            year = '' 
            watched_date = datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d')

            writer.writerow({'Title': title.strip(), 'Year': year, 'WatchedDate': watched_date})
process_netflix_csv(input_file, output_file)

print(f"Conversion completed. The new file is saved as {output_file}")
