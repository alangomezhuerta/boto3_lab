#!/usr/bin/env /home/alan/do/workspace/.venv/bin/python
aws = boto3.session.Session(profile_name='alan')
sqs = aws.resource
