import os
import re
import pandas as pd
from store.models import Category, Products
from django.contrib.auth.models import User

# Read CSV file into a DataFrame
csv_file_path = 'ML works\dataset\main_dataset.csv'
df = pd.read_csv(csv_file_path)
df= df.dropna()
df['price']=  df['price'].apply(lambda x: re.sub(r'\W+', '', x))
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# base_directory = os.path.dirname(os.path.abspath(csv_file_path))
# Get the admin user
admin_user = User.objects.get(username='admin')

# Iterate through the DataFrame and create model instances
for index, row in df.iterrows():
    # Create or get the Category instance
    category, created = Category.objects.get_or_create(
        name=row['category'],
        defaults={'slug': row['category'].lower().replace(' ', '-')}
    )

    # Get the relative image path from the CSV
    relative_image_path = row['img_paths']  # Assuming 'img_paths' is the column name
    original_path = relative_image_path
    new_prefix = "d:\\\\projects\\\\ecommerce\\\\ML works\\\\dataset\\\\book-covers\\\\"
    # Extract the subpath from the original path
    subpath = original_path.split('/', 1)[1]
    # Construct the new path
    new_path = new_prefix + subpath

    #generate url-friendly slug
    slug = re.sub(r'[^a-zA-Z0-9\-]', '', row['name']).lower().replace(' ', '-')
    # Check if the image path exists
    if os.path.exists(new_path):
        # Create the Product instance
        product = Products(
            title=row['name'],
            category=category,
            created_by=admin_user,
            author=row['author'],
            description='',  # Add your logic to fill in the description if needed
            image=relative_image_path,
            slug=slug,
            price=row['price'],
            in_stock=True,
            is_active=True,
            ratings=row['book_depository_stars']
        )
        product.save()
    else:
        print(f"Image path '{new_path}' not found. Skipping product '{row['name']}'.")

print("CSV data has been loaded into the Django database.")
