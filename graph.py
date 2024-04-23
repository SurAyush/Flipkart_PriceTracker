import pandas as pd
from matplotlib import pyplot as plt


def save_graph(id,title,threshold):

    df = pd.read_csv('FLipkartWebScraperDataset.csv')
    df2 = df.loc[df['Title'] == title]
    price_list = list(df2['Price'])
    time_list = list(df2['Date'])
    time = []
    for el in time_list:
        s = el[2:10] + "\n" + el[11:16]
        time.append(s)

    plt.plot(time, price_list, marker="*", linewidth=2,label='Price')
    plt.axhline(y=threshold, color='r', linestyle='--', label='Threshold Line')
    plt.xlabel("Time stamp")
    plt.ylabel(f"Price of {title}")
    plt.tight_layout()  # improves padding on smaller screen
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.style.use('ggplot')
    plt.legend()
    # plt.show()
    plt.savefig(f'{id}.png')
    plt.clf()

# save_graph(uuid.uuid4(),12,25000)