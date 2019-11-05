import boto3
from boto3.session import Session
from botocore.client import Config
import uuid
import os
import logging
import json
from datetime import datetime

LOGGER = logging.getLogger()
LOGGER.setLevel(os.getenv('LOG_LEVEL', 'WARNING'))

S3_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
S3_PUT_ROLE_NAME = os.environ['PUT_S3_ROLE']
DURATION_SECONDS = 900 # Pre-Signed URLの有効期限(秒) 最小値 900
REGION_NAME='ap-northeast-1'

def createPresignedUrl(event, context):
    LOGGER.info(json.dumps(event))

    FILE_NAME = str(uuid.uuid4())
    LOGGER.info('target file name to upload at ' + FILE_NAME)

    client = boto3.client('sts')
    accountId = client.get_caller_identity()['Account']
    
    LOGGER.info('accountId: ' + accountId)

    ROLE_ARN = createRoleArn(accountId)
    LOGGER.info('roleArn: ' + ROLE_ARN)

    assumeRoleResponse = client.assume_role(RoleArn=ROLE_ARN,
        RoleSessionName=FILE_NAME,
        DurationSeconds=DURATION_SECONDS
    )

    LOGGER.info(assumeRoleResponse)

    session = Session(
        aws_access_key_id=assumeRoleResponse['Credentials']['AccessKeyId'],
        aws_secret_access_key=assumeRoleResponse['Credentials']['SecretAccessKey'],
        aws_session_token=assumeRoleResponse['Credentials']['SessionToken'],
        region_name=REGION_NAME
    )

    s3 = session.client('s3', config=Config(signature_version='s3v4'))

    url = s3.generate_presigned_url(
        ClientMethod = 'put_object',
        Params = {'Bucket' : S3_BUCKET_NAME, 'Key' : createS3Key(FILE_NAME)},
        ExpiresIn = DURATION_SECONDS,
        HttpMethod = 'PUT'
    )

    LOGGER.info(url)

    body = {
        'redirectUrl' : url
    }

    header = {
        'Access-Control-Allow-Origin' : responseCors(event['headers']['origin']) # originヘッダがないと死ぬ
    }

    response = {
        'statusCode': 200,
        'headers': header,
        'body': json.dumps(body)
    }

    return response


def createRoleArn(accountId):
    return 'arn:aws:iam::' + accountId + ':role/UploadService/' + S3_PUT_ROLE_NAME

def createS3Key(fileName):
    return datetime.now().strftime('%Y-%m-%d') + '/' + fileName

def responseCors(origin):
    return origin if origin else '*'


