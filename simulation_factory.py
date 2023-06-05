import numpy
import matplotlib.pyplot as plt  # type: ignore
from simple_monte_carlo import MonteCarloSimulation

mean = .08/12
std_dev = .041


def display_distribution(generated_numbers, mean, std_dev):
    count, bins, ignored = plt.hist(generated_numbers, 30, density=True)
    plt.plot(bins, 1 / (std_dev * numpy.sqrt(2 * numpy.pi)) *
             numpy.exp(- (bins - mean) ** 2 / (2 * std_dev ** 2)),
             linewidth=2, color='r')
    plt.show()


if __name__ == '__main__':
    a = numpy.random.default_rng().normal(mean, std_dev, 40*12)
    len_a_zeroes = [float(x) for x in (numpy.zeros(len(a)))]
    # display_distribution(a, mean, std_dev)
    mc_sim = MonteCarloSimulation(a, 1, len_a_zeroes, len_a_zeroes)
    mc_sim.run()
    print(mc_sim.current_money)
    print(a[:10])





