# All decimal 3 places
# Function to compute sum. You cant use Python functions
def summation(first_list):
    summation_value=0.0
    for i in range(len(first_list)):
        summation_value+=first_list[i]
    return round(summation_value,3)

def mean(first_list):
    if len(first_list) is 0:
        return 0
    mean_value = summation(first_list)/len(first_list)
    return round(mean_value,3)

def sorting(first_list):
    sorted_list=first_list
    for i in range(len(first_list)):
        for j in range(i,len(first_list)):
            if(sorted_list[j]<sorted_list[i]):
                sorted_list[i],sorted_list[j]=sorted_list[j],sorted_list[i]
    return sorted_list

def median(first_list):
    if len(first_list) is 0:
        return 0
    first_list=sorting(first_list)
    if len(first_list)%2 is 1:
        median_value=first_list[int(len(first_list)/2)]
    else:
        median_value=(first_list[int(len(first_list)/2)-1]+first_list[int(len(first_list)/2)])/2
    return round(median_value,3)

# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    if len(first_list) is 0 or len(first_list)!=len(second_list):
        return 0
    temp=0.0
    for i in range(len(first_list)):
        temp+=(first_list[i]-second_list[i])*(first_list[i]-second_list[i])
    mse_value=temp/len(first_list)
    return round(mse_value,3)

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


# # Function to compute Kurtosis. You cant use Python functions
# def kurtosis(first_list):
#     # Kurtosis Logic
#     return kurtosis_value

