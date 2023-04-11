from flask import Flask, request, render_template 


app = Flask(__name__)


#funtion to read details for page
def readDetails(filename):
    with open(filename, 'r') as f:
        return [line for line in f]
    
def writeToFile(filename, message):
    with open(filename, 'a')as f:
        f.write(message)

@app.route('/')
def HomePage():
    name = "Alberto Quintero"
    details = readDetails('/Users/albertoquintero/obj_ori_python/packages/flaskApp/static/details.txt')
    hobbies = readDetails('/Users/albertoquintero/obj_ori_python/packages/flaskApp/static/hobbies.txt')
    favorite_food = "Pizza, Chicken wings(pretty obvious since eating them is my hobby), and pasta"
    return render_template("base.html", name=name, aboutMe=details, hobbies=hobbies, favorite_food=favorite_food)
    


@app.route('/user/<name>')
def CodeProjects(name):
    # define categories and projects with their corresponding information
    categories = {
        "Python": [
            {"name": "Project A", "description": "Quiz Game", "date": "2023"},
            {"name": "Project B", "description": "Bank Program", "date": "2023"},
            {"name": "Project C", "description": "TicTacToe", "date": "2023"}
        ],
        "C++": [
            {"name": "Project D", "description": "HangMan Game", "date": "2023"},
            {"name": "Project E", "description": "Databases", "date": "2022"}
        ],
        "Other": [
            {"name": "Project F", "description": "No other programming language experience yet but i will add once  i experience others here."},
            {"name": "Project G", "description": "No other programming language experience yet but i will add once  i experience others here."}
        ]
    }
    
    # get category from query parameter or default to "Python"
    category = request.args.get('category', 'Python')
    
    # get projects for selected category
    projects = categories.get(category, [])
    
    # render template with projects and categories
    return render_template("code.html", projects=projects, categories=categories, selected_category=category)


@app.route('/form', methods =['GET', 'POST'])
def formDemo():
    name = None
    category = None
    message = None
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        message = request.form['message']
        
    return render_template('form.html', name=name, category=category, message=message)



## when runnig this file directly...
if __name__ == "__main__":
    app.run(debug=True, port=3000)