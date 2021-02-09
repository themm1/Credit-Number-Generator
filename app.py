from flask import Flask, render_template, request
import random
from credit import Brand, CreditNumber, generate, validate

app = Flask(__name__)

amex = Brand("American Express", [15], ["34", "37"])
masterc = Brand("Master Card", [16], [str(number) for number in range(50, 56)])
visa = Brand("VISA", [13, 16, 19], [str(number) for number in range(40, 50)])

BRANDS = [amex, masterc, visa]


@app.route("/")
def index():
    return render_template("index.html", brands=BRANDS)

@app.route("/generate", methods=["POST"])
def generator():
    picked_brand = request.form.get("brand")
    for brand in BRANDS:
        if brand.name == picked_brand:
            number = generate(brand)
            break
    else:
        number = generate(random.choice(BRANDS))
    return render_template("index.html", brands=BRANDS, generated_number=f"Generated Number: {number}")

@app.route("/validate", methods=["POST"])
def validator():
    message = validate(request.form.get("number"), BRANDS)
    return render_template("index.html", brands=BRANDS, message=message)


if __name__ == "__main__":
    app.run(debug=True)