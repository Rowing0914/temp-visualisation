import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("dog.jpg") # load an image
zi = [766j, 512+766j, 256+192j]
wi = [738j, 512+496j, 256+173j]
r = np.ones((600,700,3),dtype=np.uint8) * 255 # empty-white image
for i in range(img.shape[1]):
    for j in range(img.shape[0]):
        z = complex(i,j)
        qf = ((wi[0] * (-wi[1] * (zi[0]-zi[1]) * (z-zi[2]) + wi[2] * (z-zi[1]) * (zi[0]-zi[2])) - wi[1]*wi[2]*(z-zi[0]) * (zi[1]-zi[2])))
        qs = (wi[2]*(zi[0]-zi[1])*(z-zi[2])-wi[1]*(z-zi[1])*(zi[0]-zi[2])+wi[0]*(z-zi[0])*(zi[1]-zi[2]))
        w = qf/qs
        r[int(np.imag(w)),int(np.real(w)),:] = img[j,i,:]

plt.subplot(121)
plt.imshow(img,origin='lower',aspect='auto')
plt.subplot(122)
plt.imshow(r,origin='lower',aspect='auto')
plt.show()