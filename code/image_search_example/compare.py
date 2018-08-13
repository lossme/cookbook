from image_match.goldberg import ImageSignature
gis = ImageSignature()
a = gis.generate_signature(
    'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg/687px-Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg')
b = gis.generate_signature('https://pixabay.com/static/uploads/photo/2012/11/28/08/56/mona-lisa-67506_960_720.jpg')

# ratio 小于 0.4 则比较相似，数值越小越相似；大于 0.4 则没那么相似，数值越大越不像
ratio = gis.normalized_distance(a, b)
