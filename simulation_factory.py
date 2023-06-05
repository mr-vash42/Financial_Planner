import numpy
import matplotlib.pyplot as plt

mean = 10
std_dev = 1


def display_distribution(generated_numbers, mean, std_dev):
    count, bins, ignored = plt.hist(generated_numbers, 30, density=True)
    plt.plot(bins, 1 / (std_dev * numpy.sqrt(2 * numpy.pi)) *
             numpy.exp(- (bins - mean) ** 2 / (2 * std_dev ** 2)),
             linewidth=2, color='r')
    plt.show()


if __name__ == '__main__':
    a = numpy.random.default_rng().normal(mean, std_dev, 10000)
    b = numpy.random.default_rng().lognormal(mean, std_dev, 100)
    display_distribution(a, mean, std_dev)
    print(b)




