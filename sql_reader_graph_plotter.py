import pandas as pd
import sqlite3
import statistics as st
import matplotlib.pyplot as plt

database_name = "GraduationStudents.db"

#create connection to sqlite database 
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn

#this method reads data from a csv file and then stores it in the database
def read_data_from_csv_store_in_db () :
    df = pd.read_csv("D:\Python\grad-students.csv")

    conn = create_connection(database_name)

    df.to_sql("GRADUATION_STUDENTS", conn, if_exists='replace', index=False)    

#method to analyse data and to plot it against given attributes
def analyse_data_to_plot():
     
     conn = create_connection(database_name)   
     conn.row_factory = sqlite3.Row
   
     cur = conn.cursor()
     cur.execute("SELECT  * from GRADUATION_STUDENTS LIMIT 5")
 
     data_fetch = cur.fetchall()
     #create lists to store data
     majors = []
     grad_totals = []
     grad_employed = []
     diff_employed_graduated =[]

     for row in data_fetch:
        majors.append(str(row['Major_code']))
        grad_totals.append(row['Grad_total'])
        grad_employed.append(row['Grad_employed'])
        diff_employed_graduated.append(row['Grad_total']-row['Grad_employed'])
    
    #A general graph to plot two datas across one 
     plt.plot(  majors,  grad_totals , label = "Total Graduated" )
     plt.plot(  majors,  grad_employed , label = "Total Employed" )
     plt.xlabel('Major - code') 
     plt.ylabel('No of people')
     plt.title('Total graduated vs Total Employed ') 
     plt.legend()
     plt.savefig("D:\Python\\totalEmployed_totalGraduated.png")
     plt.figure(figsize=(18, 6))

     #splitting three datas in three different graphs
     plt.subplot(131)
     plt.bar(  majors,  grad_totals   )
     plt.xlabel('Major - code') 
     plt.ylabel('No of people graduated')

     plt.subplot(132)
     plt.xlabel('Major - code') 
     plt.ylabel('No of people employed')
     plt.bar(  majors,  grad_employed   )

     plt.subplot(133)
     plt.xlabel('Major - code') 
     plt.ylabel('No of graduated minus employed')
     plt.plot(  majors,  diff_employed_graduated   )

     plt.suptitle('Graduate Students Details')
  
     plt.savefig("D:\Python\\Cumulative.png")
   

analyse_data_to_plot()






