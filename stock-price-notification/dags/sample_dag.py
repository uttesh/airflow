from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import yfinance as yf
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email_credentials import EMAIL_ADDRESS, EMAIL_PASSWORD

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1
}

dag = DAG(
    'stock_price_notification',
    default_args=default_args,
    description='Check real-time stock prices and send email notification',
    schedule_interval='0 9 * * *'  # Run every day at 9 AM
)

def get_stock_prices():
    symbols = ["AAPL", "MSFT", "GOOGL", "AMZN"]
    stock_data = yf.download(symbols, period="1d")["Close"]
    return stock_data

def send_email(subject, body, recipients):
    sender_email = EMAIL_ADDRESS
    sender_password = EMAIL_PASSWORD
    
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = ", ".join(recipients)
    msg["Subject"] = subject
    
    msg.attach(MIMEText(body, "plain"))
    
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipients, msg.as_string())

def process_stock_prices():
    stock_prices = get_stock_prices()
    subject = "Daily Stock Prices - {}".format(datetime.now().strftime("%Y-%m-%d"))
    body = "Today's Stock Prices:\n\n{}".format(stock_prices)
    recipients = ["recipient1@example.com", "recipient2@example.com"]
    send_email(subject, body, recipients)

fetch_stock_prices_task = PythonOperator(
    task_id='fetch_stock_prices',
    python_callable=get_stock_prices,
    dag=dag
)

send_email_task = PythonOperator(
    task_id='send_email',
    python_callable=process_stock_prices,
    dag=dag
)

fetch_stock_prices_task >> send_email_task
