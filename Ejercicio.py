import numpy as np

print ('------------------------- ESCALAR --------------------------')
e = 5
print(e)

print ('------------------------- VECTOR --------------------------')
v = np.array([1,2,3])
print(v)

print ('------------------------- MATRIZ --------------------------')
m = np.array([[3,2,4],[-6,7,1]])
print(m)

print ('------------------------- TIPOS DE DATOS DE MATRICES --------------------------')

print ('Tipo Escarlar')
print (type(e))

print ('Tipo Vector')
print (type(v))

print ('Tipo Matriz')
print (type(m))

print ('------------------------- DIMESIÓN DE MATRICES --------------------------')
print(m.shape)

print ('------------------------- REESCRIPCIÓN DE MATRICES --------------------------')
print (v.reshape(1,3))
print (v.reshape(3,1))

print ('------------------------- SUMA DE MATRICES --------------------------')
m1 = np.array([[2,3,5],[7,8,9]])
m2 = np.array([[1,1,1],[1,1,1]])
print(m1 + m2)

print ('------------------------- RESTA DE MATRICES --------------------------')
print(m1 - m2)

print ('------------------------- SUMA DE UN ESCALAR Y UNA MATRIZ --------------------------')
m3 = np.array([[9,8,7],[1,3,-5]])
print(m3 + 1)

print ('------------------------- SUMA DE UN ESCALAR Y UNA MATRIZ --------------------------')
print ('Matriz Original')
print (m3)
print ('Transpuesta')
print (m3.T)

print ('------------------------- TRANSPUESTA DE UN VECTOR --------------------------')
print ('Vector Original')
print (v)
print ('Transpuesta')
print ((v.reshape(1,3)).T)