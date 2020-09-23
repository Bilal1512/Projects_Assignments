# All decimal 3 places
# Function to compute sum. You cant use Python functions
import math
def summation(first_list):
    for i in range(len(first_list)):
        if isinstance(first_list[i],(int,float)) is False:
            return 0
    summation_value=0.0
    for i in range(len(first_list)):
        summation_value+=first_list[i]
    return summation_value


def mean(first_list):
    if len(first_list) is 0:
        return 0
    for i in range(len(first_list)):
        if isinstance(first_list[i],(int,float)) is False:
            return 0
    mean_value = summation(first_list)/len(first_list)
    return mean_value

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
    for i in range(len(first_list)):
        if isinstance(first_list[i],(int,float)) is False:
            return 0
    first_list=sorting(first_list.copy())
    if len(first_list)%2 is 1:
        median_value=first_list[int(len(first_list)/2)]
    else:
        median_value=(first_list[int(len(first_list)/2)-1]+first_list[int(len(first_list)/2)])/2
    return median_value

# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    if len(first_list) is 0 or len(first_list)!=len(second_list):
        return 0
    for i in range(len(first_list)):
        if isinstance(first_list[i],(int,float)) is False or isinstance(second_list[i],(int,float)) is False:
            return 0
    temp=0
    for i in range(len(first_list)):
        temp+=((first_list[i]-second_list[i])*(first_list[i]-second_list[i]))
    mse_value=temp/len(first_list)
    return mse_value

# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    for i in range(len(first_list)):
        if isinstance(first_list[i],(int,float)) is False or isinstance(second_list[i],(int,float)) is False:
            return 0
    rmse_value= math.sqrt(mse(first_list,second_list))
    return rmse_value


# # Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    if len(first_list) is 0 or len(first_list)!=len(second_list):
        return 0
    for i in range(len(first_list)):
        if isinstance(first_list[i],(int,float)) is False or isinstance(second_list[i],(int,float)) is False:
            return 0
    mean_value=mean(first_list)
    temp1=mse(first_list, second_list)*len(first_list)
    temp2=0.0
    for i in range(len(first_list)):
        temp2+=(first_list[i]-mean_value)*(first_list[i]-mean_value)
    if temp2 is 0:
        return 0
    nse_value=1-(temp1/temp2)
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    if len(first_list) is 0 or len(first_list)!=len(second_list):
        return 0
    for i in range(len(first_list)):
        if isinstance(first_list[i],(int,float)) is False or isinstance(second_list[i],(int,float)) is False:
            return 0
    mean_value_x=mean(first_list)
    mean_value_y=mean(second_list)
    temp1=0.0
    temp2=0.0
    temp3=0.0
    for i in range(len(first_list)):
        temp1+=(first_list[i]-mean_value_x)*(second_list[i]-mean_value_y)
        temp2+=(first_list[i]-mean_value_x)*(first_list[i]-mean_value_x)
        temp3+=(second_list[i]-mean_value_y)*(second_list[i]-mean_value_y)
    if temp2 is 0 or temp3 is 0:
        return 0
    pcc_value=temp1/(math.sqrt(temp2)*math.sqrt(temp3))
    return pcc_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    if len(first_list) is 0 or len(first_list)!=len(second_list):
        return 0
    for i in range(len(first_list)):
        if isinstance(first_list[i],(int,float)) is False or isinstance(second_list[i],(int,float)) is False:
            return 0
    a=0
    for i in range(len(first_list)):
        a+=abs(first_list[i]-second_list[i])
    mae_value=a/len(first_list)
    return mae_value


# Function to compute variance. You cant use Python functions
def variance(first_list):
    if len(first_list) is 0 :
            return 0
    for i in range(len(first_list)):
        if isinstance(first_list[i],(int,float)) is False:
            return 0
    mean_value=mean(first_list)
    temp=0
    for i in range(len(first_list)):
        temp+=(first_list[i]-mean_value)*(first_list[i]-mean_value)
    variance_value=temp/len(first_list)
    return variance_value

# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    for i in range(len(first_list)):
        if isinstance(first_list[i],(int,float)) is False:
            return 0
    standard_deviation_value=math.sqrt(variance(first_list))
    return standard_deviation_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    for i in range(len(first_list)):
        if isinstance(first_list[i],(int,float)) is False:
            return 0
    standard_deviation_value=standard_deviation(first_list)
    if len(first_list) is 0 or standard_deviation_value is 0:
            return 0
    mean_value=mean(first_list)
    temp=0
    for i in range(len(first_list)):
        temp+=((first_list[i]-mean_value)*(first_list[i]-mean_value)*(first_list[i]-mean_value))/(standard_deviation_value*standard_deviation_value*standard_deviation_value)
    skewness_value=temp/len(first_list)
    return skewness_value

# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    for i in range(len(first_list)):
        if isinstance(first_list[i],(int,float)) is False:
            return 0
    standard_deviation_value=standard_deviation(first_list)
    if len(first_list) is 0 or standard_deviation_value is 0:
            return 0
    mean_value=mean(first_list)
    temp=0
    for i in range(len(first_list)):
        temp+=((first_list[i]-mean_value)*(first_list[i]-mean_value)*(first_list[i]-mean_value)*(first_list[i]-mean_value))/(standard_deviation_value*standard_deviation_value*standard_deviation_value*standard_deviation_value)
    kurtosis_value=temp/len(first_list)
    return kurtosis_value
