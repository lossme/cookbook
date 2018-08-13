import os
import shutil
from pyspark import SparkContext, SparkConf


conf = SparkConf().setMaster('local[*]').setAppName('TestApp')
sc = SparkContext(conf=conf)

lines_rdd = sc.textFile("/opt/spark/README.md")

word_count_rdd = lines_rdd.flatMap(lambda line: line.split(' '))\
    .map(lambda word: (word, 1))\
    .reduceByKey(lambda a, b: a + b)\
    .sortBy(lambda item: item[1], ascending=False)


word_count_rdd.persist()

if os.path.exists('word_count_result'):
    shutil.rmtree('word_count_result')

word_count_rdd.map(lambda item: '{}\t{}'.format(item[0], item[1])).coalesce(1).saveAsTextFile("word_count_result")
