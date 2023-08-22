#Implement the cleanFiles function in the code cell below.

  
'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members
    
    This function should remove all rows from currentMem containing 'no' 
    in the 'Active' column and appends them to exMem.
    '''
def cleanFiles(currentMem,exMem):
    with open(currentMem,'r+') as writeFile: 
        with open(exMem,'a+') as appendFile:
            #get the data
            writeFile.seek(0)
            members = writeFile.readlines()
            #remove header
            header = members[0]
            members.pop(0)
    # TODO: Open the currentMem file as in r+ mode
    # TODO: Open the exMem file in a+ mode
    # TODO: Read each member in the currentMem (1 member per row) file into a list.
    # Hint: Recall that the first line in the file is the header.'''
            inactive = [member for member in members if ('no' in member)]
#TODO: iterate through the members and create a new list of the innactive members
#go to the beginning of the write file
            writeFile.seek(0) 
            writeFile.write(header)
            for member in members:
                if (member in inactive):
                    appendFile.write(member)
                else:
                    writeFile.write(member)      
            writeFile.truncate()
      # ''' Go to the beginning of the currentMem file
        # TODO: Iterate through the members list. 
        # If a member is inactive, add them to exMem, otherwise write them into currentMem'''


# Do not modify this code for this exercise.
memReg = '/members.txt'
exReg = '/inactive.txt'
cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())


#output :
'''
Active Members: 
Membership No  Date Joined  Active  
    96263      2018-5-16    yes   
    65001      2015-4-2     yes   
    72203      2020-2-23    yes   
    90344      2015-8-16    yes   
    34087      2017-7-10    yes   
    83812      2019-5-24    yes   
    19211      2016-12-15   yes   
    28662      2017-2-18    yes   
    82067      2016-5-3     yes   
    73538      2019-10-14   yes   
    22736      2020-5-11    yes   
    41109      2020-12-18   yes   
    55740      2019-5-6     yes   
    32981      2016-12-19   yes   

Inactive Members: 
Membership No  Date Joined  Active  
    97597      2017-6-6     no    
    48454      2017-8-1     no    
    15855      2016-10-9    no    
    58261      2018-11-2    no    
    18898      2015-10-8    no    
    94982      2018-8-4     no    
    91022      2019-7-9     no    
    78669      2015-10-13   no    
    62387      2018-12-1    no    
    '''
