import json
import boto3
import os
from datetime import datetime

s3 = boto3.client("s3")

def lambda_handler(event, context):
    try:
        # Log the event data
        print("Received event:", json.dumps(event, indent=2))
        
        # Extract file details from the event
        for record in event.get("Records", []):
            bucket_name = record["s3"]["bucket"]["name"]
            object_key = record["s3"]["object"]["key"]

            # Get object metadata
            response = s3.head_object(Bucket=bucket_name, Key=object_key)
            metadata = {
                "Bucket": bucket_name,
                "Key": object_key,
                "FileSize": response["ContentLength"],
                "ContentType": response["ContentType"],
                "LastModified": response["LastModified"].strftime("%Y-%m-%d %H:%M:%S"),
                "Metadata": response.get("Metadata", {})
            }

            # Log extracted metadata
            print("File Metadata:", metadata)

            # Optionally, write the metadata to a DynamoDB table
            # Uncomment the following lines if you wish to use DynamoDB
            # save_to_dynamodb(metadata)

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Metadata extracted successfully", "metadata": metadata})
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

# Uncomment this function to store metadata in DynamoDB
# dynamodb = boto3.resource("dynamodb")
# table_name = "FileMetadataTable"  # Replace with your DynamoDB table name
# table = dynamodb.Table(table_name)

# def save_to_dynamodb(metadata):
#     table.put_item(Item=metadata)
