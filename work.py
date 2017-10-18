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
                
            elif 'Jul' in totes[1]:
                Jul += 1
                Total_count += 1
                
            elif 'Aug' in totes[1]:
                Aug += 1
                Tota_count += 1
            elif 'Sep' in totes[1]:
                Sep += 1
                Total_count += 1
            else: pass
                    
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
    print('Total requests made for August:                  ...', Aug)
    print('Total requests made for September:                  ', Sep)
                

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

def files_by_month():
    #harder than expected
    
    Oct = []
    Nov = []
    Dec = []
    Jan = []
    Feb = []
    Mar = []
    Apr = []
    May = []
    Jun = []
    Jul = []
    Aug = []
    Sep = []   
    
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
                O = tuple(totes)
                Oct.append(O)
            
            elif 'Nov' in totes[1]:
                N = tuple(totes)
                Nov.append(N)
                
            elif 'Dec' in totes[1]:
                D = tuple(totes)
                Dec.append(D)
                
            elif 'Jan' in totes[1]:
                J = tuple(totes)
                Jan.append(J)
                
            elif 'Feb' in totes[1]:
                F = tuple(totes)
                Feb.append(F)
                
            elif 'Mar' in totes[1]:
                M = tuple(totes)
                Mar.append(M)
                
            elif 'Apr' in totes[1]:
                A = tuple(totes)
                Apr.append(A)
                
            elif 'May'in totes[1]:
                M = tuple(totes)
                May.append(M)
                
            elif 'Jun' in totes[1]:
                Ju = tuple(totes)
                Jun.append(Ju)
                
            elif 'Jul' in totes[1]:
                Jl = tuple(totes)
                Jul.append(Jl)  
                
            elif 'Aug' in totes[1]:
                AU = tuple(totes)
                Aug.append[AU]
            
            elif 'Sep' in totes[1]:
                SE = tuple(totes)
                Sep.append[SE]
                
            else: pass
            
    f = open("OctLog.txt","w+")
    a = len(Oct) 
    count1 = 0
    while count1 < a:
        OO = str(Oct[count1])
        f.write(OO)  
    f.close()    
    
    f = open("NovLog.txt","w+")
    b = len(Nov)
    count2 = 0
    while count2 < b:
        NN = str(Nov[count2])
        f.write(NN)
    f.close()
    
    f = open("DecLog.txt","w+")
    c = len(Dec)
    count3 = 0
    while count3 < c:
        DD = str(Dec[count3])
        f.write(DD)
    f.close()
    
    f = open("JanLog.txt","w+")
    d =len(Jan)
    count4 = 0
    while count4 < d:
        JJ = str(Jan[count4])
        f.write(JJ)
    f.close() 
    
    f = open("FebLog.txt","w+")
    e = len(Feb)
    count5 = 0
    while count5 < e:
        FF = str(Feb[count5])
        f.write(FF)
    f.close()    
    
    f = open("MarLog.txt","w+")
    f2 = len(Mar)
    count6 = 0
    while count6 < f2:
        MM = str(Mar[count6])
        f.write(MM)
    f.close() 
    
    f = open("AprLog.txt","w+")
    g = len(Apr)
    count7 = 0
    while count7 < g:
        AA = str(Apr[count7])
        f.write(AA)
    f.close()    
    
    f = open("MayLog.txt","w+")
    h = len(May)
    count8 = 0
    while count8 < h:
        MY = str(May[count8])
        f.write(MY)
    f.close()   
    
    f = open("JunLog.txt","w+")
    i = len(Jun)
    count9 = 0
    while count9<i:
        JN = str(Jun[count9])
        f.write(JN)
    f.close()    
    
    f = open("JulLog.txt","w+")
    j = len(Jul)
    count10 = 0
    while count10 < j:
        JL = str(Jul[count10])
        f.write(JL)
    f.close()
    
    f = open("AugLog.txt","w+")
    k = len(Aug)
    count11 = 0
    while count11 < k:
        AU = str(Aug[count11])
        f.write(AU)
    f.close()
    
    f = open("SepLog.txt", "w+")
    l = len(Sep)
    count12 = 0
    while count12 < l:
        SE = str(Sep[count12])
        f.write(SE)
    f.close()
    
    print("Your logs have been seperated into different files by month\n")
    
def main():
    print('\n-----------------------------------------\n')
    total = total_requests()
    print('The TOTAL requests made during this time period: ...', total,'\n')
    requests_per_month()
    print('\n')
    percentage_of_requests()
    files_by_month()
    
main()
