import pandas as pd
from pathlib import Path
from sklearn.linear_model import LinearRegression
import hvplot.pandas 

sales_csv_path = Path('../Data/sales_data.csv')
menu_csv_path = Path('../Data/menu_data.csv')

def cleanup_df_sum(df):
    df1 = df[['Quantity', 'Revenue', 'Date']]
    df1.set_index('Date', inplace = True)
    df1 = df1.groupby(by = [df1.index.year, df1.index.month]).sum()
    df1['Quantity_Over_Time'] = 0
    df1['Revenue_Over_Time'] = 0
    df1.reset_index(level=[0,0], inplace = True)
    for index, row in df1.iterrows():
        if index == 0:
            df1.iloc[index, 3] = df1.iloc[index, 1]
            df1.iloc[index, 4] = df1.iloc[index, 2]
        else:
            df1.iloc[index, 3] = (df1.iloc[index, 1] + df1.iloc[index-1, 3])
            df1.iloc[index, 4] = (df1.iloc[index, 2] + df1.iloc[index-1, 4])
    df1.drop(columns = ['Date'], inplace = True)
    return df1


def cleanup_df_count(df):
    df = df.drop(columns = ['Quantity_Over_Time', 'Revenue_Over_Time', 'Line_Item_ID', 'Cost', 'Price', 'Item_Ordered'])
    df.set_index('Date', inplace = True)
    df = df.groupby(by = [df.index.year, df.index.month]).count()
    return df

sales_df = pd.read_csv(sales_csv_path)
menu_df = pd.read_csv(menu_csv_path)

sales_df['Date'] = pd.to_datetime(sales_df['Date'])

sales_df['Customer_Id'] = 0

count = 1
list_of_customer_numbers = {}

for credit_card_number in sales_df['Credit_Card_Number']:
    if credit_card_number in list_of_customer_numbers:
        pass
    else:
        list_of_customer_numbers[credit_card_number] = count
        count+=1
        
for index, row in sales_df.iterrows():
    if row[2] in list_of_customer_numbers.keys():
        sales_df.iloc[index,5] = list_of_customer_numbers[row[2]]
        

menu_df.set_index('item', inplace = True)
sales_df.set_index('Menu_Item', inplace = True)

combined_df = sales_df.join(menu_df)
combined_df.reset_index(inplace = True)
combined_df.rename(columns = {'index': "Item_Ordered", 'price': 'Price', 'cost': 'Cost'}, inplace = True)
combined_df.drop(columns = ['Credit_Card_Number', 'description', 'category'], inplace = True)
combined_df['Revenue'] = (combined_df['Quantity']*combined_df['Price'])-combined_df['Cost']

combined_df = sales_df.join(menu_df)
combined_df.reset_index(inplace = True)
combined_df.rename(columns = {'index': "Item_Ordered", 'price': 'Price', 'cost': 'Cost'}, inplace = True)
combined_df.drop(columns = ['Credit_Card_Number', 'description', 'category'], inplace = True)
combined_df['Revenue'] = (combined_df['Quantity']*combined_df['Price'])-combined_df['Cost']

list_of_menu_items = []
for item in combined_df['Item_Ordered']:
    if item in list_of_menu_items:
        pass
    else:
        list_of_menu_items.append(item)
           
burnt_garlic_tonkotsu_ramen_df = combined_df[combined_df.Item_Ordered == 'burnt garlic tonkotsu ramen'].copy()
miso_crab_ramen_df = combined_df[combined_df.Item_Ordered == 'miso crab ramen'].copy()
nagomi_shoyu_df = combined_df[combined_df.Item_Ordered == 'nagomi shoyu'].copy()
shio_ramen_df = combined_df[combined_df.Item_Ordered == 'shio ramen'].copy()
soft_shell_miso_crab_ramen_df = combined_df[combined_df.Item_Ordered == 'soft-shell miso crab ramen'].copy()
spicy_miso_ramen_df = combined_df[combined_df.Item_Ordered == 'spicy miso ramen'].copy()
tonkotsu_ramen_df = combined_df[combined_df.Item_Ordered == 'tonkotsu ramen'].copy()
tori_paitan_ramen_df = combined_df[combined_df.Item_Ordered == 'tori paitan ramen'].copy()
truffle_butter_ramen_df = combined_df[combined_df.Item_Ordered == 'truffle butter ramen'].copy()
vegetarian_curry_king_trumpet_mushroom_ramen_df = combined_df[combined_df.Item_Ordered == 'vegetarian curry + king trumpet mushroom ramen'].copy()
vegetarian_spicy_miso_df = combined_df[combined_df.Item_Ordered == 'vegetarian spicy miso'].copy()


