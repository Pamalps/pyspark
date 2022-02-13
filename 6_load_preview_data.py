#load csv file using sql_context to a spark dataframe
df=sql_context.read.csv('/file.csv',
                    header=True,
                    inferSchema=True)


#view the schema of the input dataset - to see which columns are integers and strings
df.printSchema()

#convert spark dataframe to pandas dataframe - to get a pandas view which is cleaner
df.limit(5).toPandas()

