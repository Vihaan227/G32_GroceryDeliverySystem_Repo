# from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# from werkzeug.security import generate_password_hash, check_password_hash
# from datetime import UTC 

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your-secret-key'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///groceryhub.db'
# db = SQLAlchemy(app)
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'

# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password_hash = db.Column(db.String(128))

#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)
    

# class Product(db.Model):
#     __tablename__ = 'products'
    
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.Text)
#     price = db.Column(db.Float, nullable=False)
#     stock = db.Column(db.Integer, default=0)
#     image_url = db.Column(db.String(255))
#     category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
#     category = db.relationship('Category', backref='products')

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

# @app.route('/')
# def index():
#     top_stores = [
#         {"name": "Store A", "discount": 50, "image": "https://via.placeholder.com/300x200"},
#         {"name": "Store B", "discount": 30, "image": "https://via.placeholder.com/300x200"},
#         {"name": "Store C", "discount": 25, "image": "https://via.placeholder.com/300x200"},
#     ]
    
#     categories = [
#         {"name": "Fastest Growing", "description": "Top 10 fastest growing stores", "icon": "bi-graph-up", "filter": "fastest-growing"},
#         {"name": "Electronics", "description": "Latest gadgets and tech", "icon": "bi-laptop", "filter": "electronics"},
#         {"name": "Alcohol & Liquor", "description": "Wide selection of spirits", "icon": "bi-cup-straw", "filter": "alcohol"},
#         {"name": "Wholesale", "description": "Bulk buying options", "icon": "bi-box-seam", "filter": "wholesale"},
#         {"name": "Retail", "description": "Individual item purchases", "icon": "bi-shop", "filter": "retail"},
#         {"name": "Self Pickup", "description": "Collect your order in-store", "icon": "bi-bag-check", "filter": "self-pickup"},
#         {"name": "Grocery", "description": "Fresh produce and essentials", "icon": "bi-cart3", "filter": "grocery"},
#         {"name": "Music", "description": "Essentials to professional gear", "icon": "bi-music-note", "filter": "grocery"},
#     ]
    
#     fastest_growing_stores = [
#         {"name": "TechMart", "rating": 4.5, "description": "Cutting-edge electronics", "image": "../static/unnamed.jpg"},
#         {"name": "FreshGrocer", "rating": 4.8, "description": "Farm-fresh produce", "image": "../static/2.png"},
#         {"name": "BulkBuy", "rating": 4.2, "description": "Wholesale savings", "image": "../static/bulk.jpg"},
#     ]
    
#     return render_template('index.html', top_stores=top_stores, categories=categories, fastest_growing_stores=fastest_growing_stores)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         userEmail = request.form.get('email')
#         user = User.query.filter_by(email=userEmail).first()

#         if (userEmail == user.email and user.check_password(request.form['password'])):
#             login_user(user)
#             flash('Logged in successfully.', 'success')
#             return redirect(url_for('index'))
#         else:
#             flash('Invalid username or password', 'error')
#     return render_template('login.html')


# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('index'))

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         user = User(username=request.form['username'], email=request.form['email'])
#         user.set_password(request.form['password'])
#         db.session.add(user)
#         db.session.commit()
#         flash('Registration successful. Please log in.', 'success')
#         return redirect(url_for('login'))
#     return render_template('register.html')

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)

# @app.route("/grocery")
# @login_required
# def grocery():
#     return render_template("grocery.html")

from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, UTC
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///groceryhub.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    carts = db.relationship('Cart', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    
    def __repr__(self):
        return f'<Category {self.name}>'

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    image_url = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    category = db.relationship('Category', backref='products')
    
    def __repr__(self):
        return f'<Product {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'stock': self.stock,
            'image_url': self.image_url,
            'category': self.category.name if self.category else None
        }

