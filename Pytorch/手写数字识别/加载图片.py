import torchvision
from PIL import Image
import torch
image_name="./data/8.png"

# loader使用torchvision中自带的transforms函数

loader = torchvision.transforms.Compose([

torchvision.transforms.ToTensor()])

# 输入图片地址

# 返回tensor变量

def image_loader(image_name):

    image = Image.open(image_name).convert('RGB')

    image = loader(image).unsqueeze(0)

    return image.to(torch.float)

im1=image_loader(image_name)
print(im1)

