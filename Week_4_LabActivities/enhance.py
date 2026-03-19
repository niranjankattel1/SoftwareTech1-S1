from PIL import Image, ImageEnhance 
# import an image  
image1 = Image.open('Assets/insects/1_Gammar 2021_1_2021_06_03-13-19-23-879.PNG') 
image2 = Image.open('Assets/insects/1_Gammar 2021_1_2021_06_03-13-19-23-898.PNG') 
image3 = Image.open('Assets/insects/1_Limniu 2021_1_2021_06_02-13-08-37-958.PNG') 
# create an enhancer 
# vibrance_enhancer = ImageEnhance.Color(image) 
contrast_enhancer = ImageEnhance.Contrast(image1) 
brightness_enhancer = ImageEnhance.Brightness(image2) 
sharpness_enhancer = ImageEnhance.Sharpness(image3) 
# apply the enhancer  
enhanced_image1 = contrast_enhancer.enhance(1.5) 
enhanced_image2 = brightness_enhancer.enhance(2) 
enhanced_image3 = sharpness_enhancer.enhance(3) 
# show  
# image1.show() 
# enhanced_image1.show()
# image2.show() 
# enhanced_image2.show()
image3.show() 
enhanced_image3.show()