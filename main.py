import matplotlib.pyplot as plt
from utils.execution_time_gathering import gather_execution_times

def plot_results(df):
    """
    Plots execution times of different palindrome checking algorithms.

    :param df: Pandas DataFrame with execution times.
    """
    plt.figure(figsize=(10, 6))

    plt.plot(df['Size'], df['Iterative'], label='Iterative Method', marker='s')
    plt.plot(df['Size'], df['Recursive'], label='Recursive Method', marker='^')
    plt.plot(df['Size'], df['Reverse'], label='Reverse Method', marker='o')

    plt.xlabel("String Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Palindrome Checking Algorithms")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    string_sizes = [50, 100, 150, 200, 250, 300, 350, 400, 450]
    df = gather_execution_times(string_sizes)
    plot_results(df)