__author__ = 'Aman'
from urllib import  request #from keyword
csv_url = "http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=10&e=20&f=2014&g=d&a=2&b=27&c=2014&ignore=.csv"
def download_csv_file(csv_url_link) :
#now we need our program to connect to internet
    response = request.urlopen(csv_url_link) #store the response from the link
    print("Response: ", response)
    csv = response.read()
    print("CSV",csv)
    csv_string = str(csv)
    print("csv_string",csv_string)
    #now I am spliting the lines by new line char
    lines = csv_string.split("\\n")
    print("lines",lines)
    dest_url = r"google.csv"
    fw = open(dest_url,"w")
    for line in lines :
        fw.write(line + "\n")
    fw.close()

download_csv_file(csv_url)