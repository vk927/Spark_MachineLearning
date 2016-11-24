from pyspark.mllib.linalg import Vectors
from pyspark.mllib.feature import ElementwiseProduct

vec1=Vectors.dense([10,35,50])
vec2=Vectors.dense([1,2,3])
ep=ElementwiseProduct(vec2)
new_vec=ep.transform(vec_rdd)

new_vec.first()
