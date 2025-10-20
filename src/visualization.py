import matplotlib.pyplot as plt
import seaborn as sns

def plot_coordinates(df):
    plt.figure(figsize=(10, 10))
    sns.scatterplot(x="latitude", y="longitude", hue="id", data=df)
    plt.title("User Movement Scatter Plot")
    plt.grid()
    plt.show()
