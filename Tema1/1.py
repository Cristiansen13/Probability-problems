import numpy as np

# Varianta 1
"""
r = np.random.random()*10
L = 3/np.sqrt(3)*r
cnt = 0
for i in range(10000):
    alpha = np.random.random() * 2 * np.pi
    Ax = r * np.sin(alpha)
    Ay = r * np.cos(alpha)
    alpha = np.random.random() * 2 * np.pi
    Bx = r * np.sin(alpha)
    By = r * np.cos(alpha)
    dist = np.sqrt((Ax - Bx)**2 + (Ay - By)**2)
    if dist > L:
        cnt += 1
print(cnt/10000)
# sau
"""
print("Varianta 1")
r = np.random.random()*10
L = 3/np.sqrt(3)*r
cnt = 0
for i in range(10000):
    alpha1 = np.random.random() * 2 * np.pi
    alpha2 = np.random.random() * 2 * np.pi
    absolut = np.abs(alpha2-alpha1)
    dist = 2 * r * np.sin(absolut/2)
    if dist > L:
        cnt += 1
print(cnt/10000)
#Varianta 2
print("Varianta 2")
r = np.random.random()*10
L = 3/np.sqrt(3)*r
cnt = 0
for i in range(10000):
    r2 = np.sqrt(np.random.random()) * r
    dist = 2 * np.sqrt(r**2 - r2 **2)
    if dist > L:
        cnt += 1
print(cnt/10000)

#Varianta 3
print("Varianta 3")
r = np.random.random()*10
L = 3/np.sqrt(3)*r
cnt = 0
for i in range(10000):
    r2 = np.random.random() * r
    dist = 2 * np.sqrt(r**2 - r2 **2)
    if dist > L:
        cnt += 1
print(cnt/10000)
