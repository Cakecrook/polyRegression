This is a project from my CS 460G (Machine Learning) course. The task was to use gradient descent to perform polynomial regression on three synthetic data sets.

50 of the possible points were for implementing the algorithm such that the Mean Squared Error was less than the following benchmarks:

  Synthetic 1: First Order - 30 MSE, Second Order - 30 MSE, Fourth Order - 20 MSE, Seventh Order - 15 MSE
  Synthetic 2: First Order - 60 MSE, Second Order - 60 MSE, Fourth Order - 60 MSE, Seventh Order - 60 MSE
  Synthetic 3: First Order - 0.75 MSE, Second Order - 0.75 MSE, Fourth Order - 0.7 MSE, Seventh Order - 0.7 MSE

My implementation was successfully within 10 of these 12 benchmarks, and was not far off on the other 2. Here are my results:

  Synthetic 1: First Order - 24.4589 MSE, Second Order - 24.1820 MSE, Fourth Order - *23.6396 MSE, Seventh Order - *21.9793 MSE
  Synthetic 2: First Order - 49.0876 MSE, Second Order - 49.1208 MSE, Fourth Order - 49.1838 MSE, Seventh Order - 49.5888 MSE
  Synthetic 3: First Order - 0.6652 MSE, Second Order - 0.6649 MSE, Fourth Order - 0.6638 MSE, Seventh Order - 0.6862 MSE

I put a * next to the two benchmarks that I missed.

The next 30 possible points came from plotting the lines with the points. My plotline function does this.
