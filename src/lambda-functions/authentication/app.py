import json

def authenticate_user(event, context):
    """
    Lambda function to authenticate users.
    
    Parameters:
    - event: Event data passed to the Lambda function.
    - context: Runtime information provided by Lambda.
    
    Returns:
    - A response containing the user authentication status.
    """
    # Dummy authentication logic for demonstration
    user_id = event.get('userId')
    if user_id:
        authenticated = True
        message = f"User {user_id} authenticated successfully."
    else:
        authenticated = False
        message = "Authentication failed. User ID not provided."
    
    return {
        'statusCode': 200,
        'body': json.dumps({'authenticated': authenticated, 'message': message})
    }
