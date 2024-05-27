#!/bin/bash

set -e

# Find the stack name from the SAM configuration file
STACK_NAME=$(awk '/stack_name:/{print $2}' samconfig.toml)

if [ -z "$STACK_NAME" ]; then
  echo "Stack name not found in samconfig.toml"
  exit 1
fi

# Delete the CloudFormation stack
echo "Deleting the CloudFormation stack..."
aws cloudformation delete-stack --stack-name $STACK_NAME

# Wait for the stack to be deleted
echo "Waiting for the stack to be deleted..."
aws cloudformation wait stack-delete-complete --stack-name $STACK_NAME

echo "Teardown complete."
