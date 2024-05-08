import boto3
from botocore.exceptions import NoCredentialsError
from django.core.files.storage import default_storage

def upload_image_to_s3(image_field):
    s3 = boto3.client('s3')
    bucket_name = 'imageforgeheroku'  # Replace with your S3 bucket name

    try:
        # Open the file using the storage backend
        with default_storage.open(image_field.name, 'rb') as file:
            file_content = file.read()

        # Upload the file content to S3
        s3.put_object(Body=file_content, Bucket=bucket_name, Key=image_field.name)
        print(f"Image uploaded to S3 bucket '{bucket_name}' successfully!")
    except FileNotFoundError:
        print("The file was not found!")
    except NoCredentialsError:
        print("Credentials not available!")