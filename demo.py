# TSD will automatically load the network and weight
import TSD as tsd

# read image
image = tsd.get_img('1.jpg')

# get result for image
result = tsd.get_result(image)

print result
