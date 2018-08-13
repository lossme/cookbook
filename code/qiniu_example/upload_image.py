from qiniu import Auth, put_file, etag

from config import ACCESS_KEY, SECRET_KEY, BUCKET_NAME, BUCKET_URL


class QiniuTool():

    def __init__(self, access_key, secret_key, bucket_name, bucket_url):
        self.q = Auth(access_key, secret_key)
        self.bucket_name = bucket_name
        self.bucket_url = bucket_url

    def upload_image(self, file, key=None):
        if key is None:
            key = etag(file)
        # 生成上传 Token，可以指定过期时间等
        token = self.q.upload_token(BUCKET_NAME, key, 3600)
        ret, response = put_file(token, key, localfile)
        url = '{}/{}'.format(self.bucket_url, key)
        return url


if __name__ == '__main__':
    qiniu_tool = QiniuTool(access_key=ACCESS_KEY, secret_key=SECRET_KEY,
                           bucket_name=BUCKET_NAME, bucket_url=BUCKET_URL)
    # 要上传文件的本地路径
    localfile = './image/voez.png'
    image_url = qiniu_tool.upload_image(localfile)
    print(image_url)
