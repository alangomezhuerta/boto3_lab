#!/usr/bin/env /home/alan/do/workspace/.venv/bin/python

import boto3

aws_mag_con=boto3.session.Session(profile_name="alan")
s3 = aws_mag_con.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

