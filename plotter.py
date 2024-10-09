import cv2
import numpy as np 
import matplotlib.pyplot as plt
 
image = cv2.imread('./images_16/1.png')
img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # need alpha chanel


size = 16
shape = (size, size, size, 3)
model = np.empty(shape)

for i in range(size):
    model[i] = img


image = cv2.imread('./images_16/2.png')
img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # need alpha chanel

# switch xyz
for x in range(size):
    for y in range(size):
        for z in range(size):
            if np.equal(img[x][y][z], np.array([0, 0, 0])).all():
                model[x][y][z] = np.array([0, 0, 0])



#Ploting
fig = plt.figure(figsize=(4,4))

ax = fig.add_subplot(111, projection='3d')

for x in range(size):
    for y in range(size):
        for z in range(size):
            if np.not_equal(model[x][y][z], np.array([0, 0, 0])).all():
                ax.scatter(x, y, z, color=model[x][y][z]/255.0)

plt.show()
