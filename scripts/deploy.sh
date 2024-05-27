#!/bin/bash

set -e

# Build the SAM application
echo "Building the SAM application..."
sam build

# Deploy the SAM application
echo "Deploying the SAM application..."
sam deploy --guided

echo "Deployment complete."
