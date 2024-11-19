# AWS Lambda File Metadata Extractor

## Overview

The **AWS Lambda File Metadata Extractor** is a serverless application that extracts metadata from files uploaded to an S3 bucket. The metadata includes file size, content type, last modified date, and any custom metadata. Optionally, the metadata can be stored in DynamoDB for further use.

---

## Features

- **Automatic Metadata Extraction**: Triggered by S3 events upon file upload.
- **Rich Metadata Details**: Extracts file size, type, last modified timestamp, and custom metadata.
- **Optional Storage**: Supports saving metadata to DynamoDB.

---

## Workflow

1. A file is uploaded to an S3 bucket.
2. S3 triggers the Lambda function.
3. The Lambda function extracts metadata from the file.
4. Metadata is returned in the response or optionally saved to DynamoDB.

---

## Metadata Example

Sample metadata extracted:

```json
{
  "Bucket": "example-bucket",
  "Key": "example-file.txt",
  "FileSize": 2048,
  "ContentType": "text/plain",
  "LastModified": "2024-11-19 12:30:45",
  "Metadata": {
    "customKey": "customValue"
  }
}
