from __future__ import print_function
import boto3

client = boto3.client('elasticbeanstalk')

response_env = client.create_environment(
    ApplicationName='todo_app',
    EnvironmentName='todoapp-env',
    CNAMEPrefix='to-do-cname',
    Tier={
        'Name': 'WebServer',
        'Type': 'Standard',
        'Version': '1.0'
    },

    VersionLabel='v1',
    PlatformArn='arn:aws:elasticbeanstalk:ap-south-1::platform/Python 3.8 running on 64bit Amazon Linux 2/3.3.17',
    OptionSettings=[
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "IamInstanceProfile",
            "Value": "aws-elasticbeanstalk-ec2-role",
        },
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "InstanceType",
            "Value": "t2.micro",
        },
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "EC2KeyName",
            "Value": "",
        },
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "ImageId",
            "Value": "ami-076e3a557efe1aa9c",
        },
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "SecurityGroups",
            "Value": "launch-wizard-1",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "BreachDuration",
            "Value": "1",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "Statistic",
            "Value": "Average",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "Unit",
            "Value": "Percent",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "EvaluationPeriods",
            "Value": "1",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "Period",
            "Value": "1",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "UpperThreshold",
            "Value": "80",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "UpperBreachScaleIncrement",
            "Value": "1",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "MeasureName",
            "Value": "CPUUtilization",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "LowerThreshold",
            "Value": "50",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "LowerBreachScaleIncrement",
            "Value": "-1",
        },
        {
            "Namespace": "aws:autoscaling:asg",
            "OptionName": "Availability Zones",
            "Value": "Any 2",
        },
        {
            "Namespace": "aws:autoscaling:asg",
            "OptionName": "MaxSize",
            "Value": "3",
        },
        {
            "Namespace": "aws:autoscaling:asg",
            "OptionName": "MinSize",
            "Value": "1",
        },
    ],
)
