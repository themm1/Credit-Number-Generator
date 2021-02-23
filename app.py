from flask import Flask, render_template, request, jsonify
import random
from credit import Brand, CreditNumber, generate, validate

app = Flask(__name__)

amex = Brand("American Express", [15], ["34", "37"])
masterc = Brand("Master Card", [16], [str(number) for number in range(50, 56)])
visa = Brand("VISA", [13, 16, 19], [str(number) for number in range(40, 50)])

BRANDS = [amex, masterc, visa]


@app.route("/")
def home():
    brands_dict = {}
    for brand in BRANDS:
        numbers = []
        for i in range(3):
            numbers.append(generate(brand))
        brands_dict[brand.name] = numbers
            
    return render_template("home.html", brands=BRANDS, brands_dict=brands_dict)

@app.route("/generate", methods=["POST"])
def generator():
    picked_brand = request.form["brand"]
    for brand in BRANDS:
        if brand.name == picked_brand:
            number = generate(brand)
            break
    else:
        number = generate(random.choice(BRANDS))
    return jsonify({"number": f"Generated Number: {number}"})

@app.route("/validate", methods=["POST"])
def validator():
    message = validate(request.form.get("number"), BRANDS)
    return jsonify({"message": message})

@app.route("/advanced/")
def adv_generator():
    return render_template("adv_generator.html")

@app.route("/about/")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)