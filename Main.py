import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 23)


# Injest csv file and clean data and convert data types
def ingestCSV(pathTocsv):
    uncleanedDF = pd.read_csv(pathTocsv)
    df_cleaned = uncleanedDF.drop(
        ["Purchase Order Number", "Website", "Ordering Customer Email", "Shipment Date", "Shipping Address Name",
         "Shipping Address Street 1", "Shipping Address Street 2", "Shipping Address City", "Shipping Address State",
         "Shipping Address Zip", "Order Status", "Group Name", "Buyer Name", "Carrier Name & Tracking Number"], axis=1)

    df_cleaned = df_cleaned.apply(lambda x: x.str.strip('$'))
    df_cleaned['Subtotal'] = df_cleaned['Subtotal'].astype('float64')
    df_cleaned['Shipping Charge'] = df_cleaned['Shipping Charge'].astype('float64')
    df_cleaned['Tax Before Promotions'] = df_cleaned['Tax Before Promotions'].astype('float64')
    df_cleaned['Total Promotions'] = df_cleaned['Total Promotions'].astype('float64')
    df_cleaned['Tax Charged'] = df_cleaned['Tax Charged'].astype('float64')
    df_cleaned['Total Charged'] = df_cleaned['Total Charged'].astype('float64')

    # print(df_cleaned)
    return df_cleaned


# Split Date to years,month,days
def splitDatetime(cleanedDF):
    cleanedDF['Order Date'] = pd.to_datetime(cleanedDF['Order Date'])
    cleanedDF['Order Year'] = cleanedDF['Order Date'].dt.year
    cleanedDF['Order Month'] = cleanedDF['Order Date'].dt.month
    cleanedDF['Order Day'] = cleanedDF['Order Date'].dt.day
    cleanedDF = cleanedDF.drop('Order Date', axis=1)
    newOrder = ['Order Year', 'Order Month', 'Order Day', 'Order ID',
                'Payment Instrument Type', 'Subtotal', 'Shipping Charge',
                'Tax Before Promotions', 'Total Promotions', 'Tax Charged', 'Total Charged']

    cleanedDF = cleanedDF[newOrder]
    return cleanedDF

# Get list of all the unique years in the column
def yearsArray(cleanedDF):
    yearsList = cleanedDF['Order Year'].value_counts().index.tolist()
    print(yearsList)
    return yearsList


# Yearly Spending
def yearlySpending(cleandDF):
    df_yearlySpending = cleandDF.groupby('Order Year').sum()
    df_yearlySpending = df_yearlySpending.drop(['Order Month', 'Order Day', 'Subtotal', 'Shipping Charge', 'Tax Before Promotions',
                            'Total Promotions', 'Tax Charged'], axis=1)
    ax = df_yearlySpending.plot(kind='bar')
    ax.set_title("Yearly Spending Habits")
    #return ax


# Monthly Spending
def monthlySpending(cleanedDF):
    years = yearsArray(cleanedDF)
    for i in range(len(years)):
        df_monthly = cleanedDF.loc[cleanedDF['Order Year'] == years[i]]

        df_monthlySpending = df_monthly.groupby('Order Month').sum()
        df_monthlySpending = df_monthlySpending.drop(
            ['Order Year', 'Order Day', 'Subtotal', 'Shipping Charge', 'Tax Before Promotions',
             'Total Promotions', 'Tax Charged'], axis=1)

        ax = df_monthlySpending.plot(kind='bar')
        ax.set_title(str(years[i]) + ' Monthly Spending')
        # ax = ax.plot(kind='bar', figsize=(10,4))
        # plt.show()


# daily Spending
def dailySpending(cleanedDF):
    years = yearsArray(cleanedDF)
    monthsList = []
    for i in range(len(years)):
        df_monthly = cleanedDF.loc[cleanedDF['Order Year'] == years[i]]
        monthsList = df_monthly['Order Month'].value_counts().index

        for j in range(len(monthsList)):
            df_daily = df_monthly.loc[df_monthly['Order Month'] == monthsList[j]].groupby("Order Day").sum()
            df_daily = df_daily.drop(
                ['Order Year', 'Order Month', 'Subtotal', 'Shipping Charge', 'Tax Before Promotions',
                 'Total Promotions', 'Tax Charged'], axis=1)

            # ax = df_daily.plot(kind='bar')
            # ax.set_title('Year' + str(yearsList[i]) + ' Month: ' + str(monthsList[j]) + ' Daily Spending')
            # ax = ax.plot(kind='bar', figsize=(20, 10))
            # plt.show()


df_Spending = ingestCSV("data/01-Jan-2017_to_01-Jan-2019.csv")
df_Spending = splitDatetime(df_Spending)
yearlySpending(df_Spending)
plt.show()
