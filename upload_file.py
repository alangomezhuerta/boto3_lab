#!/usr/bin/env /home/alan/do/workspace/.venv/bin/python

import boto3

aws_con=boto3.session.Session(profile_name="alan")
s3_con = aws_con.resource('s3')
data = open('test_text.txt','rb')
s3_con.Bucket('s3-bucket-lab-aglab').put_object(Key='test_text.txt', Body=data)