burnt_garlic_tonkotsu_ramen_df_sum = cleanup_df_sum(burnt_garlic_tonkotsu_ramen_df)
burnt_garlic_tonkotsu_ramen_df_sum.rename(columns = {
    'Quantity': 'Burnt_Garlic_Tonkotsu_Ramen_Quantity', 
    'Revenue': 'Burnt_Garlic_Tonkotsu_Ramen_Revenue', 
    'Quantity_Over_Time': 'Burnt_Garlic_Tonkotsu_Ramen_Quantity_Over_Time', 
    'Revenue_Over_Time': 'Burnt_Garlic_Tonkotsu_Ramen_Revenue_Over_Time'
}, inplace = True)

miso_crab_ramen_df_sum = cleanup_df_sum(miso_crab_ramen_df)
miso_crab_ramen_df_sum.rename(columns = {
    'Quantity': 'Miso_Crab_Ramen_Quantity', 
    'Revenue': 'Miso_Crab_Ramen_Revenue', 
    'Quantity_Over_Time': 'Miso_Crab_Ramen_Quantity_Over_Time', 
    'Revenue_Over_Time': 'Miso_Crab_Ramen_Revenue_Over_Time'
}, inplace = True)

nagomi_shoyu_df_sum = cleanup_df_sum(nagomi_shoyu_df)
nagomi_shoyu_df_sum.rename(columns = {
    'Quantity': 'Nagomi_Shoyu_Quantity', 
    'Revenue': 'Nagomi_Shoyu_Revenue', 
    'Quantity_Over_Time': 'Nagomi_Shoyu_Quantity_Over_Time', 
    'Revenue_Over_Time': 'Nagomi_Shoyu_Revenue_Over_Time'
}, inplace = True)

shio_ramen_df_sum = cleanup_df_sum(shio_ramen_df)
shio_ramen_df_sum.rename(columns = {
    'Quantity': 'Shio_Ramen_Quantity', 
    'Revenue': 'Shio_Ramen_Revenue', 
    'Quantity_Over_Time': 'Shio_Ramen_Quantity_Over_Time', 
    'Revenue_Over_Time': 'Shio_Ramen_Revenue_Over_Time'
}, inplace = True)

soft_shell_miso_crab_ramen_df_sum = cleanup_df_sum(soft_shell_miso_crab_ramen_df)
soft_shell_miso_crab_ramen_df_sum.rename(columns = {
    'Quantity': 'Soft_Shell_Miso_Crab_Ramen_Quantity', 
    'Revenue': 'Soft_Shell_Miso_Crab_Ramen_Revenue', 
    'Quantity_Over_Time': 'Soft_Shell_Miso_Crab_Ramen_Quantity_Over_Time', 
    'Revenue_Over_Time': 'Soft_Shell_Miso_Crab_Ramen_Revenue_Over_Time'
}, inplace = True)

spicy_miso_ramen_df_sum = cleanup_df_sum(spicy_miso_ramen_df)
spicy_miso_ramen_df_sum.rename(columns = {
    'Quantity': 'Spicy_Miso_Ramen_Quantity', 
    'Revenue': 'Spicy_Miso_Ramen_Revenue', 
    'Quantity_Over_Time': 'Spicy_Miso_Ramen_Quantity_Over_Time', 
    'Revenue_Over_Time': 'Spicy_Miso_Ramen_Revenue_Over_Time'
}, inplace = True)

tonkotsu_ramen_df_sum = cleanup_df_sum(tonkotsu_ramen_df)
tonkotsu_ramen_df_sum.rename(columns = {
    'Quantity': 'Tonkotsu_Ramen_Quantity', 
    'Revenue': 'Tonkotsu_Ramen_Revenue', 
    'Quantity_Over_Time': 'Tonkotsu_Ramen_Quantity_Over_Time', 
    'Revenue_Over_Time': 'Tonkotsu_Ramen_Revenue_Over_Time'
}, inplace = True)

tori_paitan_ramen_df_sum = cleanup_df_sum(tori_paitan_ramen_df)
tori_paitan_ramen_df_sum.rename(columns = {
    'Quantity': 'Tori_Paitan_Ramen_Quantity', 
    'Revenue': 'Tori_Paitan_Ramen_Revenue', 
    'Quantity_Over_Time': 'Tori_Paitan_Ramen_Quantity_Over_Time', 
    'Revenue_Over_Time': 'Tori_Paitan_Ramen_Revenue_Over_Time'
}, inplace = True)

