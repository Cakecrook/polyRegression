This is a project from my CS 460G (Machine Learning) course. The task was to use gradient descent to perform polynomial regression on three synthetic data sets.

50 of the possible points were for implementing the algorithm such that the Mean Squared Error was less than the following benchmarks:

                First Order     Second Order    Fourth Order    Seventh Order
Synthetic 1:       30 MSE          30 MSE          20 MSE           15 MSE
Synthetic 2:       60 MSE          60 MSE          60 MSE           60 MSE
Synthetic 3:     0.75 MSE        0.75 MSE         0.7 MSE          0.7 MSE

My implementation was successfully within 10 of these 12 benchmarks, and was not far off on the other 2. Here are my results:

                First Order     Second Order    Fourth Order    Seventh Order
Synthetic 1:    24.4589 MSE      24.1820 MSE    *23.6396 MSE    *21.9793 MSE
Synthetic 2:    49.0876 MSE      49.1208 MSE     49.1838 MSE     49.5888 MSE
Synthetic 3:     0.6652 MSE       0.6649 MSE      0.6638 MSE      0.6862 MSE

I put a * next to the two benchmarks that I missed.

The next 30 possible points came from plotting the lines with the points. My plotline function does this.
