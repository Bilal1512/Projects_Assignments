# # All decimal 3 places
# a=3.4
# a="{0:.3f}".format(a)
# print(a)
# Function to compute mean
import math

def sum_of_list(first_list):
    a=0
    for i in range(len(first_list)):
        a+=first_list[i]
    return a

def mean(first_list):
    if len(first_list) is 0:
        return 0
    mean_value = sum_of_list(first_list)/len(first_list)
    return round(mean_value,3)

def sort_list(first_list):
    for i in range(len(first_list)):
        for j in range(i,len(first_list)):
            if(first_list[j]<first_list[i]):
                first_list[i],first_list[j]=first_list[j],first_list[i]
    return first_list

# Function to compute median. You cant use Python functions
def median(first_list):
    if len(first_list) is 0:
        return 0
    first_list=sort_list(first_list)
    if len(first_list)%2 is 1:
        median_value=first_list[int(len(first_list)/2)]
    else:
        median_value=(first_list[int(len(first_list)/2)-1]+first_list[int(len(first_list)/2)])/2
    return round(median_value,3)


print(median([3,1,4,2,5,1]))
print(sort_list([3,1,4,2,5,1]))
# # Function to compute Standard deviation. You cant use Python functions
# def standard_deviation(first_list):
#     # Standard deviation Logic
#     return standard_deviation_value


# # Function to compute variance. You cant use Python functions
# def variance(first_list):
#     # variance Logic
#     return variance_value


# # Function to compute RMSE. You cant use Python functions
# def rmse(first_list, second_list):
#     # RMSE Logic
#     return rmse_value


# # Function to compute mse. You cant use Python functions
# def mse(first_list, second_list):
#     # mse Logic
#     return mse_value


# # Function to compute mae. You cant use Python functions
# def mae(first_list, second_list):
#     # mae Logic
#     return mae_value


# # Function to compute NSE. You cant use Python functions
# def nse(first_list, second_list):
#     # nse Logic
#     return nse_value


# # Function to compute Pearson correlation coefficient. You cant use Python functions
# def pcc(first_list, second_list):
#     # nse Logic
#     return pcc_value


# # Function to compute Skewness. You cant use Python functions
# def skewness(first_list):
#     # Skewness Logic
#     return skewness_value
    
# def sorting(first_list):
#     # Sorting Logic
#     return sorted_list


# # Function to compute Kurtosis. You cant use Python functions
# def kurtosis(first_list):
#     # Kurtosis Logic
#     return kurtosis_value


# # Function to compute sum. You cant use Python functions
# def summation(first_list):
#     # sum Logic
#     return summation_value
