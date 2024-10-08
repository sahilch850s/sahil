from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'
hostname = 'localhost'
database = 'postgres'  
username = 'postgres'
password = 'Choudhary@717'
port_id = 5432

def fetch_data():

    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=password,
        port=port_id
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM shopping")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

@app.route('/')
def index():
    cart = session.get('cart', [])
    cartlength = len(cart) 
    return render_template('index.html',  cartlength=cartlength)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/cart')
def cart():
    cart = session.get('cart', [])
    print(cart)
    return render_template('add_cart.html', cart=cart)
print(cart)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_name = request.form['product_name']
    product_price = request.form['product_price']

    cart = session.get('cart', [])

    for item in cart:
        if item['product_name'] == product_name:
     
            item['quantity'] += 1
            break
    else:
        cart.append({
            'product_name': product_name,
            'product_price': product_price,
            'quantity': 1,
            'total_price': product_price

        })

    session['cart'] = cart

    return redirect(url_for('index'))
@app.route('/remove_cart', methods=['POST'])
def remove_from_cart():
    product_name = request.form['product_name']
    
    cart = session.get('cart', [])
   
    cart = [item for item in cart if item['product_name'] != product_name]
    
    session['cart'] = cart
    return redirect(url_for('cart'))
    


if __name__ == '__main__':
    app.run(debug=True)
