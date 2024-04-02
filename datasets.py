import csv
import matplotlib.pyplot as plt

def load_data(filename, column_index):
    data = []
    with open(filename) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            data.append(row[column_index])
    return data

def create_subplot(ax, data, title, fontsize='medium'):
    value_counts = {}
    for value in data:
        value_counts[value] = value_counts.get(value, 0) + 1
    labels = value_counts.keys()
    counts = value_counts.values()
    ax.bar(labels, counts)
    ax.set_xlabel(title)
    ax.set_ylabel('Count')
    ax.tick_params(axis='x', rotation=90, labelsize=6)
    ax.tick_params(axis='y', labelsize=fontsize)

def main():
    filename = 'fuel.csv'
    year_data = load_data(filename, 1)
    model_data = load_data(filename, 2)
    engine_index_data = load_data(filename, 3)
    engine_cylinders_data = load_data(filename, 4)
    engine_displacement_data = load_data(filename, 5)
    fuel_type_data = load_data(filename, 9)

    fig, axs = plt.subplots(2, 3, figsize=(12, 12))

    # Plot each categorical variable
    create_subplot(axs[0, 0], year_data, 'Year')
    create_subplot(axs[0, 1], model_data, 'Model')
    create_subplot(axs[0, 2], engine_index_data, 'Engine Index')
    create_subplot(axs[1, 0], engine_cylinders_data, 'Engine Cylinders')
    create_subplot(axs[1, 1], engine_displacement_data, 'Engine Displacement')
    create_subplot(axs[1, 2], fuel_type_data, 'Fuel Type')

    # Set title for all subplots
    fig.suptitle('Distribution of Categorical Variables', fontsize=16)

    # Adjust layout
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.4, hspace=0.6)
    plt.show()

if __name__ == "__main__":
    main()