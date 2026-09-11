from merge_sort_alg import merge_sort
import numpy as np
import timeit
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

rng = np.random.default_rng(42)

def random_list(N):
    rand_L = np.round(rng.uniform( low=-100.0, high=100.0, size=N), decimals=4)

    return rand_L.tolist()

def running_time(L):
    return timeit.timeit(
        lambda: merge_sort(L),
        number=1
    )

def median_time(n):
    times = []
    for _ in range(25):
        L = random_list(n)
        times.append(running_time(L))

    return np.median(times)


def create_data():
    data_points = []
    list_lengths = rng.integers(low=2, high=10001, size=300) #we will generate 300 data points of size at most 10000
    for n_len in list_lengths:
        time_L = median_time(n_len)
        data_points.append([n_len, time_L])

    return data_points



if __name__ == "__main__":

    data_points = create_data()
    x = [point[0] for point in data_points]
    y1 = [point[1] for point in data_points]
    y2 = [p[1]/(p[0]*np.log2(p[0])) for p in data_points]
    C = np.median(y2)

    time_formatter = FuncFormatter(lambda y, _: f"{1000*y:.2f} ms")
    normalized_formatter = FuncFormatter(lambda y, _: f"{1e9*y:.1f} ns")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    #T(n) vs n
    ax1.scatter(x, y1)
    ax1.yaxis.set_major_formatter(time_formatter)

    ax1.set_xlabel("n")
    ax1.set_ylabel("T(n)")
    ax1.set_title("Merge-sort running time")

    #We try to approximate T(n) by C*nlog(n)
    x_model = np.sort(np.array(x))
    y_model = C * x_model * np.log2(x_model)

    ax1.plot(
        x_model,
        y_model,
        label=r"$C n\log_2 n$"
    )

    ax1.legend()


    #T(n)/(nlog(n)) vs n
    ax2.scatter(x, y2)
    ax2.yaxis.set_major_formatter(normalized_formatter)

    ax2.set_xlabel("n")
    ax2.set_ylabel(r"$T(n)/(n\log_2 n)$")
    ax2.set_title(rf"Normalized merge-sort running time C $\approx$ {C * 1e9:.1f} ns")

    plt.tight_layout()
    plt.savefig("merge_sort_plots.png")
    plt.show()

    print(f"C ≈ {C * 1e9:.2f} ns")
