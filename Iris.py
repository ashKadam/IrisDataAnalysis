
# coding: utf-8

# In[4]:

import pandas as pd


# In[5]:

pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")


# In[6]:

header_names = ['sepal_length','sepal_width','petal_length','petal_width','spacies']
iris_data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", names=header_names)


# In[7]:

iris_data.head()


# In[8]:

iris_data.shape


# In[9]:

iris_data.shape


# In[10]:

iris_data[iris_data.spacies == 'Iris-setosa']


# In[11]:

iris_setosa = iris_data[iris_data.spacies == 'Iris-setosa']


# In[12]:

type(iris_setosa)


# In[13]:

iris_setosa.drop('spacies',axis=1)


# In[14]:

iris_setosa.head()


# In[15]:

iris_data['spacies'].unique()


# In[16]:

iris_data.head()


# In[17]:

iris_data.describe()


# In[20]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as mplot
import seaborn as sb


# In[25]:

sb.pairplot(iris_data, hue='spacies')


# In[26]:

iris_data_setosa_2 = iris_data[(iris_data['spacies'] == 'iris_setosa')
                             & (iris_data['sepal_length'] >= 2.0)]


# In[27]:

iris_data_setosa_2.hist()


# In[28]:

iris_data_setosa_2


# In[30]:

iris_data.describe()


# In[35]:

iris_data['spacies'].unique()


# In[36]:

iris_data_setosa_2 = iris_data[iris_data['spacies'] == 'Iris-setosa']
iris_data_setosa_2.head()
iris_data_setosa_2.describe()


# In[41]:

iris_data_setosa = iris_data[(iris_data['spacies'] == 'Iris-setosa')]
iris_data_setosa.head()


# In[42]:

iris_data_setosa_2 = iris_data_setosa [(iris_data_setosa['sepal_length'] >= 5)]
iris_data_setosa_2.head()


# In[44]:

iris_data_setosa_2['sepal_width'].hist()


# In[49]:

iris_data.plot(kind='scatter',x='sepal_length', y='sepal_width')


# In[50]:

iris_data_versi = iris_data[(iris_data['spacies'] == 'Iris-versicolor')]
iris_data_versi.head()


# In[54]:

iris_data_virgi = iris_data[(iris_data['spacies'] == 'Iris-virginica')]
iris_data_virgi.head()


# In[55]:

iris_data_versi.plot(kind='scatter',x='sepal_length',y='sepal_width')


# In[56]:

iris_data_virgi.plot(kind='scatter',x='sepal_length',y='sepal_width')


# In[63]:

fig, axs = mplot.subplots(1, 3, sharey=True)
iris_data_setosa.plot(kind='scatter', x='sepal_length', y='sepal_width', ax=axs[0], figsize=(16, 8))
iris_data_setosa.plot(kind='scatter', x='sepal_length', y='petal_length', ax=axs[1])
iris_data_setosa.plot(kind='scatter', x='sepal_length', y='petal_width', ax=axs[2])


# In[64]:

fig, axs = mplot.subplots(1, 3, sharey=True)
iris_data_setosa.plot(kind='scatter', x='sepal_length', y='sepal_width', ax=axs[0], figsize=(16, 8))
iris_data_versi.plot(kind='scatter', x='sepal_length', y='sepal_width', ax=axs[1])
iris_data_virgi.plot(kind='scatter', x='sepal_length', y='sepal_width', ax=axs[2])


# In[65]:

fig, axs = mplot.subplots(1, 3, sharey=True)
iris_data_setosa.plot(kind='scatter', x='petal_length', y='petal_width', ax=axs[0], figsize=(16, 8))
iris_data_versi.plot(kind='scatter', x='petal_length', y='petal_width', ax=axs[1])
iris_data_virgi.plot(kind='scatter', x='petal_length', y='petal_width', ax=axs[2])


# In[72]:

iris_data_setosa.describe()


# In[110]:

from sklearn import linear_model, datasets


# In[78]:

features = ['petal_length','petal_width']
X = iris_data[features] 
Y = iris_data['spacies']
h=0.2


# In[81]:

logreg = linear_model.LogisticRegression()


# In[82]:

logreg.fit(X,Y)


# In[83]:

import numpy as np


# In[96]:

x_min, x_max = X.values[:, 0].min() - .5, X.values[:, 0].max() + .5
y_min, y_max = X.values[:, 1].min() - .5, X.values[:, 1].max() + .5


# In[98]:

x_max


# In[99]:

xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = logreg.predict(np.c_[xx.ravel(), yy.ravel()])


# In[100]:

Z


# In[105]:

Z = Z.reshape(xx.shape)


# In[108]:

mplot.figure(1, figsize=(4, 3))


# In[117]:

yy


# In[111]:

iris = datasets.load_iris()


# In[ ]:

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5


# In[ ]:

xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = logreg.predict(np.c_[xx.ravel(), yy.ravel()])


# In[122]:

s = pd.Series(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
f = pd.Categorical.from_codes(iris.target,s)
f


# In[ ]:



