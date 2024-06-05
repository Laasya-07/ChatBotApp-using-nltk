from flask import Flask, render_template, request, jsonify
from chat import get_response

# flask constructor that points to the start of the application
app = Flask(__name__, template_folder='templates')

@app.route("/", methods=["GET"])
def index_get():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/blogs")
def blogs():
    return render_template('blogs.html')

@app.route("/shop")
def shop():
    return render_template('shop.html')
@app.route("/predict", methods=["POST"])
def predict():
    text = request.get_json().get('message')
    
    if "about page" in text.lower():
        return jsonify({"redirect": "/about"})
    if "home page" in text.lower():
        return jsonify({"redirect": "/"})
    if "blogs page" in text.lower():
        return jsonify({"redirect": "/blogs"})
    # if "shop page" in text.lower():
    #     return jsonify({"redirect": "/shop"})
    # check if text is valid
    response = get_response(text)
    #message = {"answer": response}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)