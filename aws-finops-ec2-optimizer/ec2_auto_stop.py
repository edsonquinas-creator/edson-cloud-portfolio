import boto3

# Connect to AWS EC2 in the London Region
ec2 = boto3.client('ec2', region_name='eu-west-2')

def stop_dev_instances():
    # Filter for running instances specifically tagged for Development
    filters = [
        {'Name': 'tag:Environment', 'Values': ['Dev']},
        {'Name': 'instance-state-name', 'Values': ['running']}
    ]

    response = ec2.describe_instances(Filters=filters)
    instance_ids = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])

    # Execute the cost-saving shutdown
    if instance_ids:
        print(f"Waste detected! Stopping instances: {instance_ids}")
        ec2.stop_instances(InstanceIds=instance_ids)
        print("Success: Dev instances stopped. Weekend OpEx waste avoided!")
    else:
        print("No running Dev instances found. Your cloud bill is safe.")

if __name__ == '__main__':
    stop_dev_instances()
