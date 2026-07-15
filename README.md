# Retail Data Engineering Platform

An end-to-end retail data engineering pipeline that processes transactional data using Python, Apache Kafka, Apache Spark, Apache Airflow, MySQL, and Tableau.

The project demonstrates a modern data engineering workflow from data ingestion to analytics visualization.

---

## Project Overview

This project simulates a retail analytics platform that:

- Generates retail transaction data
- Ingests streaming data using Kafka
- Processes and transforms data using Spark
- Implements Bronze, Silver, and Gold data layers
- Orchestrates workflows using Apache Airflow
- Stores analytical data in MySQL
- Creates business dashboards using Tableau

---

# Architecture
             Retail Transactions
                     |
                     ↓
          Python Data Generator
                     |
                     ↓
                Apache Kafka
                     |
                     ↓
         Apache Spark Processing
                     |
    --------------------------------
    |              |               |
    ↓              ↓               ↓
 Bronze         Silver          Gold
  Layer          Layer           Layer
    |              |               |
    --------------------------------
                     |
                     ↓
              MySQL Data Warehouse
                     |
                     ↓
          Tableau Analytics Dashboard

---

# Technology Stack

## Programming
- Python
- SQL

## Data Engineering
- Apache Kafka
- Apache Spark
- Apache Airflow
- Docker

## Database
- MySQL

## Analytics & Visualization
- Tableau

## Development Tools
- Git
- GitHub
- VS Code

---

# Data Pipeline

## 1. Data Generation

Synthetic retail transaction data is generated using Python.

Sample attributes:

- Transaction ID
- Customer ID
- Product ID
- Product Category
- Amount
- Payment Method
- Store Location
- Timestamp

---

## 2. Data Streaming

Apache Kafka is used for real-time transaction ingestion.

Flow:
Python Producer
|
↓
Kafka Topic
|
↓
Spark Consumer


---

## 3. Data Processing

Apache Spark performs:

- Data cleaning
- Schema validation
- Transformation
- Aggregations

Data is organized into:

### Bronze Layer
Raw ingested data

### Silver Layer
Cleaned and transformed data

### Gold Layer
Business-ready analytical datasets

---

## 4. Workflow Orchestration

Apache Airflow manages pipeline execution.

Pipeline tasks:
Generate Data
↓
Transform Data
↓
Load Analytics Data

---

# Database Design

MySQL database:
retail_db
|
└── sales_transactions

Table columns:

| Column | Description |
|---|---|
| transaction_id | Transaction identifier |
| customer_id | Customer identifier |
| product_id | Product identifier |
| amount | Sales amount |
| timestamp | Transaction timestamp |
| transaction_time | Processed datetime |
| revenue_category | Revenue classification |

---

# Tableau Dashboard

The final analytics layer provides:

## Retail Sales Analytics Dashboard

Features:

- Total Revenue KPI
- Revenue by Product Category
- Sales Trend Over Time

Dashboard insights:

- Revenue performance
- Product category analysis
- Sales patterns

---

# Project Structure
retail-data-engineering-platform

├── airflow
│ └── dags

├── dashboards
│ └── Tableau dashboards

├── data
│ ├── raw
│ ├── silver
│ └── gold

├── docker
│ └── Kafka containers
├── kafka
│ └── producer scripts

├── spark
│ └── Spark processing

├── sql
│ └── SQL scripts

├── src
│ ├── ingestion
│ └── transformation

├── tests

├── requirements.txt
└── README.md
---

# How to Run the Project

## Clone Repository

```bash
git clone https://github.com/Anitharaj31/retail-data-engineering-platform.git

Create Environment
python3 -m venv venv

source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Start Services

Docker:
docker compose up -d

Run Airflow:
airflow webserver
airflow scheduler
Key Skills Demonstrated
Data Engineering Pipelines
ETL Development
Streaming Data Processing
Data Warehousing
Data Modeling
Workflow Orchestration
Business Intelligence Analytics

Future Enhancements
Deploy pipeline on AWS
Add AWS S3 data lake
Add AWS Glue ETL jobs
Add Amazon Athena analytics
Implement CI/CD pipeline
Add monitoring with Grafana

Author

Anitha Raj Bale
