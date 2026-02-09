# Support Ticket Data Pipeline

## Overview
This project demonstrates an **end-to-end Python data pipeline** for support-oriented workflows.  
It includes **data extraction, transformation, validation, and reporting**, with a focus on **scalable and maintainable pipelines**.

## Features
- Automated ETL pipeline: Extract → Transform → Validate → Report
- Handles **50+ tickets daily** in a mock dataset
- Detects **duplicate or missing data** and logs anomalies
- Generates **reports for non-technical audiences**
- Easily extendable for **production use** (scheduling, notifications)

## File Structure
support-ticket-data-pipeline/
│
├── data/                        # CSVs (optional for GitHub; or include sample CSVs)
│   └── raw_tickets.csv
│
├── data/output/                 # leave empty or include sample reports
│
├── generate_csv.py               # Script to create mock data
├── support_pipeline.py           # Main pipeline code
└── README.md                     # Explains the project
