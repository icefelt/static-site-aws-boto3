# static-site-aws-boto3
This python code uses the boto3 library to create a static site using an AWS S3 bucket. 

This code will 
1. create an S3 bucket named Icefelt-Test-Bucket
2. configure it as a static website
3. upload the static website files to the bucket
4. configure the bucket to be publicly accessible
5. print the bucket's website endpoint

## Installation
1. Clone the source code to a local directory directory
2. Create a Python virtual environment and activate it

```sh
$ git clone git@github.com:icefelt/static-site-aws-boto3.git && cd static-site-aws-boto3/
$ python -m venv ./venv && source venv/bin/activate
(venv) $
```

2. Install dependencies
```sh
(venv) $ python -m pip install -r requirements.txt
```

## Usage

Create the bucket 
```sh
$ python static-website.py
```

Delete the bucket using AWS CLI
```sh
$ aws s3 rb s3://icefelt-test-bucket
```

## Release History
- 0.2.0

## About the Author
Scott Eissfeldt - email: scott@eissfeldt.com
