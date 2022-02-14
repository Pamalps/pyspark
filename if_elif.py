import os
import sys
import time
import argparse

from pyspark import SparkConf
from pyspark.sql import SparkSession

from pyspark.sql import functions as F
from pyspark.sql import types as T


parser = argparse.ArgumentParser(description='Pamal')
parser.add_argument('--name',type=str,default='Pamal')
parser.add_argument('--age',type=int,default=30)
args=parser.parse_args()

def main(spark):
    print(sys.version)

    print("--------Pamal's test--------")

    print(args.name)
    print(args.age)

    if args.name == 'Pamal':
        df1=['hello','pamal']
        df2='bye','pamal'
    elif args.name == 'sino':
        df1=['hello','sino']
        df2='bye','sino'
    elif args.name == 'Moe'
        df1=['Ok']
        df2='bye'
    else:
        sys.exit('i no like the name')

