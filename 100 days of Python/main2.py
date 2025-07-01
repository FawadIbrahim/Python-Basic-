import pandas as pd
import smtplib
from email.message import EmailMessage
from email_validator import validate_email, EmailNotValidError
import getpass
import os

def read_emails(file_path):
    try:
        ext = os.path.splitext(file_path)[-1].lower()
        if ext == '.csv':
            df = pd.read_csv(file_path)
        elif ext in ['.xls', '.xlsx']:
            df = pd.read_excel(file_path, engine='openpyxl')  # install openpyxl if needed
        else:
            raise ValueError("Unsupported file format. Please use a .csv, .xls or .xlsx file.")

        if 'Email' not in df.columns:
            raise ValueError("The file must contain a column labeled 'Email'.")

        return df['Email'].dropna().tolist()

    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def send_email(to_email, subject, body, sender_email, sender_password):
    try:
        validate_email(to_email)

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = to_email
        msg.set_content(body)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)

        return True
    except (EmailNotValidError, smtplib.SMTPException, Exception) as e:
        print(f" Failed to send email to {to_email}: {e}")
        return False

def main():
    print("Bulk Email Sender (Console App)")
    file_path = input("Enter the path to the Excel or CSV file: ").strip()
    subject = input("Enter the email subject: ").strip()
    body = input("Enter the email body: ").strip()
    sender_email = input("Enter your email address (Gmail): ").strip()
    sender_password = getpass.getpass("Enter your email app password (input hidden): ")

    email_list = read_emails(file_path)
    if not email_list:
        print("No valid emails to process. Exiting.")
        return

    verified = []
    not_verified = []

    print("\n Sending emails...\n")
    for email in email_list:
        print(f"Sending to {email}...")
        if send_email(email, subject, body, sender_email, sender_password):
            verified.append(email)
        else:
            not_verified.append(email)

    pd.DataFrame({'Email': verified}).to_csv("verified.csv", index=False)
    pd.DataFrame({'Email': not_verified}).to_csv("not_verified.csv", index=False)

    print("\n Summary:")
    print(f" Emails sent successfully: {len(verified)}")
    print(f" Emails failed to send: {len(not_verified)}")
    print("Results saved to 'verified.csv' and 'not_verified.csv'.")

if __name__ == "__main__":
    main()
