import matplotlib.pyplot as plt
import numpy as np
# panda -- prendre des grandes quantitées de données

#graph 1
x = [0.477, 0.556, 0.581, 0.593, 0.601, 0.607, 0.612, 0.627]
y = [0.067, 0.156, 0.392, 0.629, 0.860, 1.110, 1.350, 2.340]

p = np.polyfit(x, np.log(y), 1)
a = np.exp(p[1])
b = p[0]
x_fitted = np.linspace(np.min(x), np.max(x), 100)
y_fitted = a * np.exp(b * x_fitted)
p = np.polyfit(x, np.log(y), 1, w=np.sqrt(y))
a = np.exp(p[1])
b = p[0]
x_fitted_weighted = np.linspace(np.min(x), np.max(x), 100)
y_fitted_weighted = a * np.exp(b * x_fitted_weighted)

ax = plt.axes()
ax.scatter(x, y)
ax.axvline(x=0.3, color='red', linestyle='--')
ax.plot(x_fitted_weighted, y_fitted_weighted, 'k--',label=f'y = {a:.2E} * e^({b:.3f}x)')

plt.xlabel('Vbe [V]')
plt.ylabel('Ic [mA]')
plt.grid()
plt.legend()
plt.savefig("mesure 1.pdf")
# plt.show()


# #graph 2
# x_values_1 = [4.46, 9.01, 0.544, 0.15, 0.109, 0.087, 0.067, 0.057, 0.051, 0.045]
# y_values_1 = [4.53, 4.90, 4.34, 4.00, 3.20, 2.40, 1.58, 1.18, 0.99, 0.78]

# x_values_2 = [5.734, 8.72, 13.68, 18.65, 23.58, 3.72, 2.71, 1.73, 0.734, 0.496, 0.255, 0.138, 0.106, 0.084, 0.065]
# y_values_2 = [1.034, 1.056, 1.088, 1.12, 1.16, 1.046, 1.039, 1.031, 1.02, 1.014, 1.008, 0.905, 0.726, 0.53, 0.349]

# x_values_3 = [1.83, 4.67, 6.5, 9.264, 13.95, 18.64, 23]
# y_values_3 = [4.23, 4.38, 4.51, 4.7, 4.93, 5.19, 5.7]

# x_values_4 = [16.02, 11.11, 6.27, 3.38, 0.54]
# y_values_4 = [3.25, 3.21, 3.10, 2.98, 2.84]

# x_l1 = np.linspace(0.2, 25, 100) 
# x_l4 = np.linspace(0.2, 20, 100) 

# #y_l1 = 0.0666 * x_l1 + 4.2791  
# y_l2 = 0.0069 * x_l1 + 0.9941  
# y_l3 = 0.0656 * x_l1 + 4.0757  
# y_l4 = 0.0209 * x_l1 + 2.9432 

# #plt.plot(x_l1, y_l1,c='b')
# plt.plot(x_l1, y_l2,c='c')
# plt.plot(x_l1, y_l3,c='orange')
# plt.plot(x_l4, y_l4,c='g')


# plt.scatter(x_values_1, y_values_1, c='b', label='mesure 1')
# plt.scatter(x_values_2, y_values_2, c='c', label='mesure 2')
# plt.scatter(x_values_3, y_values_3, c='orange', label='mesure 3')
# plt.scatter(x_values_4, y_values_4, c='g', label='mesure 4')

# plt.axvline(x=0.3, color='r',label='Vce sat.')

# plt.xlabel('Vce [v]')
# plt.ylabel('Ic [mA]')
# plt.legend()
# plt.grid()
# # plt.savefig("logos/mesure 2.pdf")
# # plt.show()

# #graph 3
# x_l = np.linspace(-150,25, 100) 
# #y_l1 = 0.0813 * x_l + 4.1673  
# y_l2 = 0.0069 * x_l + 0.9941  
# y_l3 = 0.0656 * x_l + 4.0757  
# y_l4 = 0.0209 * x_l + 2.9432 
# plt.axvline(x = 0,color='black')
# plt.axhline(y = 0,color='black')
# #plt.plot(x_l, y_l1,c='b',label='mesure 1: y = x +')
# plt.plot(x_l, y_l2,c='c',label='mesure 2: y = 0.0069x + 0.9941')
# plt.plot(x_l, y_l3,c='orange',label='mesure 3: y = 0.0656x + 4.0757')
# plt.plot(x_l, y_l4,c='g',label='mesure 4: y = 0.0209x + 2.9432')
# plt.xlabel('Vce [v]')
# plt.ylabel('Ic [mA]')
# plt.grid()
# plt.legend()
# # plt.savefig("logos/Vearly.pdf")
# # plt.show()

# #calcul du point d'intersection entre les 2 droites

# class Line:
#   def _init_(self,slope,const):
#     self.m=slope
#     self.c=const
# def findSolution(L1,L2):
#   x=(L1.c-L2.c)/(L2.m-L1.m)
#   y=L1.m*x+L1.c
#   return (x,y)
# L1=Line(0.0069,0.9941 ) #Equation of line y=3x+5
# L2=Line(0.0209,2.9432) #Equation of line y=2x+3
# sol=findSolution(L1,L2)
# print(sol)# point d'intersection des 2 droites
