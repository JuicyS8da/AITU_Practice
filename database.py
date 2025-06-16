import sqlite3
from models import Product

class ProductDB:
    def __init__(self, db_path: str = "products.db"):
        self.connection = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    brand TEXT,
                    model TEXT,
                    price_value REAL,
                    currency TEXT DEFAULT 'USD',
                    country_origin TEXT,
                    color TEXT,
                    weight_g INTEGER,
                    product_code TEXT UNIQUE
                )
            """)

    def insert_product(self, product: Product):
        try:
            price = float(product.price_value) if product.price_value.lower() != 'none' else None
            weight = int(product.weight_g) if product.weight_g.isdigit() else None
            currency = product.currency or 'USD'

            with self.connection:
                self.connection.execute("""
                    INSERT INTO products (
                        brand, model, price_value, currency,
                        country_origin, color, weight_g, product_code
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    product.brand,
                    product.model,
                    price,
                    currency,
                    product.country_origin,
                    product.color,
                    weight,
                    product.product_code
                ))
                print(f"✅ Inserted: {product.brand} {product.model}")
        except sqlite3.IntegrityError:
            print(f"⚠️ Product with code {product.product_code} already exists.")
        except Exception as e:
            print(f"❌ Error inserting product: {e}")
    
    def get_all_products(self):
        with self.connection:
            cursor = self.connection.execute("SELECT * FROM products")
            return cursor.fetchall()

