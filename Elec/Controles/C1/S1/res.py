import statistics as st
import matplotlib.pyplot as plt

list = [
    4.00,
    10.00,
    7.00,
    2.00,
    8.00,
    18.00,
    12.00,
    6.00,
    1.50,
    12.00,
    16.00,
    14.00,
    15.00,
    13.00,
    15.00,
    12.00,
    11.00,
    2.75,
    9.50,
    4.00,
    16.50,
    19.50,
    9.50,
    7.00,
    4.00,
    8.00,
    13.00,
    7.50]

moy = st.mean(list)
print('Moyenne = ', moy)

med = st.median(list)
print('Mediane = ', med)

std = st.stdev(list, moy)
print('Ecart-type = ', std)

fig = plt.figure(figsize=[8, 5])
ax = fig.add_axes([0.1, 0.12, 0.8, 0.8])

ax.hist(list, bins=[i for i in range(21)],
        histtype='stepfilled',
        color='blue', alpha=.5)

ax.hist(list, bins=[i for i in range(21)],
        histtype='step',
        color='blue', alpha=.8)

ax.axvline(moy,
           color='blue',
           lw=2.0)

ax.tick_params(direction='in',
               length=5, width=1,
               labelsize=15,
               top=True, right=True)

ax.set_xlim((0, 20))

ax.set_xlabel(r"$\mathrm{Notes}$ ", fontsize="x-large")
ax.set_ylabel(r"$\mathrm{N}_\mathrm{notes}$ ", fontsize="x-large")

plt.show()
