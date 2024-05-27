import json

def process_order(event, context):
    """
    Lambda function to process orders.
    
    Parameters:
    - event: Event data passed to the Lambda function.
    - context: Runtime information provided by Lambda.
    
    Returns:
    - A response containing the order processing status.
    """
    # Dummy order processing logic for demonstration
    order_data = json.loads(event['body'])
    if order_data:
        order_id = generate_order_id()
        message = f"Order {order_id} processed successfully."
    else:
        order_id = None
        message = "Order processing failed. No order data provided."
    
    return {
        'statusCode': 200,
        'body': json.dumps({'orderId': order_id, 'message': message})
    }

def generate_order_id():
    """
    Function to generate a unique order ID.
    
    Returns:
    - A unique order ID.
    """
    # Logic to generate a unique order ID (e.g., using UUID)
    return 'ORD123456789'
