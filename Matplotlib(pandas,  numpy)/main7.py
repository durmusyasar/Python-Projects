import matplotlib.pyplot as plt

fig = plt.figure("Histogram")
ax = fig.add_subplot(1, 1, 1)
ax.hist([21,12,23,35,45,60,33,22,56,34,28,40,41], bins = 7, facecolor = 'g', normed = False)

plt.title("Distribution")
plt.xlabel("Range")
plt.ylabel("Amount")
plt.show()

fig2 = plt.figure("Box-plot")
ax1 = fig2.add_subplot(1, 1, 1)
ax1.hist([21,12,23,35,45,60,33,22,56,34,28,40,41], bins = 7, facecolor = 'g', normed = False)
plt.show()

fig3 = plt.figure("Bar")
ax2 = fig3.add_subplot(1, 1, 1)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('Bars')
ax2.bar([0,1,2,3], [5,10,15,5], [0.5,1,1.3,1], color=['b', 'r'])
plt.show()

fig4 = plt.figure("Line")
ax3 = fig4.add_subplot(1, 1, 1)
ax3.set_xlim([-2, 10])
ax3.set_ylim([0, 6])
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_title('Lines')
ax3.bar([-1,2,4,7,8], [5,2,3,4,3],  color='r')
plt.show()

data = {
    'Player': ['Wade', 'James', 'Kobe', 'Curry'],
    'First': [10,10,8,12],
    'Second': [12,8,13,8],
    'Third': [15,12,8,8],
    'Fourth': [18,20,15,8]
}
fig5 = plt.figure("Stacked bar")
ax4 = fig5.add_subplot(1,1,1)
bar_width = 0.5
bars = [i+1 for i in range(len(data['First']))]
ticks = [i + (bar_width/2) for i in bars]
ax4.bar(
    bars, data['First'], width = bar_width,
    label = 'First Quarter', color = '#FFD600'
)
ax4.bar(
    bars, data['Second'], width = bar_width, bottom = data['First'],
    label = 'Second Quarter', color = '#FFD600'
)
ax4.bar(
    bars, data['Third'], width = bar_width,
    bottom = [i+j for i, j in zip(data['First'], data['Second'])],
    label = 'Third Quarter', color = '#FF9200'
)
ax4.bar(
    bars, data['Fourth'], width = bar_width,
    bottom = [i+j+k for i, j, k in zip(data['First'], data['Second'], data['Third'])],
    label = 'Fourth Quarter', color = 'r'
)
plt.xticks(ticks, data['Player'])
ax4.set_xlabel("Total")
ax4.set_ylabel("Player")
plt.legend(loc = "upper right")
plt.xlim([min(ticks)-bar_width, max(ticks)+bar_width])
plt.show()

