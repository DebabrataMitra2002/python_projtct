import pandas as pd

def gradient_descent(x, y):
    m_curr = b_curr = 0 
    iterator = 1000
    L = 0.0001
    n = len(x)
    for i in range(iterator):
        y_predict = m_curr * x + b_curr
        cost = (1/n) * sum(val**2 for val in (y - y_predict))
        md = -(2/n) * sum(x * (y - y_predict))  # Partial derivative of cost function w.r.t m
        bd = -(2/n) * sum(y - y_predict)       # Partial derivative of cost function w.r.t b
        m_curr = m_curr - L * md   # m = m - L * md
        b_curr = b_curr - L * bd   # b = b - L * bd
        print("m {}, b {}, cost {}, iteration {}".format(m_curr, b_curr, cost, i))


df = pd.read_csv('test_scores.csv')
x = df['math'].values  # Convert 'math' column to numpy array
y = df['cs'].values    # Convert 'cs' column to numpy array

gradient_descent(x, y)
