# Real-Time Data Warehouse and Analysis Project
## I'm working on it: this project is not finished yet
## Overview

This project focuses on building a real-time data warehouse and performing data analysis on streaming financial data. The pipeline involves extracting data from the Finnhub API, processing it using Apache Kafka and Apache Spark, storing it in a distributed data warehouse (Hadoop HDFS), training a time series model to predict closing prices, and visualizing real-time data using Power BI.

## Table of Contents

- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Data Flow](#data-flow)
- [Time Series Model](#time-series-model)
- [Real-Time Visualization](#real-time-visualization)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project integrates various technologies to create a robust data processing and analysis pipeline for real-time financial data. The primary components include Finnhub API for data extraction, Kafka for data streaming, Spark for data processing, Hadoop HDFS for distributed storage, and Power BI for real-time visualization.

## Architecture

The architecture of the system involves the following components:

- **Data Extraction:** Finnhub API
- **Data Streaming:** Apache Kafka
- **Data Processing:** Apache Spark
- **Distributed Data Warehouse:** Hadoop HDFS
- **Time Series Modeling:** Machine learning models for predicting closing prices
- **Real-Time Visualization:** Power BI

## Setup and Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/youssefdahmou/Kafka_Spark_Hadoop_Stream_data-analysis.git
    cd real-time-data-warehouse
    ```

2. **Install Dependencies:**
   - [Apache Kafka](https://kafka.apache.org/)
   - [Apache Spark](https://spark.apache.org/)
   - [Hadoop HDFS](https://hadoop.apache.org/)
   - [Power BI](https://powerbi.microsoft.com/)


3. **Run the Pipeline:**
   - Execute scripts for data extraction, Kafka streaming, Spark processing, and Hadoop HDFS storage.

## Usage

The usage of this project involves executing the data processing pipeline and monitoring the real-time visualizations through Power BI.

## Data Flow

1. **Data Extraction:** Use Finnhub API to fetch real-time financial data.
2. **Data Streaming:** Stream data through Kafka for real-time processing.
3. **Data Processing:** Utilize Apache Spark for processing and feature engineering.
4. **Distributed Data Warehouse:** Store processed data in Hadoop HDFS for distributed storage.

## Time Series Model

Train machine learning models on historical data to predict closing prices in real-time.

## Real-Time Visualization

Utilize Power BI to visualize real-time data insights and trends.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
