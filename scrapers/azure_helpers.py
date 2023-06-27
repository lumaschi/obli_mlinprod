import os

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

#CONNECT_STR = os.environ.get("DefaultEndpointsProtocol=https;AccountName=lucianagerman4638471639;AccountKey=s3ctA9+X+SqyzvUbgzESug9elvK5YbHEKD7Px4RuFu5SG/34BuO5zl+AkbffpYG1q8J+LSbjnpqp+AStfiXepA==;EndpointSuffix=core.windows.net")
CONNECT_STR = "DefaultEndpointsProtocol=https;AccountName=lucianagerman4638471639;AccountKey=s3ctA9+X+SqyzvUbgzESug9elvK5YbHEKD7Px4RuFu5SG/34BuO5zl+AkbffpYG1q8J+LSbjnpqp+AStfiXepA==;EndpointSuffix=core.windows.net"

#CONTAINER_NAME = os.environ.get("azureml-blobstore-712d0730-8ebc-42ee-99e3-a783cdcdbbff")
CONTAINER_NAME = "azureml-blobstore-712d0730-8ebc-42ee-99e3-a783cdcdbbff"

blob_service_client = BlobServiceClient.from_connection_string(CONNECT_STR)
container_client = blob_service_client.get_container_client(container=CONTAINER_NAME)


def upload_blob(path, buf):
    container_client.upload_blob(name=path, data=buf.getvalue())


def append_file_to_blob(path):
    with open(path, mode="rb") as data:
        container_client.upload_blob(name=path, data=data, blob_type="AppendBlob")
