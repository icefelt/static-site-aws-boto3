import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Create a bucket
bucket_name = 'my-static-website'
s3.create_bucket(Bucket=bucket_name)

# Set the bucket as a static website
website_configuration = {
    'IndexDocument': 'index.html',
    'ErrorDocument': '404.html'
}
s3.put_bucket_website(Bucket=bucket_name, WebsiteConfiguration=website_configuration)

