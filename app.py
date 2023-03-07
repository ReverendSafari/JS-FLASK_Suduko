from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/handle_data', methods=['POST'])
def handle_data():
    dict = request.form
    suduko_numbers = []
    right_answers = [3, 1, 5, 4, 8, 2, 9, 6, 7,
     4, 9, 2, 7, 6, 5, 1, 3, 8,
     6, 7, 8, 1, 9, 3, 2, 4, 5,
     7, 2, 3, 9, 1, 6, 5, 8, 4,
     9, 6, 4, 2, 5, 8, 7, 1, 3,
     5, 8, 1, 3, 7, 4, 6, 9, 2,
     8, 5, 7, 6, 3, 1, 4, 2, 9,
     2, 3, 6, 5, 4, 9, 8, 7, 1,
     1, 4, 9, 8, 2, 7, 3, 5, 6]
    rightToString = []
    badCells = []

    for i in range(len(right_answers)):
        rightToString.append(str(right_answers[i]))

    for key in dict:
        suduko_numbers.append(dict[key])

    for i in range(len(right_answers)):
        if (suduko_numbers[i] != "" and suduko_numbers[i] != rightToString[i]):
            badCells.append(i)
    solved = 0
    if suduko_numbers == rightToString:
        solved = 1
    return render_template('mainTemp.html', values=suduko_numbers, badCells=badCells, solved=solved)



@app.route('/')
def hello_world():  # put application's code here
    suduko_numbers = [3,"",5,4,"",2,"",6,"",
4,9,"",7,6,"",1,"",8,
6,"","",1,"",3,2,4,5,
"","",3,9,"","",5,8,"",
9,6,"","",5,8,7,"",3,
"",8,1,3,"",4,"",9,2,
"",5,"",6,"",1,4,"","",
2,"","",5,4,9,"",7,"",
1,4,9,"","",7,3,"",6]
    for i in range (81):
        suduko_numbers.append(i)
    return render_template('mainTemp.html', values=suduko_numbers)


if __name__ == '__main__':
    app.run(debug=True)