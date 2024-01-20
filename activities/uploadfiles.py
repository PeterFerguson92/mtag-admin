import os
import random
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.split(base_name)
    return name, ext

def event_upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = "{ext}".format(new_filename=new_filename, ext=ext)
    return "event/{final_filename}".format(
        new_filename=new_filename, final_filename=final_filename
    )
    
def event_image_restriction(image):
    image_width, image_height = get_image_dimensions(image)
    if image_width > 771 or image_height > 461:
        raise ValidationError('Image width needs to be less than  height: 461px  width: 771 px')