\# Job Market Data Pipeline



\## Overview

Built an automated ETL pipeline to collect, process, and store job market data using Python and cloud database integration.



\## Features

\- Extracts job data from public API

\- Cleans and normalizes job information

\- Stores data in Supabase (PostgreSQL)

\- Handles duplicate records using unique constraints

\- Fully automated pipeline execution



\## Tech Stack

\- Python

\- Pandas

\- REST APIs

\- Supabase (PostgreSQL)



\## Architecture

Extract → Transform → Load → Cloud DB



\## How to Run

```bash

python -m pipeline.main\_pipeline

