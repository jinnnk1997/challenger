
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Path to the image of the hugging rabbit
img_path = 'hug_rabbit_image.png'

# Load and display the image
img = mpimg.imread(img_path)
imgplot = plt.imshow(img)
plt.axis('off')  # Hide axes
plt.show()
