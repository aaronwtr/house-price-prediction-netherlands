from data_preprocessing import *
from utils import *

if __name__ == '__main__':
    datasets = {'60048ned': 'number_of_movers', '82900NED': 'house_supply'}
    region_of_interest = 'Zuid-Holland (PV)'

    data = get_data(datasets)

    filtering = Filtering(region_of_interest)
    number_of_movers = filtering.filter_movers_data(data[0][0])
    house_supply = filtering.filter_house_supply(data[1][1])
    merged_data = pd.concat([number_of_movers, house_supply], axis=1)

    plot_dataframe(merged_data)
