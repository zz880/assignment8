import numpy as np
import matplotlib.pyplot as plt

class investment:
    # class investment includes the function used to run the simulation of investments
    def __init__(self, positions, num_trials):
        self.positions = positions
        self.num_trials = num_trials

    def investments(self):
        result = open('results.txt', 'w')
        for position in self.positions:
            cumu_ret = np.zeros(self.num_trials)
            daily_ret = np.zeros(self.num_trials)
            for trial in range(self.num_trials):
                position_value = 1000 / position
                sign = np.random.choice([2, 0], size=position, p=[0.51, 0.49]) # mimic biased coin
                cumu_ret[trial] = sum(sign * position_value)
                daily_ret[trial] = cumu_ret[trial]/1000 - 1
            mean_daily_ret = np.mean(daily_ret)
            std_daily_ret = np.std(daily_ret)
            result.write('Position Value:  {0}  Mean:  {1}  Standard Deviation:  {2} \n'.format(position,mean_daily_ret,std_daily_ret))
            plt.hist(daily_ret,100,range=[-1,1])
            plt.savefig("histogram_"+str(position).zfill(4)+"_pos.pdf")
            plt.close()
        result.close()



