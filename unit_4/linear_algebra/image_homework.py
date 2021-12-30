from PIL import Image
from numpy import asarray
#open an image and convert it to array 
image=Image.open("my_page.jpg")
to_array=asarray(image)
print(to_array)
print(to_array.shape)
#print the matrix type 
print(to_array.dtype)
#transpose 
transpose=to_array.T
print(transpose)
