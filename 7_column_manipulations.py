#drop a column
df=df.drop('col1','col2')

#select columns
df=df.select('col1','col2')

#view distinct values in a col
df.select('col1').distinct().show()

df1=df.select(f.col('col1')).distinct()