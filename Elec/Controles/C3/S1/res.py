import os
import numpy as np
import statistics as st
import matplotlib.pyplot as plt

dgmap = plt.cm.get_cmap('viridis')

list = [
    1.00,
    10.00,
    13.00,
    5.50,
    0.50,
    7.00,
    10.00,
    1.50,
    7.50,
    6.00,
    7.00,
    7.00,
    15.50,
    10.00,
    8.00,
    8.00,
    10.00,
    3.75,
    11.00,
    5.50,
    8.50,
    1.50,
    10.00,
    13.00,
    5.50,
    5.00,
    4.00,
    12.00,
    5.00]

moy = st.mean(list)
# print('Moyenne = ', moy)

med = st.median(list)
# print('Mediane = ', med)

std = st.stdev(list, moy)
# print('Ecart-type = ', std)

fig = plt.figure(figsize=[8, 3])
ax = fig.add_axes([0.1, 0.12, 0.8, 0.8])

_, X, patches = ax.hist(list, bins=[i for i in range(21)],
                        histtype='step',
                        color='k', alpha=.5)

ax.axvspan(np.min(list),
           5.0,
           color=dgmap(0),
           alpha=.5,
           clip_path=patches[0])

ax.axvspan(5.0,
           10.0,
           color=dgmap(100),
           alpha=.5,
           clip_path=patches[0])

ax.axvspan(10.0,
           15.0,
           color=dgmap(200),
           alpha=.5,
           clip_path=patches[0])

ax.axvspan(15.0,
           np.max(list),
           color=dgmap(300),
           alpha=.5,
           clip_path=patches[0])

ax.axvline(moy,
           color='k',
           lw=2.0)

ax.tick_params(direction='in',
               length=5, width=1,
               labelsize=15,
               top=True, right=True)

ax.set_xticks(np.arange(0, 21, step=1.0))

ax.set_xlim((0, 20))

ax.set_xlabel(r"$\mathrm{Notes}$ ", fontsize="x-large")
ax.set_ylabel(r"$\mathrm{N}_\mathrm{notes}$ ", fontsize="x-large")

plt.title('Résultat C3 : moyenne = '
          + str(round(moy, 2))
          + ', écart-type = '
          + str(round(std, 2)))

dir_path = os.path.dirname(os.path.realpath(__file__))

fig = plt.gcf()
fig.savefig(dir_path + '/Res_C3_S1-GC.pdf',
            bbox_inches='tight')

# plt.show()