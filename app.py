from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data dummy untuk produk makanan lokal
products = [
    {"id": 1, "name": "Nasi Gudeg Jogja", "price": 25000, "description": "Gudeg khas Yogyakarta dengan ayam dan telur.", "image": "gudeg.jpg"},
    {"id": 2, "name": "Rendang Padang", "price": 35000, "description": "Rendang daging sapi asli dari Padang.", "image": "rendang.jpg"},
    {"id": 3, "name": "Sate Madura", "price": 20000, "description": "Sate ayam dengan bumbu kacang khas Madura.", "image": "sate.jpg"},
    {"id": 4, "name": "Bakso Malang", "price": 15000, "description": "Bakso urat dengan mie dan sayuran.", "image": "bakso.jpg"}
]

cart = []

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return render_template('product.html', product=product)
    return "Produk tidak ditemukan", 404

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)
    return redirect(url_for('cart_view'))

@app.route('/cart')
def cart_view():
    total = sum(p['price'] for p in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/checkout', methods=['POST'])
def checkout():
    # Simulasi checkout
    cart.clear()
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)