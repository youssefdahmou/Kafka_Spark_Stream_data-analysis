from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, ArrayType, LongType

# Define the schema for the incoming JSON messages
schema = StructType([
    StructField("data", ArrayType(StructType([
        StructField("c", ArrayType(StringType()), True),
        StructField("p", DoubleType(), True),
        StructField("s", StringType(), True),
        StructField("t", LongType(), True),
        StructField("v", DoubleType(), True),
    ])), True),
    StructField("type", StringType(), True),
])

# Create a Spark session
spark = SparkSession.builder \
    .appName("FinnhubStreaming") \
    .getOrCreate()

# Read data from Kafka topic 'finnhub' as a streaming DataFrame
raw_streaming_data = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "finnhub") \
    .option("kafka.group.id", "group1") \
    .load()

# Convert the value column from Kafka into a string and parse the JSON
streaming_data = raw_streaming_data \
    .selectExpr("CAST(value AS STRING)") \
    .select(from_json("value", schema).alias("message")) \
    .select("message.data", "message.type")

# Explode the 'data' array to get individual trade records
exploded_data = streaming_data.select("type", col("data").alias("trade_data")).explode("trade_data")

# Select relevant fields
final_data = exploded_data.select(
    "type",
    col("trade_data.c").alias("c"),
    col("trade_data.p").alias("price"),
    col("trade_data.s").alias("symbol"),
    col("trade_data.t").alias("timestamp"),
    col("trade_data.v").alias("volume")
)

# Perform further processing or write the streaming data to another sink
# For example, you can write it to the console for testing purposes
query = final_data \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

# Wait for the termination of the streaming query
query.awaitTermination()
