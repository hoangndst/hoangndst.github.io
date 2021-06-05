import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn import linear_model

def cost(x):
    m = A.shape[0]
    return 0.5/m * np.linalg.norm(A.dot(x) - b, 2)**2

def grad(x):
    m = A.shape[0]
    return 1/m * A.T.dot(A.dot(x) - b)

def numerical_grad(x):
    eps = 1e-4
    g = np.zeros_like(x)
    for i in range(len(x)):
        x1 = x.copy()
        x2 = x.copy()
        x1[i] += eps
        x2[i] -= eps
        g[i] = (cost(x1) - cost(x2))/(2*eps)
    return g

def check_grad(x):
    x = np.random.rand(x.shape[0], x.shape[1])
    grad1 = grad(x)
    grad2 = numerical_grad(x)
    if np.linalg.norm(grad1 - grad2) > 1e-5:
        print("Check grad function!")
    return

def gradient_descent(x_init, learning_rate, iteration):
    x_list = [x_init]
    for i in range(iteration):
        x_new = x_list[-1] - learning_rate*grad(x_list[-1])
        if np.linalg.norm(grad(x_new))/len(x_init) < 1e-3:
            break
        x_list.append(x_new)
    return x_list

A = [2,9,7,9,11,16,25,23,22,29,29,35,37,40,46]
A = np.array([A]).T # Ox
b = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
b = np.array([b]).T # Oy
ax = plt.axes(xlim=(-10,60), ylim=(0, 20))

plt.plot(A, b, 'ro')

lr = linear_model.LinearRegression()
lr.fit(A,b)
x0_gd = np.linspace(1,46,2)
y0_sklearn = lr.intercept_[0] + lr.coef_[0][0]*x0_gd
plt.plot(x0_gd, y0_sklearn)

# Add one to A
ones = np.ones((A.shape[0], 1), dtype=np.int8)
A = np.concatenate((ones, A), axis=1)

# Random initial line
x_init = np.array([[1.], [2.]]) # (a, b)
y0_init = x_init[0][0] + x_init[1][0]*x0_gd # y = a + bx
plt.plot(x0_gd, y0_init, color="black")

check_grad(x_init)

iteration = 1000
learning_rate = 0.0001
x_list = gradient_descent(x_init, learning_rate, iteration)
for i in range(len(x_list)):
    y0_gd = x_list[i][0] + x_list[i][1]*x0_gd
    plt.plot(x0_gd, y0_gd, color="black")
plt.show()
print(len(x_list))
# Plot cost
cost_list = []
iteration_list = []
for i in range(len(x_list)):
    iteration_list.append(i+1)
    cost_list.append(cost(x_list[i]))
plt.plot(iteration_list, cost_list)

plt.show()

# print(lr.coef_)
# print(lr.intercept_)
