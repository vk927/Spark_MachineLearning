from pyspark.mllib.linalg import Vectors
from pyspark.mllib.feature import StandardScalar

vec1=Vectors.dense([10,35,50])
# create standardscalar
ss=StandardScalar(withMean=True,withStd=True)
# fit the model with data
ss_model=ss.fit(vec1)
# transform rdd with the model
scaled_rdd=ss_model.transform(vec1)