class Cart(db.Model):
    __tablename__ = 'carts'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # For logged-in users
    session_id = db.Column(db.String(100), nullable=True)  # For guest users
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    items = db.relationship('CartItem', backref='cart', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Cart {self.id}>'
    
    def add_item(self, product_id, quantity=1):
        """Add a product to cart or update quantity if already exists"""
        item = CartItem.query.filter_by(cart_id=self.id, product_id=product_id).first()
        
        if item:
            item.quantity += quantity
        else:
            item = CartItem(cart_id=self.id, product_id=product_id, quantity=quantity)
            db.session.add(item)
        
        db.session.commit()
        return item
    
    def remove_item(self, product_id):
        """Remove a product from cart"""
        item = CartItem.query.filter_by(cart_id=self.id, product_id=product_id).first()
        
        if item:
            db.session.delete(item)
            db.session.commit()
            return True
        return False
    
    def update_item(self, product_id, quantity):
        """Update quantity of a product in cart"""
        item = CartItem.query.filter_by(cart_id=self.id, product_id=product_id).first()
        
        if not item:
            return False
        
        if quantity <= 0:
            return self.remove_item(product_id)
        
        item.quantity = quantity
        db.session.commit()
        return item
    
    def clear(self):
        """Remove all items from cart"""
        CartItem.query.filter_by(cart_id=self.id).delete()
        db.session.commit()
    
    def get_total(self):
        """Calculate total price of all items in cart"""
        total = 0
        for item in self.items:
            product = Product.query.get(item.product_id)
            if product:
                total += product.price * item.quantity
        return round(total, 2)
    
    def get_item_count(self):
        """Get total number of items in cart"""
        return sum(item.quantity for item in self.items)
    
    def to_dict(self):
        """Return cart data as dictionary"""
        items = []
        total = 0
        
        for item in self.items:
            product = Product.query.get(item.product_id)
            if product:
                item_total = product.price * item.quantity
                items.append({
                    'id': item.id,
                    'product_id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'quantity': item.quantity,
                    'total': round(item_total, 2),
                    'image_url': product.image_url
                })
                total += item_total
        
        return {
            'id': self.id,
            'items': items,
            'total': round(total, 2),
            'item_count': self.get_item_count()
        }

class CartItem(db.Model):
    __tablename__ = 'cart_items'
    
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    product = db.relationship('Product')
    
    def __repr__(self):
        return f'<CartItem {self.id}>'

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    items = db.relationship('OrderItem', backref='order', lazy=True)
    user = db.relationship('User', backref='orders')

class OrderItem(db.Model):
    __tablename__ = 'order_items'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    
    product = db.relationship('Product')

# Cart Service
def get_or_create_cart():
    """Get existing cart or create a new one based on user login state"""
    if current_user.is_authenticated:
        # Logged-in user: Get their cart or create if not exists
        cart = Cart.query.filter_by(user_id=current_user.id).first()
        if not cart:
            cart = Cart(user_id=current_user.id)
            db.session.add(cart)
            db.session.commit()
        
        # If there was a session cart, merge it
        if 'cart_session_id' in session:
            session_cart = Cart.query.filter_by(session_id=session['cart_session_id']).first()
            if session_cart:
                # Transfer items from session cart to user cart
                for item in session_cart.items:
                    cart.add_item(item.product_id, item.quantity)
                
                # Delete the session cart
                db.session.delete(session_cart)
                db.session.commit()
                
                # Clear session cart ID
                session.pop('cart_session_id', None)
        
        return cart
    else:
        # Guest user: Use session-based cart
        if 'cart_session_id' not in session:
            session['cart_session_id'] = str(uuid.uuid4())
        
        cart = Cart.query.filter_by(session_id=session['cart_session_id']).first()
        if not cart:
            cart = Cart(session_id=session['cart_session_id'])
            db.session.add(cart)
            db.session.commit()
        
        return cart

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    top_stores = [
        {"name": "Store A", "discount": 50, "image": "https://via.placeholder.com/300x200"},
        {"name": "Store B", "discount": 30, "image": "https://via.placeholder.com/300x200"},
        {"name": "Store C", "discount": 25, "image": "https://via.placeholder.com/300x200"},
    ]
    
    categories = [
        {"name": "Fastest Growing", "description": "Top 10 fastest growing stores", "icon": "bi-graph-up", "filter": "fastest-growing","link":"grocery"},
        {"name": "Electronics", "description": "Latest gadgets and tech", "icon": "bi-laptop", "filter": "electronics","link":"grocery"},
        {"name": "Alcohol & Liquor", "description": "Wide selection of spirits", "icon": "bi-cup-straw", "filter": "alcohol","link":"grocery"},
        {"name": "Wholesale", "description": "Bulk buying options", "icon": "bi-box-seam", "filter": "wholesale","link":"grocery"},
        {"name": "Retail", "description": "Individual item purchases", "icon": "bi-shop", "filter": "retail","link":"grocery"},
        {"name": "Self Pickup", "description": "Collect your order in-store", "icon": "bi-bag-check", "filter": "self-pickup","link":"grocery"},
        {"name": "Grocery", "description": "Fresh produce and essentials", "icon": "bi-cart3", "filter": "grocery", "link":"grocery"},
        {"name": "Music", "description": "Essentials to professional gear", "icon": "bi-music-note", "filter": "grocery","link":"grocery"},
    ]
    
    fastest_growing_stores = [
        {"name": "TechMart", "rating": 4.5, "description": "Cutting-edge electronics", "image": "../static/unnamed.jpg"},
        {"name": "FreshGrocer", "rating": 4.8, "description": "Farm-fresh produce", "image": "../static/2.png"},
        {"name": "BulkBuy", "rating": 4.2, "description": "Wholesale savings", "image": "../static/bulk.jpg"},
    ]
    
    return render_template('index.html', top_stores=top_stores, categories=categories, fastest_growing_stores=fastest_growing_stores)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userEmail = request.form.get('email')
        user = User.query.filter_by(email=userEmail).first()

        if user and user.check_password(request.form['password']):
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User(username=request.form['username'], email=request.form['email'])
        user.set_password(request.form['password'])
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route("/grocery")
@login_required
def grocery():
    # Get products for the grocery page
    products = Product.query.all()
    return render_template("grocery.html", products=products)

# @app.route("/wine")
# @login_required
# def wine():
#     return("wine.html")

# @app.route("/wholesale")
# @login_required
# def wholesale():
#     return("wholesale.html")

# @app.route("/retail")
# @login_required
# def retail():
#     return("retail.html")

# @app.route("/musicc")
# @login_required
# def musicc():
#     return render_template('musicc.html')

# @app.route("/electronic")
# @login_required
# def electronic():
#     return render_template('electronic.html')

# @app.route("/Self Pickup")
# @login_required
# def self_pickup ():
#     return render_template('.html')


# Cart routes
@app.route('/cart')
def view_cart():
    cart = get_or_create_cart()
    return render_template('cart.html', cart=cart.to_dict())

@app.route('/cart/add/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    quantity = int(request.form.get('quantity', 1))
    
    # Verify product exists and has sufficient stock
    product = Product.query.get_or_404(product_id)
    if product.stock < quantity:
        flash(f'Sorry, only {product.stock} units available', 'warning')
        return redirect(request.referrer or url_for('grocery'))
    
    cart = get_or_create_cart()
    cart.add_item(product_id, quantity)
    
    flash(f'{product.name} added to your cart', 'success')
    return redirect(request.referrer or url_for('grocery'))

@app.route('/cart/update/<int:product_id>', methods=['POST'])
def update_cart_item(product_id):
    quantity = int(request.form.get('quantity', 0))
    
    cart = get_or_create_cart()
    if quantity > 0:
        # Verify product has sufficient stock
        product = Product.query.get_or_404(product_id)
        if product.stock < quantity:
            flash(f'Sorry, only {product.stock} units available', 'warning')
            return redirect(url_for('view_cart'))
            
        cart.update_item(product_id, quantity)
        flash('Cart updated', 'success')
    else:
        cart.remove_item(product_id)
        flash('Item removed from cart', 'success')
    
    return redirect(url_for('view_cart'))

@app.route('/cart/remove/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    cart = get_or_create_cart()
    cart.remove_item(product_id)
    
    flash('Item removed from cart', 'success')
    return redirect(url_for('view_cart'))

@app.route('/cart/clear', methods=['POST'])
def clear_cart():
    cart = get_or_create_cart()
    cart.clear()
    
    flash('Cart cleared', 'success')
    return redirect(url_for('view_cart'))

# API endpoints for cart (for AJAX functionality)
@app.route('/api/cart', methods=['GET'])
def api_get_cart():
    cart = get_or_create_cart()
    return jsonify(cart.to_dict())

@app.route('/api/cart/add/<int:product_id>', methods=['POST'])
def api_add_to_cart(product_id):
    data = request.get_json() or {}
    quantity = int(data.get('quantity', 1))
    
    product = Product.query.get_or_404(product_id)
    if product.stock < quantity:
        return jsonify({'success': False, 'message': f'Only {product.stock} available'}), 400
    
    cart = get_or_create_cart()
    cart.add_item(product_id, quantity)
    
    return jsonify({
        'success': True,
        'message': f'{product.name} added to cart',
        'cart': cart.to_dict()
    })

# Checkout process
@app.route('/checkout', methods=['GET'])
@login_required
def checkout():
    cart = get_or_create_cart()
    if not cart.items:
        flash('Your cart is empty', 'warning')
        return redirect(url_for('grocery'))
    
    return render_template('checkout.html', cart=cart.to_dict())

@app.route('/checkout/complete', methods=['POST'])
@login_required
def complete_order():
    cart = get_or_create_cart()
    if not cart.items:
        flash('Your cart is empty', 'warning')
        return redirect(url_for('grocery'))
    
    # Create new order
    order = Order(
        user_id=current_user.id,
        total_amount=cart.get_total()
    )
    db.session.add(order)
    db.session.flush()  # Get the order ID
    
    # Transfer cart items to order items
    for item in cart.items:
        product = Product.query.get(item.product_id)
        if not product or product.stock < item.quantity:
            db.session.rollback()
            flash(f'Not enough stock for {product.name if product else "a product"}', 'danger')
            return redirect(url_for('checkout'))
        
        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=product.price
        )
        db.session.add(order_item)
        
        # Update product stock
        product.stock -= item.quantity
    
    # Clear the cart and commit the order
    cart.clear()
    db.session.commit()
    
    flash('Order placed successfully!', 'success')
    return redirect(url_for('order_confirmation', order_id=order.id))

@app.route('/order/<int:order_id>')
@login_required
def order_confirmation(order_id):
    order = Order.query.filter_by(id=order_id, user_id=current_user.id).first_or_404()
    return render_template('order_confirmation.html', order=order)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        # Add sample categories if none exist
        if not Category.query.first():
            categories = [
                Category(name='Fruits'),
                Category(name='Vegetables'),
                Category(name='Dairy'),
                Category(name='Bakery'),
                Category(name='Beverages')
            ]
            db.session.bulk_save_objects(categories)
            db.session.commit()
            
        # Add sample products if none exist
        if not Product.query.first():
            fruits = Category.query.filter_by(name='Fruits').first()
            if fruits:
                products = [
                    Product(name='Apples', description='Fresh red apples', price=2.99, stock=100, 
                            category_id=fruits.id, image_url='/static/products/apple.jpg'),
                    Product(name='Bananas', description='Bunch of ripe bananas', price=1.99, stock=150, 
                            category_id=fruits.id, image_url='/static/products/banana.jpg'),
                ]
                db.session.bulk_save_objects(products)
                db.session.commit()
    
    app.run(debug=True)