import boto3
from moto import mock_aws

@mock_aws
def test_table():

    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")

    table = dynamodb.create_table(
        TableName="users",
        KeySchema=[
            {"AttributeName": "id", "KeyType": "HASH"}
        ],
        AttributeDefinitions=[
            {"AttributeName": "id", "AttributeType": "S"}
        ],
        BillingMode="PAY_PER_REQUEST"
    )

    table.put_item(Item={
        "id": "101",
        "name": "Ritik",
        "balance": 5000
    })

    response = table.get_item(Key={"id": "101"})
    print(response["Item"])

test_table()