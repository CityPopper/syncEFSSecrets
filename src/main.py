#!/usr/bin/env python3
import os
import awscli


sync_command = f'aws s3 sync --delete s3://{os.environ["S3SECRETBUCKETNAME"]} /mnt/secrets'
s3 = sh.bash.bake("aws s3")
s3.put("ls")


# def lambda_handler(event, context):
#     os.system(sync_command)
#     return os.listdir('/mnt/secrets')
