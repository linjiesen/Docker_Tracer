# -*-coding:utf-8 -*-

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

secret_id = 'AKIDylQ6XiKBFBuT7epJtFOK4whFZQ2NoI9j'
secret_key = 'hAPTIr9WeV6XjfLlCNK0Wnoc9vXu2rRu'
region = 'ap-shanghai'

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)

client = CosS3Client(config)

response = client.create_bucket(
    Bucket='alroy-1302119812',
    ACL="publick-read"  # private / public-read / public-read-write
)
