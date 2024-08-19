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
    """
    Downloads and returns stock price data for a specific ticker symbol
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period='1d')
    print(f"Downloaded data for {ticker}:")
    print(data)
    return data

def get_full_name(ticker):
    """
    Returns the full company name of a ticker symbol
    """
    stock = yf.Ticker(ticker)
    company_name = stock.info.get("longName", ticker)
    return company_name


# Process the data
def process_data(data):
    summary = data.describe()
    print("Processed data summary:")
    print(summary)
    return summary

    
def toHtml(summary):
    """
    Converts the summary dataframe to an html table
    """
    return summary.to_html()

# Send email with summary
def send_email(subject, body, recipient, ticker, company):
    # Credentials from environment variables
    sender_email = os.getenv("SENDER_MAIL")
    email_password = os.getenv("MAIL_PASS")  
    
    # Debugging prints to verify environment variables
    print(f"From Email: {sender_email}")          
    
    msg = MIMEMultipart("alternative")
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = subject
    
   # Plain text version
    text = f"{body}"
    
    # HTML version with an HTML table
    html = f"""\
    <html>
      <body>
        <p>Hello,</p>
        <p>Here is your daily stock summary for {company} as of {datetime.now().strftime('%Y-%m-%d')}:</p>
        {body}
        <p>Best regards,<br>Your Stock Automation System</p>
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
    company_name = get_full_name(ticker)
    data = download_stock_data(ticker)
    summary = process_data(data)
    
    subject = f"Daily stock summary for {company_name} ({ticker}) - {datetime.now().strftime('%Y-%m-%d')}"
    formatted_summary = toHtml(summary)
    body = f"""
    {formatted_summary}
    """
    recipient = "subhgogoi@gmail.com"
    send_email(subject, body, recipient, ticker, company_name)
    
if __name__ == "__main__":
    main()