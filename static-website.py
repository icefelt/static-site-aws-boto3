import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Create a bucket
bucket_name = 'Icefelt-Test-Bucket'
s3.create_bucket(Bucket=bucket_name,
    CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})

# Set the bucket as a static website
website_configuration = {
    'IndexDocument': 'index.html',
    'ErrorDocument': '404.html'
}
s3.put_bucket_website(Bucket=bucket_name, WebsiteConfiguration=website_configuration)

# Upload the static website files to the bucket
for file_name in ['index.html', '404.html']:
    with open(file_name, 'rb') as f:
        s3.upload_fileobj(f, bucket_name, file_name)

# Configure the bucket to be publicly accessible
s3.put_bucket_policy(
    Bucket=bucket_name,
    Policy=json.dumps({
        'Version': '2012-10-17',
        'Statement': [{
            'Sid': 'PublicReadGetObject',
            'Effect': 'Allow',
            'Principal': '*',
            'Action': 's3:GetObject',
            'Resource': 'arn:aws:s3:::Icefelt-Test-Bucket/*'
        }]
    })
)

# Print the bucket's website endpoint
print(s3.get_bucket_website(Bucket=bucket_name)['WebsiteConfiguration']['Endpoint'])