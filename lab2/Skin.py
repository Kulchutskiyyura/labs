# This Python file uses the following encoding: utf-8
from PIL import Image
class Skin:
    def __init__(self,image_path,name):
        self.__image=Image.open(image_path)
        self.name=name
    def get_image(self):
        return self.__image
    def set_image(self,image_path):
        self.__image=Image.open(image_path)
    image=property(get_image,set_image)


