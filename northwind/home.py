from flask import render_template,request,redirect,url_for
from northwind import application
from northwind.helper import connect_to_db

@application.route('/', methods=['GET', 'POST'])
def home():

    return render_template('home.html')

@application.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'show_table':
            # Perform action to show all table data
            conn = connect_to_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM orders")
            result = cursor.fetchall()
            return render_template('result.html', table_data=result)

        elif action == 'add_row':
            # Perform action to add a row
            # add_row_function()
            result = "New row added"
            return render_template('result.html', table_data=result)

        elif action == 'delete_value':
            # Perform action to delete a value
            # delete_value_function()
            result = "Value deleted"
            return render_template('result.html', table_data=result)

    return redirect(url_for('home'))

