import pandas as pd
import numpy as np
import time
pd.options.mode.chained_assignment = None                                                                               # default='warn'

# Test
#contacts = pd.read_excel(r'C:\Users\khafawaz\Desktop\BR Email 2\Contact Scrapping\Test.xlsx',sheet_name='Data')

secondsSinceEpoch_start = time.time()
timeObj_start = time.localtime(secondsSinceEpoch_start)
print()
print()

print('Start Time : %d-%d-%d %d:%d:%d' % (
timeObj_start.tm_mday, timeObj_start.tm_mon, timeObj_start.tm_year, timeObj_start.tm_hour, timeObj_start.tm_min, timeObj_start.tm_sec))
print()
print("___________________________________________________________")

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


# Main File
contacts = pd.read_excel('Contacts_Raw.xlsx')

contacts['Email'].replace('', np.nan, inplace=True)                                                              # Replace '' with 'nan' - 1
contacts['Email'].fillna('0', inplace=True)                                                                      # Fill 'na' with '0'    - 2

contacts_filtered = contacts[contacts['Email'] != "0"]                                                               # Main Table

distinct_vc = contacts_filtered['Vendor code'].unique()
#print(len(distinct_vc))

#distinct_contact_2_list =['Vendor Code', 'Email']
#distinct_contact_2_df = pd.DataFrame(distinct_contact_2_list,columns=['Type'])

#distinct_contact_2_df = pd.DataFrame({'Vendor code': range(3),"Email": range(3)})
distinct_contact_2_df = pd.DataFrame(columns=['Vendor code','Email'])

#contacts_filtered.to_csv(r'C:\Users\khafawaz\Desktop\Brand Registry - VSP\August\First Approach Email\Contacts_For_FA_Email_test.csv')

#print(distinct_contact_2_df)
#print()

#distinct_contact_2_df = pd.DataFrame({"col1": range(3),"col2": range(3)})

#distinct_contact_2_df.iloc[0,0] = np.nan
#print(distinct_contact_2_df.iloc[0,0])

def listToString(email_list):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in email_list:
        str1 = str(str1) + ele + ";"

        # return string
    return str1

ele_1=[]

# A List of Items
l = len(distinct_vc)

# Initial call to print 0% progress
printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)


for i in range(0,len(distinct_vc)):
    value = distinct_vc[i]
    #print(value)
    distinct_contact = contacts[contacts['Vendor code'].str.contains(value)]
    distinct_contact_1 = distinct_contact[['Vendor code','Email']]
    distinct_contact_1.drop_duplicates(inplace=True)
    #print(distinct_contact_1)
    #print("----------------------------")
    email_list = distinct_contact_1['Email'].tolist()
    #print(listToString(email_list))
    email_str = listToString(email_list)
    #print("----------------------------")

    #distinct_contact_2_df = distinct_contact_1.append(distinct_vc[i],ignore_index=True)
    #ele_1.append(distinct_contact_2_df.iloc[0, 0])
    distinct_contact_2_df = distinct_contact_2_df.append(pd.DataFrame({'Vendor code': value, 'Email': email_str[:-1]},index=[i]))
    time.sleep(0.1)
    printProgressBar(i + 1, l, prefix='Progress:', suffix='Complete', length=50)
    #distinct_contact_2_df.iloc[i:0] = value
    #print(distinct_contact_2_df.iloc[i,1])

#distinct_contact_3_df = distinct_contact_3_df(index )

distinct_contact_2_df.to_csv('Result.csv')

secondsSinceEpoch_end = time.time()
timeObj_end = time.localtime(secondsSinceEpoch_end)
print("___________________________________________________________")
print()
print('End TimeStamp : %d-%d-%d %d:%d:%d' % (
timeObj_end.tm_mday, timeObj_end.tm_mon, timeObj_end.tm_year, timeObj_end.tm_hour, timeObj_end.tm_min, timeObj_end.tm_sec))


# For Test
#distinct_contact_2_df.to_excel(r'C:\Users\khafawaz\Desktop\BR Email 2\Contact Scrapping\Result.xlsx')

# For Main File

#print(ele_1)