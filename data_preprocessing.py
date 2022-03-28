import cbsodata as cbs
import pandas as pd
import pickle as pkl
import os


def get_data(datasets):
    """
    Get data from the cbsodata library.
    :param datasets: Dictionary of datasets to download. The keys are the dataset ids corresponding to CBS url and the
    values are the names of the datasets.
    :return: List of all the retrieved datasets in dataframe format.
    """
    data = []
    for dataset_id, dataset_name in datasets.items():
        if os.path.exists(f'datasets/{dataset_name}.pkl'):
            data.append(pkl.load(open(f'datasets/{dataset_name}.pkl', 'rb')))
        else:
            data.append(pd.DataFrame(cbs.get_data(dataset_id)))
            pkl.dump(data, open(f'datasets/{dataset_name}.pkl', 'wb'))
            print(f'{dataset_name} saved!')
    return data


class Filtering:
    def __init__(self, region):
        self.periods_of_interest = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
        self.region = region

    def filter_movers_data(self, number_of_movers):
        """
        Filter the data to only include movers in the indicated region from the RegioS column. Also, only include movers
        from the period of interest. We also only want to consider the Verhuismobiliteit_5 column.
        :param number_of_movers: Dataframe of the number_of_movers_data
        :param region: Given region in the Netherlands
        :return:
        """
        number_of_movers_regions = number_of_movers[number_of_movers['RegioS'] == self.region]
        number_of_movers_regions = number_of_movers_regions[number_of_movers_regions['Perioden'].isin(self.periods_of_interest)]
        number_of_movers_data = number_of_movers_regions[['Perioden', 'Verhuismobiliteit_5']]
        number_of_movers_data.rename(columns={'Verhuismobiliteit_5': 'number_of_movers'}, inplace=True)
        number_of_movers_data = number_of_movers_data.set_index('Perioden')

        return number_of_movers_data

    def filter_house_supply(self, house_supply):
        house_supply = house_supply[house_supply['RegioS'] == self.region]
        house_supply = house_supply[house_supply['StatusVanBewoning'] == 'Totaal']
        house_supply = house_supply[house_supply['Perioden'].isin(self.periods_of_interest)]
        house_supply = house_supply[['Perioden', 'Koopwoningen_2']]
        house_supply.rename(columns={'Koopwoningen_2': 'house_supply'}, inplace=True)
        house_supply = house_supply.set_index('Perioden')

        return house_supply
