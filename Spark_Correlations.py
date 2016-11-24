from pyspark.mllib.linalg import Vectors
from pyspark.mllib.stat import statistics

v1=sc.parallelize([1.0,2.0,3.0])
v2=sc.parallelize([9.0,4.0,1.0])

print Statistics.corr(v1,v2)

