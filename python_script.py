import pandas as pd 

df=pd.read_csv("/opt/airflow/dags/sales_data.csv")

df=df.drop_duplicates()

df=df.fillna(0)

df["Amount"]=df["Amount"].astype(int)

df["Date"]=pd.to_datetime(df["Date"],format='%d-%m-%Y')
df["Date"]=df["Date"].dt.strftime('%Y-%m-%d')

print("Row count:",len(df))
print(df.head())

df.to_csv("/opt/airflow/dags/cleaned_sales.csv",index=False)