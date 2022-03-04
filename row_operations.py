#fill nulls with zeroes
df1=df1.fillna(0)

#show command
spark.sql("describe formatted xx.yy").show(1000,False,True)
df.show(1000,truncate=True,vertical=False)