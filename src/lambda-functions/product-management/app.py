import json

def get_products(event, context):
    """
    Lambda function to retrieve products from the catalog.
    
    Parameters:
    - event: Event data passed to the Lambda function.
    - context: Runtime information provided by Lambda.
    
    Returns:
    - A response containing the list of products.
    """
    # Dummy product catalog data for demonstration
    products = [
        {'id': 1, 'name': 'Bottled Water - 500ml', 'price': 1.99},
        {'id': 2, 'name': 'Mineral Water - 1L', 'price': 2.99}
    ]
    
    return {
        'statusCode': 200,
        'body': json.dumps(products)
    }
