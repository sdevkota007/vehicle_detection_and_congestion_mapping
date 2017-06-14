from statistics import mean
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

data_df = pd.DataFrame.from_csv("out.csv")

data_df = data_df[:50]

xs = np.array(data_df["Id"].values)
# xs = np.array([1,2,3,4,5], dtype=np.float64)
ys = np.array(data_df["10:00-10:15"].values)
# ys = np.array([125,142,139,127,153], dtype=np.float64)

def best_fit_slope_and_intercept(xs,ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)*mean(xs)) - mean(xs*xs)))

    b = mean(ys) - m*mean(xs)

    return m, b

m, b = best_fit_slope_and_intercept(xs,ys)

print(m,b)

regression_line = [(m*x)+b for x in xs]

regression_line = []
for x in xs:
    regression_line.append((m*x)+b)

plt.scatter(xs,ys,color='#003F72')
plt.plot(xs, regression_line)
plt.show()

predict_x = 53

predict_y = (m*predict_x)+b
print(predict_y)

predict_x = 54
predict_y = (m*predict_x)+b
print (predict_y)

plt.scatter(xs,ys,color='#003F72',label='data')
plt.plot(xs, regression_line, label='regression line')
plt.legend(loc=4)
plt.show()