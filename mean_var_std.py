import numpy as np
def calculate(input_list):
 if len(input_list) !=9:
    return("Input list must contain exactly 9 digits")
 else:  
  array=np.array(input_list).reshape(3,3)
 stats = {}
 stats['mean_row']=np.mean(array,axis =0)
 stats['variance_row']=np.var(array,axis=0)
 stats['standard_deviation_row']=np.std(array,axis=0)
 stats['max_row']=np.max(array,axis=0)
 stats['min_row']=np.min(array,axis=0)
 stats['sum_row']=np.sum(array,axis=0)

 stats['mean_column']=np.mean(array,axis =1)
 stats['variance_column']=np.var(array,axis=1)
 stats['standard_deviation_column']=np.std(array,axis=1)
 stats['max_column']=np.max(array,axis=1)
 stats['min_column']=np.min(array,axis=1)
 stats['sum_column']=np.sum(array,axis=1)

 stats['mean_flat']=np.mean(array.flatten())
 stats['variance_flat']=np.var(array.flatten())
 stats['standard_deviation_flat']=np.std(array.flatten())
 stats['max_flat']=np.max(array.flatten())
 stats['min_flat']=np.min(array.flatten())
 stats['sum_flat']=np.sum(array.flatten())

 return stats

