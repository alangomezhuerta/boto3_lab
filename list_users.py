#!/usr/bin/env /home/alan/do/workspace/.venv/bin/python

import boto3

aws_mag_con=boto3.session.Session(profile_name="alan")
iam_con=aws_mag_con.resource('iam')
for each_user in iam_con.users.all():
    print(each_user.name)


