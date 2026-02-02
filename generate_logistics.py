import pandas as pd

shipment_data = {
    'order_id': [101, 102, 103, 106, 110],
    'planned_ship_date': ['2023-01-02', '2023-01-03', '2023-01-02', '2023-03-11', '2023-05-02'],
    'actual_ship_date': ['2023-01-05', '2023-01-03', '2023-01-07', '2023-03-11', '2023-05-06']
}

df = pd.DataFrame(shipment_data)
df.to_csv('shipments.csv', index=False)
print("Success! 'shipments.csv' created in Project 2 folder.")
