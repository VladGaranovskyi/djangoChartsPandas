import pandas as pd
from .models import Purchase
from datetime import datetime


def csv_to_db():
    df = pd.read_csv('data/supermarket_sales.csv')  # use pandas to read the csv
    records = df.to_records()  # convert to records

    # loop through and create a purchase object using django
    for record in records:
        purchase = Purchase(
            city=record[3],
            customer_type=record[4],
            gender=record[5],
            product_line=record[6],
            unit_price=record[7],
            quantity=record[8],
            tax=record[9],
            total=record[10],
            date=datetime.strptime(record[11], '%m/%d/%Y').date(),
            time=record[12],
            payment=record[13],
            cogs=record[14],
            profit=record[16],
            rating=record[17],
        )
        purchase.save()
