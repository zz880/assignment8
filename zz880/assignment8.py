from investment import *

def main():
    try:
        positions = raw_input("Enter a list of the number of shares to buy in parallel: e.g. 1,10,100,1000 \n")
        positions_split = positions.split(",")
        position_list = [int(position) for position in positions_split]
    except:
        print ("Invalid Input. Please Enter a list of the number of shares, e.g. 1,10,100,1000 \n")

    try:
        num_trials = int(raw_input("How many times to randomly repeat the test?\n"))
    except:
        print ("Invalid Input. Please enter an positive integer")
    outcome = investment(position_list, num_trials)
    outcome.investments()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard Interruption")







