import boto3

def create_bucket(bucket_name):
  """Creates an S3 bucket."""
  s3 = boto3.resource("s3")
  s3.create_bucket(Bucket=bucket_name)

def upload_file(bucket_name, file_path):
  """Uploads a file to an S3 bucket."""
  s3 = boto3.resource("s3")
  s3.Bucket(bucket_name).upload_file(file_path)

def create_lambda_function(function_name, handler, runtime="python3.8"):
  """Creates a Lambda function."""
  lambda_client = boto3.client("lambda")
  lambda_client.create_function(
    FunctionName=function_name,
    Runtime=runtime,
    Handler=handler
  )

def create_dynamodb_table(table_name, primary_key="id"):
  """Creates a DynamoDB table."""
  dynamodb = boto3.resource("dynamodb")
  dynamodb.create_table(
    TableName=table_name,
    KeySchema=[{"AttributeName": primary_key, "KeyType": "HASH"}]
  )

def create_api_gateway(rest_api_id, resource_path, method="GET"):
  """Creates an API Gateway REST API."""
  api_gateway = boto3.client("apigateway")
  api_gateway.create_rest_api(RestApiId=rest_api_id, ResourcePath=resource_path, Method=method)

def main():
  """The main function."""
  create_bucket("my-bucket")
  upload_file("my-bucket", "my-file.txt")
  create_lambda_function("my-function", "my_function.lambda_handler")
  create_dynamodb_table("my-table", "id")
  create_api_gateway("my-api-gateway", "/my-resource")

if _name_ == "_main_":
  main()