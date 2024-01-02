import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Read the image
img = mpimg.imread('images/0d5018e494c388988349f345050d4d54.jpg')

# Display the image
plt.imshow(img)
plt.show()

fig, images = plt.subplots(nrows=1, ncols=2)
img1 = mpimg.imread('images/0d5018e494c388988349f345050d4d54.jpg')
img2 = mpimg.imread('images/1d08fb6ce7ff65739b59e75f603c6559.jpg')
images[0].imshow(img1)
images[1].imshow(img2)
plt.show()

