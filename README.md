# Spotify End-to-End Data Engineering ETL Project

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline for Spotify data using AWS services. It involves extracting data from the Spotify API, transforming the data, and loading it into an S3 bucket. The transformed data is organized into different folders (`album`, `songs`, and `artist`) for analysis through AWS Glue and Athena.

---

## Project Architecture

### 1. **Extraction**
- **Lambda Function**: `spotify_api_data_extract`
  - **Purpose**: Fetch data from the Spotify API.
  - **Triggers**: Scheduled daily via **Amazon CloudWatch Events**.
  - **Output**: JSON files stored in an S3 bucket.

### 2. **Transformation and Loading**
- **Lambda Function**: `spotify_transformation_load_function`
  - **Purpose**: Transform raw JSON data into structured CSV files.
  - **Triggers**: Triggered by the **S3 Object Put Event**.
  - **Output**: 
    - CSV files stored in specific folders (`album`, `songs`, `artist`) within the S3 bucket.

### 3. **Data Cataloging**
- **AWS Glue Crawlers**:
  - Created crawlers for `album`, `songs`, and `artist` data.
  - Crawlers update the schema and populate the **`spotify_db`** database.

### 4. **Data Analysis**
- **Amazon Athena**:
  - Queries the `spotify_db` database for insights.
  - Provides an SQL interface for analyzing Spotify data.

---

## Project Workflow

1. **Extract**:
   - Daily trigger pulls data from the Spotify API.
   - Data is saved as JSON files in the S3 bucket.

2. **Transform & Load**:
   - JSON files trigger `spotify_transformation_load_function`.
   - Data is cleaned, structured, and saved as CSV files in `album`, `songs`, and `artist` folders in the S3 bucket.

3. **Catalog**:
   - AWS Glue Crawlers scan the S3 bucket to create/update the schema in the `spotify_db`.

4. **Analyze**:
   - Use Amazon Athena to query and visualize the data.

---

## AWS Services Used

| Service         | Purpose                                                                 |
|-----------------|-------------------------------------------------------------------------|
| **Lambda**      | Serverless functions for data extraction and transformation            |
| **S3**          | Data storage for raw JSON and processed CSV files                      |
| **CloudWatch**  | Scheduler for daily API data extraction                                |
| **AWS Glue**    | Data cataloging with crawlers and schema creation                      |
| **Amazon Athena** | SQL-based data querying for analysis                                 |

---

## Folder Structure

```plaintext
spotify-end-to-end-data-engineer-etl-project/
├── lambda/
│   ├── spotify_api_data_extract.py        # Lambda function for data extraction
│   ├── spotify_transformation_load_function.py  # Lambda function for data transformation and loading
├── data/
│   ├── raw/                               # Raw JSON data from Spotify API
│   ├── processed/
│       ├── album/                         # CSV files for album data
│       ├── songs/                         # CSV files for song data
│       ├── artist/                        # CSV files for artist data
├── README.md                              # Project documentation


