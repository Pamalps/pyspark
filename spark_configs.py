import sys
import time
import argparse

from pyspark import SparkConf
from pyspark.sql import SparkSession

from pyspark.sql import functions as F
from pyspark.sql import types as T

def main(spark):
    print(sys.version)

    df.createOrReplaceTempView('df_temp')


if __name__ == "__main__":
    conf= SparkConf()
    conf.set("spark.executor.instances","10")
    conf.set("spark.executor.memory","50g")
    conf.set("spark.driver.memory","40g")
    conf.set("spark.sql.shuffle.partitions","100")
    conf.set("spark.default.parallelism","100")
    conf.set("spark.debug.maxtostringfields","1000")
    #conf.set("spark.sql.autoBroadcastJoinThreshold","-1")
    #conf.set("spark.driver.extraJavaOptions","-XX:+UseG1GC")
    #conf.set("spark.executor.extraJavaOptions","-XX:+UseG1GC")
    conf.set('spark.shuffle.service.enabled','true')
    conf.set('spark.dynamicAllocation.enabled','true')
    conf.set('spark.dynamicAllocation.minExecutors',1)
    conf.set('spark.dynamicAllocation.maxExecutors',100)
    conf.set('spark.dynamicAllocation.initialExecutors',20)
    conf.set('spark.driver.maxResultSize',"64g")

    #Spark session
    spark = SparkSession \
        .builder \
        .master("yarn") \
        .enableHiveSupport() \
        .appName("pamal") \
        .config(conf=conf) \
        .getOrCreate()
    
    spark.sparkContext.setLogLevel("ERROR")

    #Run and time the spark job
    time0= time.time()
    main(spark)
    time1-time.time()

    #End
    print(f"Total runtime: {str(int(time1-time0))}s")
    spark.stop()