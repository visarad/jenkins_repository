import tensorflow
import tensorflow_probability as tfp
import matplotlib.pyplot as plt

tfd = tfp.distributions

normal = tfd.Normal(loc=0.,scale=1.)
data = normal.sample((2,3))


plt.hist(normal.sample(10000),bins=5, density=True) 
plt.show()                              
                 
