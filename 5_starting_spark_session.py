#using setAppName(), we can specify the name of the project , using setMaster, set the number of workers
#conf for configurations
conf = SparkConf().setAppName('Pamal test App')
#feed the configurations into a spark context
sc= SparkContext(conf=conf)
#start a sql context on top of spark context
sql_context = SQLContext(sc)