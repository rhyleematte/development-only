from django.db import migrations
from django.db import connection

# Custom function to create tables if they do not already exist
def create_or_ignore_tables(apps, schema_editor):
    with connection.cursor() as cursor:
        try:
            # Creating 'api_cart' table if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS api_cart (
                    id BIGINT(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    user_id BIGINT(20) NOT NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """)
            # Creating 'api_cartitem' table if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS api_cartitem (
                    id BIGINT(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    quantity INT(10) UNSIGNED NOT NULL CHECK (quantity >= 0),
                    cart_id BIGINT(20) NOT NULL,
                    product_id BIGINT(20) NOT NULL,
                    FOREIGN KEY (cart_id) REFERENCES api_cart(id),
                    FOREIGN KEY (product_id) REFERENCES api_product(id)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """)
            # You can continue with other tables as needed, for example 'api_product' and so on
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS api_product (
                    id BIGINT(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    price DECIMAL(10, 2) NOT NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """)
            # Continue for other tables like 'api_chat', 'api_contact', etc.
            print("Tables created or already exist.")
        except Exception as e:
            print(f"Error creating tables: {e}")

class Migration(migrations.Migration):

    # Dependencies define the order in which migrations are applied
    dependencies = [
        ('api', '0003_cart_product_cartitem'),
    ]

    # Operations to run the custom function
    operations = [
        migrations.RunPython(create_or_ignore_tables),
    ]