truffle_butter_ramen_df_sum = cleanup_df_sum(truffle_butter_ramen_df)
truffle_butter_ramen_df_sum.rename(columns = {
    'Quantity': 'Truffle_Butter_Ramen_Quantity', 
    'Revenue': 'Truffle_Butter_Ramen_Revenue', 
    'Quantity_Over_Time': 'Truffle_Butter_Ramen_Quantity_Over_Time', 
    'Revenue_Over_Time': 'Truffle_Butter_Ramen_Revenue_Over_Time'
}, inplace = True)

vegetarian_curry_king_trumpet_mushroom_ramen_df_sum = cleanup_df_sum(vegetarian_curry_king_trumpet_mushroom_ramen_df)
vegetarian_curry_king_trumpet_mushroom_ramen_df_sum.rename(columns = {
    'Quantity': 'Vegetarian_Curry_King_Trumpet_Mushroom_Ramen_Quantity', 
    'Revenue': 'Vegetarian_Curry_King_Trumpet_Mushroom_Ramen_Revenue', 
    'Quantity_Over_Time': 'Vegetarian_Curry_King_Trumpet_Mushroom_Ramen_Quantity_Over_Time', 
    'Revenue_Over_Time': 'Vegetarian_Curry_King_Trumpet_Mushroom_Ramen_Revenue_Over_Time'
}, inplace = True)

vegetarian_spicy_miso_df_sum = cleanup_df_sum(vegetarian_spicy_miso_df)
vegetarian_spicy_miso_df_sum.rename(columns = {
    'Quantity': 'Vegetarian_Spicy_Miso_Quantity', 
    'Revenue': 'Vegetarian_Spicy_Miso_Revenue', 
    'Quantity_Over_Time': 'Vegetarian_Spicy_Miso_Quantity_Over_Time', 
    'Revenue_Over_Time': 'Vegetarian_Spicy_Miso_Revenue_Over_Time'
}, inplace = True)


Item_Quantity_Over_Time_DF = pd.concat([
    burnt_garlic_tonkotsu_ramen_df_sum['Burnt_Garlic_Tonkotsu_Ramen_Quantity_Over_Time'],
    miso_crab_ramen_df_sum['Miso_Crab_Ramen_Quantity_Over_Time'],
    nagomi_shoyu_df_sum['Nagomi_Shoyu_Quantity_Over_Time'],
    shio_ramen_df_sum['Shio_Ramen_Quantity_Over_Time'],
    soft_shell_miso_crab_ramen_df_sum['Soft_Shell_Miso_Crab_Ramen_Quantity_Over_Time'],
    spicy_miso_ramen_df_sum['Spicy_Miso_Ramen_Quantity_Over_Time'],
    tonkotsu_ramen_df_sum['Tonkotsu_Ramen_Quantity_Over_Time'],
    tori_paitan_ramen_df_sum['Tori_Paitan_Ramen_Quantity_Over_Time'],
    truffle_butter_ramen_df_sum['Truffle_Butter_Ramen_Quantity_Over_Time'],
    vegetarian_curry_king_trumpet_mushroom_ramen_df_sum['Vegetarian_Curry_King_Trumpet_Mushroom_Ramen_Quantity_Over_Time'],
    vegetarian_spicy_miso_df_sum['Vegetarian_Spicy_Miso_Quantity_Over_Time']
    ], axis=1)

Item_Revenue_Over_Time_DF = pd.concat([
    burnt_garlic_tonkotsu_ramen_df_sum['Burnt_Garlic_Tonkotsu_Ramen_Revenue_Over_Time'],
    miso_crab_ramen_df_sum['Miso_Crab_Ramen_Revenue_Over_Time'],
    nagomi_shoyu_df_sum['Nagomi_Shoyu_Revenue_Over_Time'],
    shio_ramen_df_sum['Shio_Ramen_Revenue_Over_Time'],
    soft_shell_miso_crab_ramen_df_sum['Soft_Shell_Miso_Crab_Ramen_Revenue_Over_Time'],
    spicy_miso_ramen_df_sum['Spicy_Miso_Ramen_Revenue_Over_Time'],
    tonkotsu_ramen_df_sum['Tonkotsu_Ramen_Revenue_Over_Time'],
    tori_paitan_ramen_df_sum['Tori_Paitan_Ramen_Revenue_Over_Time'],
    truffle_butter_ramen_df_sum['Truffle_Butter_Ramen_Revenue_Over_Time'],
    vegetarian_curry_king_trumpet_mushroom_ramen_df_sum['Vegetarian_Curry_King_Trumpet_Mushroom_Ramen_Revenue_Over_Time'],
    vegetarian_spicy_miso_df_sum['Vegetarian_Spicy_Miso_Revenue_Over_Time']
    ], axis=1)



