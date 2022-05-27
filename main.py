import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def zad1():
    ox = np.arange(-6,7, 0.1)
    oxtick = np.arange(-6,7,2)

    plt.plot(ox, 20*np.sin(ox), 'r--', label="y=20*sin(x)")
    plt.plot(ox, ((2*ox)/5)-2, color='orange',ls='dashed', label="y=(2x/5)-2")
    plt.plot(ox, 7-ox, 'g-', label="y=7-x")

    plt.legend(loc='lower left')
    plt.title('Tytuł ABCD')
    plt.ylim(-30,30)
    plt.xticks(oxtick)

    plt.savefig('zad1.jpg')

    plt.show()

def zad2():
    xlsx = pd.read_excel('mieszkania2.xlsx')
    df = pd.DataFrame(xlsx)
    new_df_2015 = df.loc[(df['Rok'] == 2015)]

    explode =[0.1,0.2,0.2]
    seria = new_df_2015.groupby('Formy budownictwa')['Wartość'].sum()
    colors = np.random.rand(len(seria), 3)

    wedges, texts, atotext = plt.pie(x=seria, labels=seria.index,
                                     autopct='%1.1f%%',
                                     textprops=dict(color="black"),
                                     colors=['c','pink','skyblue'],
                                     shadow=True,
                                     explode=explode)
    plt.title('Dane z roku 2015')
    plt.xlabel('Procentowy udział Form Budownictwa\n w danym roku')
    plt.annotate('165912', xy=(-0.3, 1),xycoords='axes fraction', fontsize=10, horizontalalignment='left', verticalalignment='bottom') #index w lewym gornym rogu
    plt.show()


def zad3():
    xlsx = pd.read_excel('turystyka2.xlsx')
    df = pd.DataFrame(xlsx)
    df2 = df.T
    df2.columns = ['Rok', 'Liczba Kategorii']
    df2['temp'] = 1

    new_df_2015 = df2.loc[(df2['Rok'] == 2015)]
    x = np.arange(new_df_2015.sum()['temp'])
    etykieta = list(x)
    wartosci = list(new_df_2015['Liczba Kategorii'])

    plt.bar(x=etykieta, height=wartosci, color=['c','pink'])
    plt.title('Kategoreie hoteli w roku 2015')
    plt.ylabel('ilość')
    plt.xlabel('Numer kategorii')
    plt.tick_params(axis='y', labelrotation = 45)
    plt.grid(axis="y", color="black", alpha=.5, linewidth=.4)
    plt.show()


zad3()