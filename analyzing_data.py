import pandas as pd
input ("Load Files Into a DataFrame...")
df = pd.read_excel('data/my_data.xlsx')
print(df) 
input ("Press Enter to describe the Dataframe...")
print (df.describe())
input ("Press Enter Sort the Dataframe...")
print (df.sort_values("SNAMES "))
input ("Press Enter To Filter the Dataframe...")
print (df.filter(["SNAMES ","QUIZZES "]))
input ("Press Enter to Filter Columns Contain aA..")
print (df.filter(regex ='[aA]'))
input ("Press Enter to Group Student by Semester..")
print (df.groupby(['Semester']).mean())

