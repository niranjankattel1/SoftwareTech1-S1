from PIL import Image  
# import an image
image1 = Image.open('Assets/insects/1_Gammar 2021_1_2021_06_03-13-19-23-879.PNG') 
image2 = Image.open('Assets/insects/1_Gammar 2021_1_2021_06_03-13-19-23-898.PNG') 
image3 = Image.open('Assets/insects/1_Limniu 2021_1_2021_06_02-13-08-37-958.PNG') 

# flip  
image_transpose = image1.transpose(Image.Transpose.ROTATE_90)
image_transpose = image2.transpose(Image.Transpose.ROTATE_90)
image_transpose = image3.transpose(Image.Transpose.ROTATE_90)
# rotation  
image_rotate = image1.rotate(45, expand = False, center = (0,0)) 
image_rotate = image2.rotate(45, expand = False, center = (0,0)) 
image_rotate = image3.rotate(45, expand = False, center = (0,0)) 
# crop 
image_crop = image1.crop((800,600,1600,1600)) 
image_crop = image2.crop((800,600,1600,1600)) 
image_crop = image3.crop((800,600,1600,1600)) 
# resize  
image_resize = image1.resize((1000,600)) 
image_resize = image2.resize((1000,600)) 
image_resize = image3.resize((1000,600)) 
# applying multiple transformations to an image in a single line of 
#code 
combined_image1 = image1.transpose(Image.Transpose.ROTATE_90).resize((2000,1500)).rotate(10) 
combined_image1.show() 
combined_image2 = image2.transpose(Image.Transpose.ROTATE_90).resize((2000,1500)).rotate(10) 
combined_image2.show() 
combined_image3 = image3.transpose(Image.Transpose.ROTATE_90).resize((2000,1500)).rotate(10) 
combined_image3.show() 