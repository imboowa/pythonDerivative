import matplotlib.pyplot as plt

# This is a list of any point on the curve that our slope is found
x = [0.66666667,1,2,3,4,5,6,7,8,9]

# This is the function that makes the curved line
def f(x):
    return (3 * (x ** 2) - (4 * x)) + 5


# This calculates the derivative
def d(func, x, h=1e-8):
    goal = {}
    for i in x:
        answer = (func(i + h) - func(i)) / h
        goal.update({i:answer})
    return goal

# call the derivative and store its data in a dictionary
deal = d(f, x).items()

# print the derivative, key, value pairs like
# number in list(1), derivative(1.9999)
for key, value in deal:
    print(f"{key:<15.8f}: {value:.8f}")

gi_x = []
for i in x:
    gi_x.append(f(i))



plt.plot(x, d(f, x).values(), marker='.', linestyle='-',color='y')
plt.plot(x, gi_x, marker='.', linestyle='-',color='b')
#plt.legend()
plt.show()