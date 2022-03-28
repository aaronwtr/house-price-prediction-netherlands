import matplotlib.pyplot as plt
import pandas as pd


def plot_dataframe(data):
    if not isinstance(data, pd.DataFrame):
        raise TypeError("data must be of type pd.DataFrame!")

    fig = data.plot(x='number_of_movers', y='house_supply', kind='scatter', c=data.index, colormap='viridis',
                    colorbar=True)

    fig.set_xticklabels(fig.get_xticks(), rotation=45)
    fig.set_xticklabels(fig.get_xticks().round(0))
    plt.tight_layout()
    plt.show()
