from flask import Flask, render_template

#Project by Kaija Pendergast and Brandi Babilya

app = Flask(__name__)

color1 = "black"
color2 = "red"
row = 8
column = 8

@app.route ("/") 
#Mainpage!
def get_main_page():
    return render_template("index.html",color1 = color1,color2 = color2, column = column, row = row)

@app.route ("/<column>") 
#All columns, rows and one color declared
def get_column(column):
    get_main_page()
    return render_template("index.html",color1 = color1, color2=color2,column = int(column), row = row )

@app.route ("/<column>/<row>") 
#All columns, rows and one color declared
def get_columns_and_rows(column,row):
    get_main_page()
    return render_template("index.html",color1 = color1, color2=color2,column = int(column), row = int(row) )

@app.route ("/<column>/<row>/<color1>") 
#All columns, rows and one color declared
def get_column_row_color(column,row,color1):
    return render_template("index.html", column = int(column), row = int(row), color1 = color1,color2 = color2 )

@app.route ("/<column>/<row>/<color1>/<color2>") 
#All columns, rows and colors declared
def get_new_columns_and_colors(column,row,color1,color2):
    return render_template("index.html", color1 = color1, color2 = color2, column = int(column), row = int(row))


if __name__ == "__main__":
    app.run(debug = True)
