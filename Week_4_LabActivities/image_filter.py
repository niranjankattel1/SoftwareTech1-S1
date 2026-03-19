from PIL import Image, ImageFilter 
# create an image  
image = Image.open('Assets/insects/1_Limniu 2021_1_2021_06_02-13-08-37-958.PNG') 
# apply a basic filter 
# image_blur = image.filter(ImageFilter.BLUR) 
image_contour = image.filter(ImageFilter.CONTOUR) 
image_emboss = image.filter(ImageFilter.EMBOSS) 
# image_edge = image.filter(ImageFilter.FIND_EDGES) 
# apply advanced filters 
image_boxblur = image.filter(ImageFilter.BoxBlur(radius = 20)) 
image_gaussianblur = image.filter(ImageFilter.GaussianBlur(radius = 20)) 
# image_unsharp = image.filter(ImageFilter.UnsharpMask(radius = 20)) 
image_emboss.show() 
image_contour.show()