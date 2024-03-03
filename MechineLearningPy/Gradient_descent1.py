import numpy as np

def gradient_descent(x, y):
    m_curr = b_curr = 0
    iterations = 10000   # Number of iterations
    n = len(x)
    l = 0.0001           # Learning rate
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr   # y = mx + b equation
        cost = (1/n) * sum(val**2 for val in (y - y_predicted))  # Cost function
        md = -(2/n) * sum(x * (y - y_predicted))  # Partial derivative of cost function w.r.t m
        bd = -(2/n) * sum(y - y_predicted)       # Partial derivative of cost function w.r.t b
        m_curr = m_curr - l * md   # m = m - L * md
        b_curr = b_curr - l * bd   # b = b - L * bd
        print("m {}, b {}, cost {}, iteration {}".format(m_curr, b_curr, cost, i))    

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])
gradient_descent(x, y)