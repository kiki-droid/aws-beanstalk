from __future__ import print_function
import boto3

client = boto3.client('elasticbeanstalk')

response = client.create_application_version(
    ApplicationName='todo_app',
    VersionLabel='v1',
    Description='todo_flask_app',
    SourceBundle={
        'S3Bucket': '',
        'S3Key': 'todo_app.zip'
    },
    AutoCreateApplication=True,
    Process=True
)
