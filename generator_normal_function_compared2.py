'''There is one thing to keep in mind, though. If the list is smaller than the running machine’s available memory, then list comprehensions can be faster to evaluate than the equivalent generator expression. To explore this, let’s sum across the results from the two comprehensions above. You can generate a readout with cProfile.run():'''
import cProfile
cProfile.run('sum([i * 2 for i in range(10000)])')

cProfile.run('sum((i * 2 for i in range(10000)))')

'''Here, you can see that summing across all values in the list comprehension took about a third of the time as summing across the generator. 
If speed is an issue and memory isn’t, then a list comprehension is likely a better tool for the job.'''