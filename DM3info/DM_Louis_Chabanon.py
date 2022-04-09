from os import chdir
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

chdir('/Users/louischabanon/dev/info/DM3info')

### Exercice 1

image = mpimg.imread("image1.png")
l = image.shape[0]
h = image.shape[1]
n = image.shape[2]
print("l'image est de dimension:", image.ndim,image.shape)
print("Le nombre de couleurs élémentaires est:", n)


def rotation_algo_iteratif(img):
    new_image = np.zeros((h, l, n),)
    for x in range(l):
        for y in range(h):
            new_image[y][l-1-x]=img[x][y]
    plt.imshow(new_image)
    plt.show()

#rotation_algo_iteratif(image)


def echange_pixels(image, x0, y0, x1, y1):
    p0 = np.copy(image[x0][y0])
    p1 = np.copy(image[x1][y1])
    image[x0][y0] = p1
    image[x1][y1] = p0
    return image


image2 = np.array([[1,0.5,0],[0.5,0,1],[0,1,0.5]])
image2 = echange_pixels(image2,0,0,2,2)
#plt.imshow(image2, cmap="gray", interpolation="nearest")
#plt.show()


def echange_quadrant(image,x0,y0,x1,y1,n):
    for i in range(n):
        for j in range(n):
            image = echange_pixels(image, x0+i, y0+j, x1+i, y1+j)
    return image


image3 = plt.imread("image2_carree.png")
#_image = echange_quadrant(image3,0,0,0,256,256)
#plt.imshow(_image)
#plt.show()


def rotation(image, x0,y0, n):
    m=int(n/2)
    if n == 2:
        echange_quadrant(image, x0, y0,x0,y0+1, 1)
        echange_quadrant(image,x0,y0,x0+1, y0+1, 1)
        echange_quadrant(image,x0,y0,x0+1, y0, 1)
        return image
    else:
        echange_quadrant(image, x0, y0, x0,y0+m, m)
        echange_quadrant(image,x0,y0,x0+m, y0+m, m)
        echange_quadrant(image,x0,y0,x0+m, y0, m)

        rotation(image, x0, y0+m, m)
        rotation(image, x0+m,y0+m, m)
        rotation(image, x0+m,y0, m)
        rotation(image, x0,y0,m)
        return image
    
t=rotation(image3,0,0,512)
plt.imshow(image3)
plt.show()

### Exercice 2

import turtle as tl

tl.speed("fastest")
tl.goto(0,0)

t=30

def arbre(n, l):
    if n < 0:
        return
    else:
        tl.forward(l)
        tl.left(t)
        arbre(n-1,(2/3)*l)
        tl.right(2*t)
        arbre(n-1,(2/3)*l)
        tl.left(t)
        tl.backward(l)

tl.left(90)
arbre(2,100)
tl.done()

### Exercice 3

def carre(n,l):
    tl.right(45)
    for i in range(3):
        tl.forward(l)
        tl.right(90)
        i+=1
    tl.forward(l/2)
    if n > 0:
        carre(n-1,l/np.sqrt(2))
        carre(n-2,l/np.sqrt(2))
    tl.forward(l/2)
    tl.right(45)

