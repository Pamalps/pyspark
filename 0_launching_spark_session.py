from operator import truediv


export PYSPARK_PYTHON=python3
pyspark --driver-memory 40g
--executor memory 40g
--conf spark.sql.shuffle.partitions=100
--conf spark.default.parallelism=100
--conf spark.debug.maxtostringfields=1000
--conf spark.executor.instances=10
--conf spark.shuffle.service.enabled=true
--conf spark.dynamicAllocation.enabled=true
--conf spark.dynamicAllocation.minExecutors=1
--conf spark.dynamicAllocation.maxExecutors=100
--conf spark.dynamicAllocation.initialExecutors=20