import boto3, json

aws_resource = boto3.client('s3')
bucket_policy = {
    "Version": "2012-10-17",
    "Id": "PolicyForCloudFrontPrivateContent",
    "Statement": [
        {
            "Sid": " Grant a CloudFront Origin Identity access to support private content",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity E11NSLRICVW1J7"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::9j6lnpa-fei0ikn/*"
        }
    ]
}
aws_resource.put_bucket_policy(Bucket='9j6lnpa-fei0ikn', Policy=bucket_policy)
bucket_policy = json.dumps(bucket_policy)

