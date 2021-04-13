# -*- coding:utf-8 -*-

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

secret_id = 'AKIDylQ6XiKBFBuT7epJtFOK4whFZQ2NoI9j'
secret_key = 'hAPTIr9WeV6XjfLlCNK0Wnoc9vXu2rRu'
region = 'ap-shanghai'

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)

client = CosS3Client(config)

# response = client.delete_object(
#     Bucket='alroy-1302119812',
#     Key='picture.jpg',
# )
objects = {
    "Quiet": "true",
    "Object": [
        {
            "Key": "file_name1"
        },
        {
            "Key": "file_name2"
        }
    ]
}


client.delete_objects(
    Bucket='alroy-1302119812',
    Delete=objects,
)
