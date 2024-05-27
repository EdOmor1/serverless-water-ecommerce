# AWS: serverless-water-ecommerce

This is a Serverless Web Application built with AWS Lambda and RDS for an e-commerce platform selling water products.

## Features

- **Authentication:** Authenticate users and manage access to the platform.
- **Product Management:** Manage the product catalog and inventory.
- **Order Processing:** Process orders and update inventory accordingly.

## Prerequisites

- AWS account with appropriate permissions
- AWS CLI installed and configured
- AWS SAM CLI installed
- Python 3.8 or higher

## Getting Started

1. Clone this repository.
2. Navigate to the `serverless-water-ecommerce` directory.
3. Deploy the application using SAM CLI:
   sam build
   sam deploy --guided
5. Access the deployed API endpoints to interact with the application.

## Usage

- `/authenticate`: POST endpoint for user authentication.
- `/products`: GET endpoint to retrieve the product catalog.
- `/orders`: POST endpoint to place orders.


