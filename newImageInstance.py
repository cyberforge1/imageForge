import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = "ll_project.settings"
django.setup()


from imageGeneration.models import Image
from saveImage import local_image_path

from django.utils import timezone
from imageGeneration.models import Image

from grammar import prompt_instance

import boto3
from botocore.exceptions import NoCredentialsError


imageModel = Image()

imageModel.text_field = prompt_instance
imageModel.datetime_field = timezone.now()
imageModel.image_field = local_image_path
imageModel.local_url = f"http://127.0.0.1:8000/media/{imageModel.image_field}"


imageModel.save()


print("Text Field:", imageModel.text_field)
print("Datetime Field:", imageModel.datetime_field)
print("Image Field:", imageModel.image_field)
print("Local Image URL Field:", imageModel.local_url)
print("Specific Image Instance ID:", imageModel.id)


image_model = Image.objects.latest("datetime_field")
s3_key = f"media/{image_model.image_field.name}"
bucket_name = "imageforgeheroku"
print("This is the s3 key", s3_key)


def upload_image_to_s3(image_file):
    s3 = boto3.client("s3")
    bucket_name = "imageforgeheroku"
    s3_key = f"media/{image_model.image_field.name}"

    try:
        s3.upload_file(s3_key, bucket_name, s3_key)
        print(f"Image uploaded to S3 bucket '{bucket_name}' successfully!")
    except FileNotFoundError:
        print("The file was not found!")
    except NoCredentialsError:
        print("Credentials not available!!")


upload_image_to_s3(s3_key)
