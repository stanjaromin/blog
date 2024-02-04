import pandas as pd

def main():
# Load sales data into a DataFrame
    sales_data = pd.read_csv('sales_data.csv')

    sales_by_category = sales_data.pivot_table(
        index='Product Category',
        values='Sales',
        aggfunc='sum'
    )

    print(sales_by_category.to_string())    
    

if __name__ == '__main__':
    main()