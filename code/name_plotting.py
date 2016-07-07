import matplotlib.pylab as plt

def name_plotter(input_dict):
#INPUT: A dictionary with keys = (name, year) and values of a dictionary with Counts for that
# name and year combination; a list of names for which to sum their counts
# OUTPUT: A dictionary with counts of the names given broken down by year (year is the key,
# count the value)
    years = input_dict.keys()
    x_min = min(years)
    x_max = max(years)

    X = []
    Y = []

    for x, y in input_dict.iteritems():
        X.append(x)
        Y.append(y)

    zipped_vals = sorted(zip(X,Y))
    sorted_x, sorted_y = zip(*zipped_vals)

    fig = plt.figure(figsize=(10,8))
    plt.plot(sorted_x, sorted_y)
    plt.xlabel('Year')
    plt.ylabel('Name Count')

def plot_loop(dataframe, names_list):

    fig = plt.figure(figsize=(10,8))

    for name in names_list:
        y = dataframe[(dataframe.Name == name)].Count.values
        x = dataframe[(dataframe.Name == name)].Year.values
        zipped_vals = sorted(zip(x,y))
        X,Y = zip(*zipped_vals)

        plt.plot(X,Y)
        plt.show()
    plt.xlabel('Year')
    plt.ylabel('Name Count')
    plt.ylim([0,200])
