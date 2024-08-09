import os
import pandas as pd
import requests
import yfinance as yf
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Download stock prices
def download_stock_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period='1d')
    print(f"Downloaded data for {ticker}:")
    print(data)
    return data

# Process the data
def process_data(data):
    summary = data.describe()
    print("Processed data summary:")
    print(summary)
    return summary

# Send email with summary
def send_email(subject, body, recipient):
    # Credentials from environment variables
    sender_email = os.getenv("SENDER_MAIL")
    email_password = os.getenv("MAIL_PASS")  
    
    # Debugging prints to verify environment variables
    print(f"From Email: {sender_email}")          
    
    msg = MIMEMultipart("alternative")
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = subject
    
    # Attach both plain text and HTML versions of the email body
    text = f"{body}"
    html = f"""\
    <html>
      <body>
        <h1>{subject}</h1>
        <p>{body.replace('\n', '<br>')}</p>
      </body>
    </html>
    """
    
    msg.attach(MIMEText(text, "plain"))
    msg.attach(MIMEText(html, "html"))
    
    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login(sender_email, email_password)
        message = msg.as_string()
        server.sendmail(sender_email, recipient, message)
        server.quit()
        print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email: {e}")
    
def main():
    '''
    Coordinates the execution of the automation script
    '''
    ticker = "AAPL"
    data = download_stock_data(ticker)
    summary = process_data(data)
    
    subject = f"Daily stock summary for {ticker} - {datetime.now().strftime('%Y-%m-%d')}"
    body = f"Summary statistics:\n\n{summary}"
    
    recipient = "subhgogoi@gmail.com"
    send_email(subject, body, recipient)
    
if __name__ == "__main__":
    main()