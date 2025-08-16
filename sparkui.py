from pyspark.sql import SparkSession

# Щоб дізнатись адресу Spark UI, запустіть цей код у терміналі:
# spark-shell
# в даному випадку це буде http://192.168.0.226:4040

# Створюємо сесію Spark
spark = SparkSession.builder \
    .master("local[*]") \
    .config("spark.sql.shuffle.partitions", "2") \
    .appName("MyGoitSparkSandbox") \
    .getOrCreate()
input("Press Enter to continue...1")

# Завантажуємо датасет
nuek_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv('data/nuek-vuh3.csv')
input("Press Enter to continue...2")

nuek_repart = nuek_df.repartition(2)
input("Press Enter to continue...3")


nuek_processed = nuek_repart \
                    .where("final_priority < 3") \
                    .select("unit_id", "final_priority") \
                    .groupBy("unit_id") \
                    .count()
input("Press Enter to continue...4")

nuek_processed.collect()
input("Press Enter to continue...5")

# Закриваємо сесію Spark
spark.stop()