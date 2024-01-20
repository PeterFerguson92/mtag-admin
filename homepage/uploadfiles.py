import os
import random
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.split(base_name)
    return name, ext

def homepage_banner_upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = "{ext}".format(new_filename=new_filename, ext=ext)
    return "homepage/banner/{final_filename}".format(
        new_filename=new_filename, final_filename=final_filename
    )

def homepage_background_upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = "{ext}".format(new_filename=new_filename, ext=ext)
    return "homepage/background/{final_filename}".format(
        new_filename=new_filename, final_filename=final_filename
    )
    
def homepage_about_us_cover_upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = "{ext}".format(new_filename=new_filename, ext=ext)
    return "homepage/aboutus/{final_filename}".format(
        new_filename=new_filename, final_filename=final_filename
    )

def homepage_video_cover_upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = "{ext}".format(new_filename=new_filename, ext=ext)
    return "homepage/video-cover/{final_filename}".format(
        new_filename=new_filename, final_filename=final_filename
    )

def homepage_leader_cover_upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = "{ext}".format(new_filename=new_filename, ext=ext)
    return "homepage/leader/{final_filename}".format(
        new_filename=new_filename, final_filename=final_filename
    )

def homepage_banner_image_restriction(image):
    image_width, image_height = get_image_dimensions(image)
    if image_width > 203 or image_height > 223:
        raise ValidationError('Image width needs to be less than height: 223 px width: 204 px')
    
def homepage_background_image_restriction(image):
    image_width, image_height = get_image_dimensions(image)
    if image_width > 1921 or image_height > 905:
        raise ValidationError('Image width needs to be less than height: 905 px width: 1921 px')
    
def homepage_about_us_image_restriction(image):
    image_width, image_height = get_image_dimensions(image)
    if image_width > 371 or image_height > 421:
        raise ValidationError('Image width needs to be less than height: 421 px width: 371 px')

def about_us_image_restriction(image):
    image_width, image_height = get_image_dimensions(image)
    if image_width > 271 or image_height > 301:
        raise ValidationError('Image width needs to be less than height: 301 px width: 271 px')

def leader_image_restriction(image):
    image_width, image_height = get_image_dimensions(image)
    if image_width > 467 or image_height > 495:
        raise ValidationError('Image width needs to be less than height: 495 px width: 467 px')

def video_image_restriction(image):
    image_width, image_height = get_image_dimensions(image)
    if image_width > 561 or image_height > 430:
        raise ValidationError('Image width needs to be less than height: 430 px width: 561 px')