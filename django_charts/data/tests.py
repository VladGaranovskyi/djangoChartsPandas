import pandas as pd
from datetime import datetime
from django.test import TestCase
from .models import Purchase
from .methods import csv_to_db, objects_to_df, Chart

class TestCSVToDB(TestCase):
    def test_csv_to_db(self):
        # Assume 'supermarket_sales.csv' file contains correct data
        csv_to_db()
        # Check if any Purchase objects are created
        purchases_count = Purchase.objects.count()
        self.assertGreater(purchases_count, 0)

class TestObjectsToDF(TestCase):
    def setUp(self):
        # Assume we have some Purchase objects in the database
        Purchase.objects.create(
            city='City1',
            customer_type='Type1',
            gender='Male',
            unit_price=10.0,
            quantity=2,
            product_line='Product1',
            tax=1.0,
            total=21.0,
            date=datetime.now().date(),
            time=datetime.now().time(),
            payment='Cash',
            cogs=9.0,
            profit=11.0,
            rating=4.5
        )
        Purchase.objects.create(
            city='City2',
            customer_type='Type2',
            gender='Female',
            unit_price=20.0,
            quantity=1,
            product_line='Product2',
            tax=2.0,
            total=22.0,
            date=datetime.now().date(),
            time=datetime.now().time(),
            payment='Card',
            cogs=18.0,
            profit=4.0,
            rating=3.5
        )

    def test_objects_to_df(self):
        # Get DataFrame from Purchase objects
        df = objects_to_df(Purchase)
        # Check if DataFrame is not empty
        self.assertFalse(df.empty)

class TestChart(TestCase):
    def test_get_html(self):
        chart = Chart(chart_type='bar')
        html_code = chart.get_html()
        # Check if the HTML code is generated correctly
        self.assertIn('<canvas id=', html_code)

    def test_get_js(self):
        chart = Chart(chart_type='bar')
        js_code = chart.get_js()
        # Check if the JavaScript code is generated correctly
        self.assertIn('var chartElement = document.getElementById', js_code)

    def test_get_presentation(self):
        chart = Chart(chart_type='bar')
        presentation = chart.get_presentation()
        # Check if the presentation contains HTML and JavaScript codes
        self.assertIn('html', presentation)
        self.assertIn('js', presentation)

