import csv
import os
from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def download_csv(url, file_name):
    local_path = os.path.join('/Users/macbook/Desktop/7. Python/input_downloaded_files', file_name)
    with urlopen(url) as image, open(local_path, 'wb') as f:
        f.write(image.read())

#1 Download CSV files
urls = [
    ('https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1587042293&period2=1618578293&interval=1d&events=history&includeAdjustedClose=true', 'GOOG.csv'),
    ('https://query1.finance.yahoo.com/v7/finance/download/IBM?period1=0&period2=9999999999&interval=1d&events=history', 'IBM.csv'),
    ('https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=0&period2=9999999999&interval=1d&events=history', 'MSFT.csv')
]

for url, file_name in urls:
    download_csv(url, file_name)

#2,3 Calculates the percentage change between Close and Open price
def calculate_change(open_price, close_price):
    change = ((float(close_price) - float(open_price)) / float(open_price)) * 100
    return round(change,2)

#4 Add change values as another column to this CSV file and the output files can be stored in another folder
def process_csv_files(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            with open(os.path.join(input_folder, filename), 'r') as file:
                reader = csv.DictReader(file)
                rows = list(reader)
                header = reader.fieldnames + ['Change']

                for row in rows:
                    change = calculate_change(row['Open'], row['Close'])
                    row['Change'] = f"{change}%"

                output_file = os.path.join(output_folder, filename)
                with open(output_file, 'w', newline='') as output:
                    writer = csv.DictWriter(output, fieldnames=header)
                    writer.writeheader()
                    writer.writerows(rows)

#5 Apply
input_folder = '/Users/macbook/Desktop/7. Python/input_downloaded_files'
output_folder = '/Users/macbook/Desktop/7. Python/output_files'
process_csv_files(input_folder, output_folder)
