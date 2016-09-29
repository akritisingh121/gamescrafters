from mpi4py import MPI

def filter_py(filter, data) :
	new_data = [];
	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()

	if rank != 0:
	    data = []

	#Scatter
	data = comm.scatter(data, root=0)
	print "rank", rank, "recieved", data
	for x in data:
		if filter(x):
			new_data += [x]

	#Gather
	new_data = comm.gather(new_data, root=0)

	comm.Barrier()

	if rank == 0:
	    print new_data