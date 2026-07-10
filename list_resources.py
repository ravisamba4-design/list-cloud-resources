import boto3

def list_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    print("S3 Buckets:")
    if not response['Buckets']:
        print("  (none found)")
    for bucket in response['Buckets']:
        print(f"  - {bucket['Name']}")

def list_ec2_instances():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    print("\nEC2 Instances:")
    found = False
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            found = True
            print(f"  - {instance['InstanceId']} ({instance['State']['Name']})")
    if not found:
        print("  (none found)")

if __name__ == "__main__":
    list_s3_buckets()
    list_ec2_instances()
