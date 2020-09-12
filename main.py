import experiment
import psutil

def main():
    print("Start program\nMemory info: " , psutil.virtual_memory())
    experiment.start_experiment()


main()
