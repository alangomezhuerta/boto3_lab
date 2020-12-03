#!/home/alan/do/workspace/.venv/bin/python

import boto3


connection=boto3.session.Session(profile_name='alan')
iam=connection.resource('iam')
for i in iam.users.all():
     print(i.name)


