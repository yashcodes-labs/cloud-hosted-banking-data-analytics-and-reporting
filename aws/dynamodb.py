import boto3

dynamodb = boto3.resource(
    "dynamodb",
    region_name="ap-south-1"   # apni region
)

users_table = dynamodb.Table("Users")
