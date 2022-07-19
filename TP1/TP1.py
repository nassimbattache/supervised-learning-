import numpy as np
import matplotlib.pyplot as plt
plt.ion() # mode interactif facilite utilisation figures multiples
# fixer la graine aléatoire de numpy permet d'obtenir systématiquement les mêmes résultats
np.random.seed(150)
# définir matrices de rotation et de dilatation
rot = np.array([[0.94, -0.34], [0.34, 0.94]])
sca = np.array([[3.4, 0], [0, 2]])
# générer données classe 1
c1d = (np.random.randn(100,2)).dot(sca).dot(rot)
# générer données classe 2
c2d1 = np.random.randn(25,2)+[-10, 2]
c2d2 = np.random.randn(25,2)+[-7, -2]
c2d3 = np.random.randn(25,2)+[-2, -6]
c2d4 = np.random.randn(25,2)+[5, -7]
data = np.concatenate((c1d, c2d1, c2d2, c2d3, c2d4))
# générer étiquettes de classe 
l1c= np.ones(100, dtype=int) 
l2c =np.zeros(100, dtype=int) 
labels =np.concatenate((l1c, l2c))
# les échantillons du premier groupe sont en rouge 'r', ceux du deuxième groupe en vert (*green*) 'g'
cmp = np.array(['r','g'])
plt.figure()
plt.scatter(data[:,0],data[:,1], c=cmp[labels], s=50, edgecolors='none')