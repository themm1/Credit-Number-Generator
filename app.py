from flask import Flask, render_template, request, jsonify
import random
from credit import Brand, CreditNumber, generate, validate

app = Flask(__name__)

amex = Brand("American Express", [15], ["34", "37"])
masterc = Brand("Master Card", [16], [str(number) for number in range(51, 56)])
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
def advanced():
    return render_template("adv_generator.html", brands=BRANDS)

@app.route("/file_generator", methods=["POST"])
def advanced_generator():
    picked_brand = request.form["brand"]
    data_format = request.form["data_format"]
    count = request.form["count"]

    for brand in BRANDS:
        if brand.name == picked_brand:
            picked_brand = brand
            break

    makefile = makeFile(picked_brand, int(count))
    if data_format == "CSV":
        file = makefile.CSV()
    elif data_format == "XML":
        file = makefile.XML()
    else:
        file = makefile.JSON()
        
    return jsonify({"file": file, "data_format": data_format})


@app.route("/about/")
def about():
    return render_template("about.html")


class makeFile:
    def __init__(self, brand, count):
        self.brand = brand
        self.count = count

    def make(self, file, lambda_func):
        if self.brand in BRANDS:
            for _ in range(self.count):
                file.append(lambda_func(self.brand))
        else:
            for _ in range(self.count):
                file.append(lambda_func(random.choice(BRANDS)))
        return file

    def JSON(self):
        json = self.make([], lambda brand: {
                "CreditCard": {
                    "Brand": brand.name,
                    "Number": generate(brand)
                }
            })
        return json
        
    def CSV(self):
        header = ",".join(["Brand", "Number"])
        csv = self.make([header], lambda brand: ",".join([brand.name, generate(brand)]))
        return "\n".join(csv)

    def XML(self):
        xml = self.make(["<root>\n"], lambda brand: f"  <CreditCard>\n    <Brand>{brand.name}</Brand>\n\
    <Number>{generate(brand)}</Number>\n  </CreditCard>\n")
        xml.append("</root>")
        return "".join(xml)
        

if __name__ == "__main__":
    app.run(debug=True)