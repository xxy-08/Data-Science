import numpy as np
import pandas as pd
# Part 1 - Numpy
# Use this dataset for the first 4 questions.
# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
# 1.⁠ ⁠Define two custom numpy arrays, say A and B. Generate two new numpy arrays by stacking A and B vertically and horizontally.
A=np.array([1,2,3])
B=np.array([5,6,7])
vAB=np.vstack((A,B))
hAB=np.hstack((A,B))
print(vAB)
print(hAB)
# 2.⁠ ⁠Find common elements between A and B. [Hint : Intersection of two sets]
A=np.array([1,2,3,4])
B=np.array([5,6,7,4])
com=np.intersect1d(A,B)
print(com)
# 3.⁠ ⁠Extract all numbers from A which are within a specific range. eg between 5 and 10. 
# [Hint: np.where() might be useful or boolean masks]
A=np.array([1,2,3,4,5,6,7,111,23,432])
re=np.where((A<10)&(A>5),A,0)
print(re)
# 4.⁠ ⁠Filter the rows of iris_2d that has petallength (3rd column) > 1.5 and sepallength (1st column) < 5.0
indice = np.where([(iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)])
result=iris_2d[indice[0]]
print(result)
# Part 2 - Pandas
# 1.⁠ ⁠From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).
print("pandas")
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
df_filter=df[['Manufacturer', 'Model' ,'Type']].iloc[::20]
print(df_filter)
# 2.⁠ ⁠Replace missing values in Min.Price and Max.Price columns with their respective mean.
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
df['Min.Price']=df.fillna(df['Min.Price'].mean(),inplace=True)
df['Max.Price']=df.fillna(df['Max.Price'].mean(),inplace=True)
print(df)
# 3.⁠ ⁠How to get the rows of a dataframe with row sum > 100?
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
sum1=df[df.sum(axis=1)>100]
print(sum1)
