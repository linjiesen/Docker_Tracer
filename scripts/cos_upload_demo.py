# -*- coding:utf-8 -*-

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

secret_id = 'AKIDylQ6XiKBFBuT7epJtFOK4whFZQ2NoI9j'
secret_key = 'hAPTIr9WeV6XjfLlCNK0Wnoc9vXu2rRu'
region = 'ap-shanghai'

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)

client = CosS3Client(config)

response = client.upload_file(
    Bucket='7451-18395583854-1617302643-1302119812',
    LocalFilePath='test.jpg',
    Key='picture.jpg',
)
print(response['ETag'])
