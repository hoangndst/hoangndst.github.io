import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib.animation import writers
def cost(x):
    m = A.shape[0]
    return 0.5/m * np.linalg.norm(A.dot(x) - b)**2

def grad(x):
    m = A.shape[0]
    return 1/m * A.T.dot(A.dot(x) - b) # return f'(x):[a, b, c].T

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
    g1 = grad(x)
    g2 = numerical_grad(x)
    if np.linalg.norm(g1 - g2) > 1e-5:
        print("Check grad function")
    return

def gradient_descent(x_random, learning_rate, iteration):
    x_list = [x_random]
    for i in range(iteration):
        x_new = x_list[-1] - learning_rate*grad(x_list[-1])
        if np.linalg.norm(grad(x_new))/len(x_gd) < 0.03:
            break
        x_list.append(x_new)
    return x_list

b = [2,5,7,9,11,16,19,23,22,29,29,35,37,40,46,42,39,31,30,28,20,15,10,6]
b = np.array([b]).T
A = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
x_gd = np.linspace(1,46,10000)
# x_random = np.random.rand(3, 1)
# print(x_random)
x_random = np.array([[ -2.1],
       [ 10.1],
       [-2.1]])
fig1 = plt.figure("GD for Linear Regression")
ax = plt.axes(xlim=(-5,30), ylim=(-5, 50))

A = np.array([A]).T
plt.plot(A,b, 'ro')
# add ones and col 3 to A
ones = np.ones((A.shape[0], 1), dtype=np.int8)
col_3 = A*A
A = np.concatenate((ones, A, col_3), axis=1)

# Linear Regression
x_lg = np.linalg.inv(A.T.dot(A)).dot(A.T.dot(b))
y_lg = x_lg[0][0] + x_lg[1][0]*x_gd + x_lg[2][0]*x_gd*x_gd
plt.plot(x_gd, y_lg, color="green")

# Plot random
y_random = x_random[0][0]  + x_random[1][0]*x_gd + x_random[2][0]*x_gd*x_gd
plt.plot(x_gd, y_random, color="black")
# check grad
check_grad(x_random)

iteration = 70
learning_rate = 0.000001

x_list = gradient_descent(x_random, learning_rate, iteration)
for i in range(len(x_list)):
    y0_gd = x_list[i][0] + x_list[i][1]*x_gd + x_list[i][2]*x_gd*x_gd
    plt.plot(x_gd, y0_gd, color="black", alpha=0.3)

# Draw animation
line , = ax.plot([],[], color="blue")
def update(i):
    y0_gd = x_list[i][0][0] + x_list[i][1][0]*x_gd + x_list[i][2][0]*x_gd*x_gd
    line.set_data(x_gd, y0_gd)
    return line,

iters = np.arange(0,len(x_list), 1)
# Legend for plot
plt.xlabel('Iteration: {}   Learning rate: {}  |Grad| = {}'.format(len(x_list) - 1, learning_rate, np.linalg.norm(grad(x_list[-1]))/len(x_gd)))
plt.legend(('Data', 'Solution by Linear Regression', 'Initial Line For GD'), loc=(0.48, 0.01))
plt.title("Gradient Descent")
line_ani = animation.FuncAnimation(fig1, update, iters, interval=50, blit=True)

# Save animation to gif file
# Writer = writers['ffmpeg']
# writer = Writer(fps=15, metadata={'artist': 'Me'}, bitrate=1800)

# line_ani.save('GA Animation.gif', writer)

# fig2 = plt.figure()
# print(len(x_list))
# cost_list = []
# iteration_list = []
# plt.xlabel("Iteration")
# plt.ylabel("Cost Value")
# for i in range(len(x_list)):
#     iteration_list.append(i+1)
#     cost_list.append(cost(x_list[i]))
# plt.plot(iteration_list, cost_list)

plt.show()