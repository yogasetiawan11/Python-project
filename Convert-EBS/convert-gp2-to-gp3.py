import json
import boto3

def check_volume_id(volume_arn):
    # Split the ARN with colon ':' as separator
    arn_parts = volume_arn.split(':')
    # The volume ID is the last part after splitting by '/'
    volume_id = arn_parts[-1].split('/')[-1]
    return volume_id

def lambda_handler(event, context):
    # print resources arn from event json cloudwatch event
    volume_arn = events['resources'][0]
    volume_id = get_volume_id_from_arn(volume_arn)

    # we use ec2 client because volume is part of ec2 service
    ec2_client = boto3.client('ec2')
    response = ec2_client.modify_volume(
        VolumeId='volume_id',
        VolumeType='gp3',
)