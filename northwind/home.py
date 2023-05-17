from flask import render_template,request,redirect,url_for
from northwind import application
from northwind.helper import connect_to_db
import random

@application.route('/', methods=['GET', 'POST'])
def home():

    return render_template('home.html')

@application.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'show_order_table':
            # Perform action to show all table data
            conn = connect_to_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM orders")
            result = cursor.fetchall()
            return render_template('result.html', table_data=result)

        elif action == 'show_employee_table':
            conn = connect_to_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employees")
            result = cursor.fetchall()
            return render_template('result.html', table_data=result)

        elif action == 'show_region_table':
            conn = connect_to_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM region")
            result = cursor.fetchall()
            return render_template('result.html', table_data=result)
        
        elif action == 'add_region':
            conn = connect_to_db()
            cursor = conn.cursor()
            region_value = request.form.get('add_region')
            random_number = random.randint(10, 100000)
            cursor.execute("INSERT INTO region (region_id,region_description) VALUES (%s,%s)", (random_number,region_value))
            conn.commit()
            result = 'Region Added Succesfully'
            return render_template('result.html', table_data=result)
        

    return redirect(url_for('home'))

