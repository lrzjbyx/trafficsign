# ChsEm12J-uOAT4fbAAXLVEFg5xI085.jpg
import io
import re
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# text = "full/ChsEm12J-uOAT4fbAAXLVEFg5xI085.jpg"

# text = re.sub(r"full/[\d\w-]+","123",text)
# print(text)

# 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl1.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl2.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl3.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl4.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl5.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl6.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl7.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl8.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl9.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl10.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl11.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl12.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl13.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl14.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl15.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl16.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl17.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl18.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl19.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl20.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl21.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl22.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl23.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl24.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl25.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl26.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl27.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl28.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl29.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl30.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl31.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl32.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl33.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl34.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl35.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl36.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl37.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl38.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl39.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl40.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl41.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl42.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl43.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl44.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl45.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl46.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl47.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl48.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl49.jpg',
#                 'https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl50.jpg
#                   https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/2/jg73.jpg

# text ='https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl12823.jpg'
# path = "full/ChsEm12J-uOAT4fbAAXLVEFg5xI085.jpg"
# file_name = re.search(r'\w{2}(\d+)\.jpg',text).group(1)


# image_name = re.sub(r"full/[\d\w-]+",file_name,path)
# print(image_name)


# text = "禁止挂车、半挂车驶入"
# text = re.sub(r'[、\.,，!！]+',"",text)
# print(text)

