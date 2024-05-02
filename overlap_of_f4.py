import matplotlib.pyplot as plt

def measure_overlap(n):
    f4 = [0]*(n+1)
    f4[3] = 0
    f4[4] = 1
    for i in range(5,n+1):
        #fibonacci_recursive(n)
        f4[i] =  f4[i-1] +f4[i-2]
    
    
    return print(f4), plot_overlap(f4)
        
def plot_overlap(overlap_counts):
    plt.plot(range(5, len(overlap_counts)), overlap_counts[5:], label='Number of F(4) computations')
    plt.xlabel('n')
    plt.ylabel('Count')
    plt.title('Degree of Overlapping Subproblems')
    plt.legend()
    plt.savefig('overlap.png')
    plt.show()
    
def main():
    measure_overlap(50)

main()
    

