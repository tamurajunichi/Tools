import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

n = np.linspace(1,10,1000)
fft = np.log2(n)
dft = n**2

c = ["red", "blue"]
l = ["fft", "dft"]

ax.set_xlabel("N")
ax.set_ylabel("Operations")
ax.set_title(r'FFT and DFT')
ax.grid()

for i in range(number_data):
    ax.plot(n,y[i], color=c[i],label=l[i])
ax.plot(n, fft, color=c1, label=l1)
ax.plot(n, dft, color=c2, label=l2)
ax.legend(loc=0)    # 凡例
fig.tight_layout()  # レイアウトの設定
plt.savefig('hoge.png')


