from PIL import Image
from numpy import asarray
from numpy.linalg import norm
#convert the image to array
image=Image.open("my_page.jpg")
to_array=asarray(image)
#choose the column from the array 
col_vec=to_array[1,0]
#calculate the L1 norm
L1=norm(col_vec,1)
print("the L1 norm =",L1)
#calculate the L2 norm 
L2=norm(col_vec)
print("the L1 norm =",L2)
