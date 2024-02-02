from products.models import Product

# Function to return all products 
def get_all_products():
    return Product.objects.all()

# TODO: Create a function to create a new product in DB
def create_new_product(
        brand, 
        name, 
        type, 
        size, 
        measure_unit,
        stock_product,
        color,
        status
    ):
    product = Product(
        brand=brand,
        name=name,
        type=type,
        size=size,
        measure_unit=measure_unit,
        stock=stock_product,
        color=color,
        status=status
        )
    
    product.save()


# TODO: Create function to get a product using id or pk. 



# TODO: Create a function to filter a specific product using id or pk. Filter only actives.



# TODO: Create a function to filter a specific product by type. Filter only actives


