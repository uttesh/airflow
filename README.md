# airflow

Apache Airflow learning sample and realtime examples

# Real-time Stock Price Checking and Email Notification with Apache Airflow

This project demonstrates how to use Apache Airflow to check real-time stock prices every morning at 9 AM and send an email notification with the latest stock prices to predefined recipients.

## Prerequisites

- Docker
- Docker Compose

## Build and Run Instructions

1. Clone this repository:

```bash
git clone https://github.com/uttesh/airflow.git
cd stock-price-notification
```

2. Update sample_dag.py with your email credentials and recipient addresses.

```
> pip install yfinance
```

3. Run the following command to build and start the Docker containers:

```
docker-compose up -d --build

```

or ### Manual download and install Airflow

```
> curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.8.2/docker-compose.yaml'
> curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.8.2/airflow.sh'
> chmod +x airflow.sh
> ./airflow.sh info
> docker-compose up -d --build
```

Access the Apache Airflow UI at http://localhost:8080 in your browser. The default account has the login airflow and the password airflow.

In the Airflow UI, enable the stock_price_notification DAG and trigger a manual run.

## Configuration

- sample_dag.py: Contains the Apache Airflow DAG definition.
- docker-compose.yml: Docker Compose configuration file for running Apache Airflow and PostgreSQL containers.
