#load csv file using sql_context to a spark dataframe
import xxlimited


df=sql_context.read.csv('/file.csv',
                    header=True,
                    inferSchema=True)


#view the schema of the input dataset - to see which columns are integers and strings
df.printSchema()

#convert spark dataframe to pandas dataframe - to get a pandas view which is cleaner
df.limit(5).toPandas()

#reading a table
df=spark.sql("select * from ...")

#preview a dataframe
df.show()

#disabling log messages
sc.setLogLevel("OFF")


# to see column types and last update for the table
df1=spark.sql("describe formatted ...")


#using f strings to load data
db_name=xx
table_name=yy
df=spark.sql(f"select * from {db_name}.{table_name}")