x = df['Index'].values.reshape(-1,1)
model = LinearRegression


y = Item_Revenue_Over_Time_DF['Burnt_Garlic_Tonkotsu_Ramen_Revenue_Over_Time'].values
reg = LinearRegression().fit(x, y)
Burnt_Garlic_Tonkotsu_Ramen_Coef = reg.coef_[0]

y = Item_Revenue_Over_Time_DF['Miso_Crab_Ramen_Revenue_Over_Time'].values
reg = LinearRegression().fit(x, y)
Miso_Crab_Ramen_Coef = reg.coef_[0]

y = Item_Revenue_Over_Time_DF['Nagomi_Shoyu_Revenue_Over_Time'].values
reg = LinearRegression().fit(x, y)
Nagomi_Shoyu_Revenue_Coef = reg.coef_[0]

y = Item_Revenue_Over_Time_DF['Shio_Ramen_Revenue_Over_Time'].values
reg = LinearRegression().fit(x, y)
Shio_Ramen_Coef = reg.coef_[0]

y = Item_Revenue_Over_Time_DF['Soft_Shell_Miso_Crab_Ramen_Revenue_Over_Time'].values
reg = LinearRegression().fit(x, y)
Soft_Shell_Miso_Crab_Ramen_Coef = reg.coef_[0]

y = Item_Revenue_Over_Time_DF['Spicy_Miso_Ramen_Revenue_Over_Time'].values
reg = LinearRegression().fit(x, y)
Spicy_Miso_Ramen_Coef = reg.coef_[0]

y = Item_Revenue_Over_Time_DF['Tonkotsu_Ramen_Revenue_Over_Time'].values
reg = LinearRegression().fit(x, y)
Tonkotsu_Ramen_Coef = reg.coef_[0]

y = Item_Revenue_Over_Time_DF['Tori_Paitan_Ramen_Revenue_Over_Time'].values
reg = LinearRegression().fit(x, y)
Tori_Paitan_Ramen_Coef = reg.coef_[0]

y = Item_Revenue_Over_Time_DF['Truffle_Butter_Ramen_Revenue_Over_Time'].values
reg = LinearRegression().fit(x, y)
Truffle_Butter_Ramen_Coef = reg.coef_[0]

y = Item_Revenue_Over_Time_DF['Vegetarian_Curry_King_Trumpet_Mushroom_Ramen_Revenue_Over_Time'].values
reg = LinearRegression().fit(x, y)
Vegetarian_Curry_King_Trumpet_Mushroom_Ramen_Coef = reg.coef_[0]

y = Item_Revenue_Over_Time_DF['Vegetarian_Spicy_Miso_Revenue_Over_Time'].values
reg = LinearRegression().fit(x, y)
Vegetarian_Spicy_Miso_Coef = reg.coef_[0]

Revenue_Coef = pd.DataFrame(
{
    'Revenue_Coef' : [Burnt_Garlic_Tonkotsu_Ramen_Coef, 
                      Miso_Crab_Ramen_Coef,
                      Nagomi_Shoyu_Revenue_Coef,
                      Shio_Ramen_Coef,
                      Soft_Shell_Miso_Crab_Ramen_Coef,
                      Spicy_Miso_Ramen_Coef,
                      Tonkotsu_Ramen_Coef,
                      Tori_Paitan_Ramen_Coef,
                      Truffle_Butter_Ramen_Coef,
                      Vegetarian_Curry_King_Trumpet_Mushroom_Ramen_Coef,
                      Vegetarian_Spicy_Miso_Coef],
    'Item' : ['Burnt_Garlic_Tonkotsu_Ramen', 
              'Miso_Crab_Ramen',
              'Nagomi_Shoyu_Revenue',
              'Shio_Ramen',
              'Soft_Shell_Miso_Crab_Ramen',
              'Spicy_Miso_Ramen',
              'Tonkotsu_Ramen',
              'Tori_Paitan_Ramen',
              'Truffle_Butter_Ramen',
              'Vegetarian_Curry_King_Trumpet_Mushroom_Ramen',
              'Vegetarian_Spicy_Miso']
})

