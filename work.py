import urllib.request
from datetime import datetime

def requests_per_month():
    Total_count = 0
    
    Oct = 0
    Nov = 0
    Dec = 0
    Jan = 0
    Feb = 0
    Mar = 0
    Apr = 0
    May = 0
    Jun = 0
    Jul = 0
    Aug = 0
    Sep = 0
    
    
    data = urllib.request.urlopen('https://s3.amazonaws.com/tcmg412-fall2016/http_access_log')
    
    for line in data:
        #Turning each line into strings
        x = str(line)
        #ignore the weird lines #couldn't figure out how to work with them
        if len(x) < 74: pass
            
        else:    
            #creating a helpful list that seperates each line into sections
            a = x.split('[')
            b = a[1]
            c = b.split(']')
            d = [a[0], c[0], c[1]]
            aa = d[2]
            bb = aa.split('"')
            
            #having problems in this area due to length of some lines 
            
            if len(bb) < 3:
                totes = [a[0], c[0], bb[1]]
            else:
                aaa = bb[2]
                ccc = aaa.split()
                if len(ccc) < 2:
                    totes = [a[0], bb[1], ccc[0]]
                else:
                    totes = [a[0], c[0], bb[1], ccc[0],ccc[1]]
                
            #counting requests for each month 
            
            if 'Oct' in totes[1]:
                Oct += 1
                Total_count += 1
                
            elif 'Nov' in totes[1]:
                Nov += 1 
                Total_count += 1
                
            elif 'Dec' in totes[1]:
                Dec += 1
                Total_count += 1
                
            elif 'Jan' in totes[1]:
                Jan += 1
                Total_count += 1
                
            elif 'Feb' in totes[1]:
                Feb += 1
                Total_count += 1
                
            elif 'Mar' in totes[1]:
                Mar += 1
                Total_count += 1
                
            elif 'Apr' in totes[1]:
                Apr += 1
                Total_count += 1
                
            elif 'May'in totes[1]:
                May += 1
                Total_count += 1
                
            elif 'Jun' in totes[1]:
                Jun += 1
                Total_count += 1
                
            else:
                Jul += 1
                Total_count += 1
                    
    print('Total requests made for October:                 ...', Oct)          
    print('Total requests made for November:                   ', Nov)
    print('Total requests made for December:                ...', Dec)
    print('Total requests made for January:                    ', Jan)
    print('Total requests made for February:                ...', Feb)
    print('Total requests made for March:                      ', Mar)
    print('Total requests made for April:                   ...', Apr)
    print('Total requests made for May:                        ', May)
    print('Total requests made for June:                    ...', Jun)
    print('Total requests made for July:                       ', Jul)
                

def total_requests():
    
    Total_count = 0
    
    data = urllib.request.urlopen('https://s3.amazonaws.com/tcmg412-fall2016/http_access_log')
    
    for line in data:
        
        x = str(line)
        if len(x) < 74: pass
            
        else:    
            Total_count += 1
                       
    
    return Total_count
    
    
def percentage_of_requests():   
    Total_count = 0
    
    NotS = 0
    Red = 0
    
    data = urllib.request.urlopen('https://s3.amazonaws.com/tcmg412-fall2016/http_access_log')
    
    for line in data:
        #Turning each line into strings
        x = str(line)
        #ignore the weird lines #couldn't figure out how to work with them
        if len(x) < 74: pass
            
        else:    
            #creating a helpful list that seperates each line into sections
            a = x.split('[')
            b = a[1]
            c = b.split(']')
            d = [a[0], c[0], c[1]]
            aa = d[2]
            bb = aa.split('"')
            
            #having problems in this area due to length of some lines 
            
            if len(bb) < 3:
                totes = [a[0], c[0], bb[1]]
            else:
                aaa = bb[2]
                ccc = aaa.split()
                if len(ccc) < 2:
                    totes = [a[0], bb[1], ccc[0]]
                else:
                    totes = [a[0], c[0], bb[1], ccc[0],ccc[1]]    
                    
            if len(totes) < 4: pass
            
            else:
                if '4' in totes[3]:
                    NotS += 1
                elif '3' in totes[3]:
                    Red += 1
                else: pass
    total = total_requests()
    
    NS = (NotS/total) * 100
    NotSuccessful = str("%.2f" % NS) + '%'
    
    RD = (Red/total) * 100
    Redirected = str("%.2f" % RD) + '%'
    
    print("Percentage of requests not successful:          ...", NotSuccessful)                         
    print("Percentage of requests that were redirected:    ...", Redirected)

    
def main():
    print('\n-----------------------------------------\n')
    total = total_requests()
    print('The TOTAL requests made during this time period: ...', total,'\n')
    requests_per_month()
    print('\n')
    percentage_of_requests()
    
main()
