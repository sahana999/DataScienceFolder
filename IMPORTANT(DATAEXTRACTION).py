'''import pandas as pd
df=pd.read_csv('salaries.csv')

dt=df[(df['salary']>90000)&(df['discipline']=='B')]
print(dt)
..................'''

'''import pandas as pd
df=pd.read_csv('salaries.csv')
         #Handling missing values and filling by the sum of total(see in the output filled by 105.0)
df['service'].fillna(df['service'].sum(),inplace=True)

print(df)
.......................'''

'''import pandas as pd
df=pd.read_csv('salaries.csv')
                   #REMOVE ALL NULL VALUES(null value rows were removed)
dt=df.dropna()
print(dt)
..................'''

'''import pandas as pd
df=pd.read_csv('salaries.csv')
  #Insert a new column
df.insert(6,'test',df['service']+20)
print(df)
.............'''

'''import pandas as pd
df=pd.read_csv('salaries.csv')
df1=pd.read_csv('salaries1.csv')

#Appending csv file
df2=df.append(df1)
print(df2)
..............'''

'''import pandas as pd
df=pd.read_csv('salaries.csv')
#print dataset in ascending order based on salary
print(df.sort_values('salary'))
....................'''

'''import pandas as pd
df=pd.read_csv('salaries.csv')
#print dataset in descending order based on salary
print(df.sort_values('salary',ascending=False))
..............'''


'''import pandas as pd
df=pd.read_csv('salaries.csv')
dc=df.groupby(['rank'])
print(dc['salary'].sum())
.............'''



'''import pandas as pd
df=pd.read_csv('Emp.csv')
df1=pd.read_csv('EmpGrade.csv')
print(df)
print(df1)
#Merge two files based on empno
print(pd.merge(df,df1,on='EmpNo'))
......................'''

'''import pandas as pd
df=pd.read_csv('StudentDataForPivot.csv')
print(df)

print(pd.pivot_table(df,index=['Name','Subject'],values='Score',aggfunc='sum'))

'''

'''import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('EmpData.csv')
plt.plot(df['EmpCode'],
         df['Payment'],
         color='red',
         linestyle='--',
         linewidth=5)
plt.show()'''

'''............
import pandas as pd
#import matplotlib.pyplot as plt
df=pd.read_csv('EmpData.csv')
dfg=df.groupby("City")
total=dfg['Payment'].sum()

total.plot(kinda='bar')
...............'''

'''
..........
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('EmpData.csv')
plt.hist(df['Payment'],bins=5)
plt.show()
...............'''

'''import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('EmpData.csv')
c=df.groupby(df['City'])
cp=['red','green','blue']

c.sum().plot(kind='pie',y='Payment')
.............................................'''

'''import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('EmpData.csv')
plt.scatter(df['Payment'],
            df['NoOfHours'],marker='o')
plt.show()'''

