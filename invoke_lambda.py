import json
import boto3


def main():
    lambda_client = boto3.client("lambda", region_name="eu-north-1")

    event = {
        "name": "Sas"
    }

    response = lambda_client.invoke(
        FunctionName="HelloStudentFunction",
        InvocationType="RequestResponse",
        Payload=json.dumps(event).encode("utf-8")
    )

    payload_bytes = response["Payload"].read()
    result = json.loads(payload_bytes)

    print("Raw Lambda response:", result)
    print("statusCode:", result.get("statusCode"))
    print("body:", result.get("body"))


if __name__ == "__main__":
    main()

