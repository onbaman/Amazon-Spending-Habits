import pandas as pd
import numpy as np

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 23)

#Injest csv file and clean data
uncleanedDF = pd.read_csv("data/01-Jan-2017_to_01-Jan-2019.csv")
df_cleaned = uncleanedDF.drop(["Purchase Order Number", "Website", "Ordering Customer Email", "Shipment Date", "Shipping Address Name",
                              "Shipping Address Street 1", "Shipping Address Street 2", "Shipping Address City" ,"Shipping Address State",
                              "Shipping Address Zip", "Order Status", "Group Name", "Buyer Name", "Carrier Name & Tracking Number"], axis=1)

#print(df_cleaned)
df_cleaned = df_cleaned.apply(lambda x: x.str.strip('$'))
df_cleaned['Subtotal'] = df_cleaned['Subtotal'].astype('float64')
df_cleaned['Shipping Charge'] = df_cleaned['Shipping Charge'].astype('float64')
df_cleaned['Tax Before Promotions'] = df_cleaned['Tax Before Promotions'].astype('float64')
df_cleaned['Total Promotions'] = df_cleaned['Total Promotions'].astype('float64')
df_cleaned['Tax Charged'] = df_cleaned['Tax Charged'].astype('float64')
df_cleaned['Total Charged'] = df_cleaned['Total Charged'].astype('float64')

#Split Date input multiple columns

df_cleaned['Order Date'] = pd.to_datetime(df_cleaned['Order Date'])
df_cleaned['Order Year'] = df_cleaned['Order Date'].dt.year
df_cleaned['Order Month'] = df_cleaned['Order Date'].dt.month
df_cleaned['Order Day'] = df_cleaned['Order Date'].dt.day
df_cleaned = df_cleaned.drop('Order Date',axis=1)
newOrder = ['Order Year', 'Order Month','Order Day' ,'Order ID',
        'Payment Instrument Type', 'Subtotal','Shipping Charge',
        'Tax Before Promotions', 'Total Promotions','Tax Charged', 'Total Charged']

df_cleaned = df_cleaned[newOrder]

#print(df_cleaned)

#Get list of all the unique years in the column
yearsList = df_cleaned['Order Year'].value_counts().index.tolist()
print(yearsList)
#Yearly Spending
df_yearlySpending = df_cleaned.groupby('Order Year').sum()
df_yearlySpending.drop(['Order Month', 'Order Day', 'Subtotal', 'Shipping Charge', 'Tax Before Promotions',
                        'Total Promotions', 'Tax Charged'], axis=1)