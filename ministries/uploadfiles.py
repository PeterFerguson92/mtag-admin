import os
import random
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.split(base_name)
    return name, ext

def ministries_upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = "{ext}".format(new_filename=new_filename, ext=ext)
    return "ministries/{final_filename}".format(
        new_filename=new_filename, final_filename=final_filename
    )
    
def ministry_cover_image_restriction(image):
    image_width, image_height = get_image_dimensions(image)
    if image_width > 421 or image_height > 371:
        raise ValidationError('Image width needs to be less than  height: 371px  width: 421 px')

def ministry_gallery_image_restriction(image):
    image_width, image_height = get_image_dimensions(image)
    if image_width > 370 or image_height > 370:
        raise ValidationError('Image width needs to be less than  height: 370px  width: 370 px')