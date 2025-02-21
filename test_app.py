import unittest
from app import app, db, User

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_index(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.app.post('/register', data=dict(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        ), follow_redirects=True)
        self.assertIn(b'Registration successful', response.data)

    def test_login_logout(self):
        self.app.post('/register', data=dict(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        ), follow_redirects=True)
        
        response = self.app.post('/login', data=dict(
            username='testuser',
            password='testpassword'
        ), follow_redirects=True)
        self.assertIn(b'Logged in successfully', response.data)

        response = self.app.get('/logout', follow_redirects=True)
        self.assertIn(b'GroceryHub', response.data)

    def test_add_to_cart(self):
        # First register and login a user
        self.app.post('/register', data=dict(
            username='cartuser',
            email='cart@example.com',
            password='cartpass'
        ), follow_redirects=True)
        self.app.post('/login', data=dict(
            username='cartuser',
            password='cartpass'
        ), follow_redirects=True)
        
        # Test adding item to cart
        response = self.app.post('/add_to_cart', data=dict(
            product_id=1,
            quantity=2
        ), follow_redirects=True)
        self.assertIn(b'Item added to cart', response.data)

    def test_view_cart(self):
        # First register and login a user
        self.app.post('/register', data=dict(
            username='cartuser',
            email='cart@example.com',
            password='cartpass'
        ), follow_redirects=True)
        self.app.post('/login', data=dict(
            username='cartuser',
            password='cartpass'
        ), follow_redirects=True)
        
        response = self.app.get('/cart', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Shopping Cart', response.data)

    def test_invalid_login(self):
        response = self.app.post('/login', data=dict(
            username='nonexistent',
            password='wrongpass'
        ), follow_redirects=True)
        self.assertIn(b'Invalid username or password', response.data)

if __name__ == '__main__':
    unittest.main()

