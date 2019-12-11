from flask import Flask, render_template 
import pandas as pd
import requests
from bs4 import BeautifulSoup 
import altair as alt 

app = Flask(__name__)

def scrap(url):
    #This is fuction for scrapping
    url_get = requests.get(url)
    soup = BeautifulSoup(url_get.content,"html.parser")
    
    #Find the key to get the information
    table = soup.find(...) 
    tr = table.find_all(...) 

    temp = [] #initiating a tuple

    for i in range(1, len(tr)):
        row = table.find_all('tr')[i]
        #use the key to take information here
        #name_of_object = row.find_all(...)[0].text






        temp.append((...)) #append the needed information 
    
    temp = temp[::-1] #remove the header

    df = pd.DataFrame(temp, columns = (....)) #creating the dataframe
   #data wranggling -  try to change the data type to right data type

   #end of data wranggling

    return df

@app.route("/")
# This fuction for rendering the table
def index():
    df = scrap(...) #insert url here
    df = df.to_html(classes=["table table-bordered table-striped table-dark table-condensed"])

    return render_template("index.html", table=df)


@app.route("/charts")
# This fuction for rendering the plot
def charts():
    df = scrap(...) #insert url here

    chart = (
        alt.Chart(df)
        .encode( 
            # Put the x and y
        )
        .mark_bar() # Choose the plot type here
        .interactive() # To make the plot interactive 
    )
    return chart.to_json() 


if __name__ == "__main__": 
    app.run()
