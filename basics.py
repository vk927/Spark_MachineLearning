from pyspark.mllib.linalg import Vectors,Matrices
from pyspark.feature import LabeledPoint

vector=[1.0,2.0,3.0,4.0,5.0,6.0]

spark_vector=Vectors.dense(vector)

label=45.0
labeled_point=LabeledPoint(label,vector)
spark_matrix=Matrices.dense(3,2,vector)