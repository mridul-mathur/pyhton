import re
import schedule
import time
from sms_reader import get_sms
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# Set up Google Sheets API credentials and service
# Replace 'YOUR_CLIENT_ID.json' with your actual credentials JSON file
creds = Credentials.from_authorized_user_file('YOUR_CLIENT_ID.json', ['https://www.googleapis.com/auth/spreadsheets'])
service = build('sheets', 'v4', credentials=creds)
spreadsheet_id = 'YOUR_SPREADSHEET_ID'


def extract_transaction_data(sms_text):
    # Implement your SMS parsing logic here
    pass


def update_google_sheet(credited_total, debited_total):
    # Implement your Google Sheets update logic here
    pass


def process_sms_and_update_sheet():
    sms_messages = get_sms(address='bank_number', count=50)
    credited_total = 0
    debited_total = 0

    for sms in sms_messages:
        credited_amounts, debited_amounts = extract_transaction_data(sms['body'])
        credited_total += sum(credited_amounts)
        debited_total += sum(debited_amounts)

    update_google_sheet(credited_total, debited_total)


def main():
    schedule.every(1).hour.do(process_sms_and_update_sheet)  # Run every hour

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()