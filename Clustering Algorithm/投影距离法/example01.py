import proclus as prc
import plotter
import arffreader as ar
import numpy as np
# import adjrand

X, sup = ar.readarff("data/simple.arff")

Dims = [0,1]
# plotter.plotDataset(X, D = Dims) # plot 0-1 dimensions

R = 1 # toggle run proclus
RS = 0 # toggle use random seed

if R: # run proclus
	rseed = 902884
	if RS:
		rseed = np.random.randint(low = 0, high = 1239831)

	print ("Using seed %d" % rseed)

	M, D, A = prc.proclus(X, k = 3, l = 2, seed = rseed)
	print ("Accuracy: %.4f" % prc.computeBasicAccuracy(A, sup))
	# print ("Adjusted rand index: %.4f" % adjrand.computeAdjustedRandIndex(A, sup))
	
	plotter.plotClustering(X, M, A, D = Dims)