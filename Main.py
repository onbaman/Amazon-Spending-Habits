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