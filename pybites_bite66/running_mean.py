def running_mean(sequence):
    
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    cumulative = 0
    running_means = []

    for count, val in enumerate(sequence):
      cumulative += val
        
      current_mean = round(cumulative / (count + 1),2)
      running_means.append(current_mean)

    return running_means