Revenue_Coef.set_index('Item', inplace = True)

y = Item_Quantity_Over_Time_DF['Burnt_Garlic_Tonkotsu_Ramen_Quantity_Over_Time'].values
reg = LinearRegression().fit(x, y)
Burnt_Garlic_Tonkotsu_Ramen_Coef = reg.coef_[0]

y = Item_Quantity_Over_Time_DF['Miso_Crab_Ramen_Quantity_Over_Time'].values
reg = LinearRegression().fit(x, y)
Miso_Crab_Ramen_Coef = reg.coef_[0]

y = Item_Quantity_Over_Time_DF['Nagomi_Shoyu_Quantity_Over_Time'].values
reg = LinearRegression().fit(x, y)
Nagomi_Shoyu_Revenue_Coef = reg.coef_[0]

y = Item_Quantity_Over_Time_DF['Shio_Ramen_Quantity_Over_Time'].values
reg = LinearRegression().fit(x, y)
Shio_Ramen_Coef = reg.coef_[0]

y = Item_Quantity_Over_Time_DF['Soft_Shell_Miso_Crab_Ramen_Quantity_Over_Time'].values
reg = LinearRegression().fit(x, y)
Soft_Shell_Miso_Crab_Ramen_Coef = reg.coef_[0]

y = Item_Quantity_Over_Time_DF['Spicy_Miso_Ramen_Quantity_Over_Time'].values
reg = LinearRegression().fit(x, y)
Spicy_Miso_Ramen_Coef = reg.coef_[0]

y = Item_Quantity_Over_Time_DF['Tonkotsu_Ramen_Quantity_Over_Time'].values
reg = LinearRegression().fit(x, y)
Tonkotsu_Ramen_Coef = reg.coef_[0]

y = Item_Quantity_Over_Time_DF['Tori_Paitan_Ramen_Quantity_Over_Time'].values
reg = LinearRegression().fit(x, y)
Tori_Paitan_Ramen_Coef = reg.coef_[0]

y = Item_Quantity_Over_Time_DF['Truffle_Butter_Ramen_Quantity_Over_Time'].values
reg = LinearRegression().fit(x, y)
Truffle_Butter_Ramen_Coef = reg.coef_[0]

y = Item_Quantity_Over_Time_DF['Vegetarian_Curry_King_Trumpet_Mushroom_Ramen_Quantity_Over_Time'].values
reg = LinearRegression().fit(x, y)
Vegetarian_Curry_King_Trumpet_Mushroom_Ramen_Coef = reg.coef_[0]

y = Item_Quantity_Over_Time_DF['Vegetarian_Spicy_Miso_Quantity_Over_Time'].values
reg = LinearRegression().fit(x, y)
Vegetarian_Spicy_Miso_Coef = reg.coef_[0]

Quantity_Coef = pd.DataFrame(
{
    'Quantity_Coef' : [Burnt_Garlic_Tonkotsu_Ramen_Coef, 
                      Miso_Crab_Ramen_Coef,
                      Nagomi_Shoyu_Revenue_Coef,
                      Shio_Ramen_Coef,
                      Soft_Shell_Miso_Crab_Ramen_Coef,
                      Spicy_Miso_Ramen_Coef,
                      Tonkotsu_Ramen_Coef,
                      Tori_Paitan_Ramen_Coef,
                      Truffle_Butter_Ramen_Coef,
                      Vegetarian_Curry_King_Trumpet_Mushroom_Ramen_Coef,
                      Vegetarian_Spicy_Miso_Coef],
    'Item' : ['Burnt_Garlic_Tonkotsu_Ramen', 
              'Miso_Crab_Ramen',
              'Nagomi_Shoyu_Revenue',
              'Shio_Ramen',
              'Soft_Shell_Miso_Crab_Ramen',
              'Spicy_Miso_Ramen',
              'Tonkotsu_Ramen',
              'Tori_Paitan_Ramen',
              'Truffle_Butter_Ramen',
              'Vegetarian_Curry_King_Trumpet_Mushroom_Ramen',
              'Vegetarian_Spicy_Miso']
})

Quantity_Coef.set_index('Item', inplace = True)

Revenue_Coef.sort_values(['Revenue_Coef'], ascending = False, inplace = True)
Quantity_Coef.sort_values(['Quantity_Coef'],ascending = False, inplace = True)