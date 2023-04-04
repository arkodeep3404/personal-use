from flask import Flask,render_template,request,redirect
import json

app=Flask(__name__)

@app.route("/")
def homePage():
    return render_template("index.html")


@app.route("/buy.html")
def buyPage():
    return render_template("buy.html")

@app.route("/contact.html")
def conatctPage():
    return render_template("contact.html")

@app.route("/flat.html", methods=["POST","GET"])
def flatPage():
    if request.method=="POST":
        flatDetail = request.form
        flatAddress = flatDetail["address"]
        flatFloor = flatDetail["floor"]
        flatFlat = flatDetail["flat"]
        flatProject = flatDetail["project"]
        flatCluster = flatDetail["cluster"]
        flatBuilding = flatDetail["building"]
        flatOwner = flatDetail["owner"]
        flatSuper = flatDetail["super"]
        flatCarpet = flatDetail["carpet"]
        flatFacing = flatDetail["facing"]
        print(flatAddress,flatFloor,flatFlat,flatProject,flatCluster,flatBuilding,flatOwner,flatSuper,flatCarpet,flatFacing)
        myData = {
            "description": "Blockchain Bricks",
            "external_url": "https://Blockchain-Bricks.arkodeep12.repl.co/",
            "image": "Image",
            "name": "Arkodeep Chatterjee",
            "attributes": [
                {
                    "trait_type": "Address with Pin",
                    "value": flatAddress
                },
                {
                    "trait_type": "Floor Number",
                    "value": flatFloor
                },
                {
                    "trait_type": "Flat Number",
                    "value": flatFlat
                },
                {
                    "trait_type": "Project Name",
                    "value": flatProject
                },
                {
                    "trait_type": "Cluster",
                    "value": flatCluster
                },
                {
                    "trait_type": "Building Number",
                    "value": flatBuilding
                },
                {
                    "trait_type": "Owner Name",
                    "value": flatOwner
                },
                {
                    "trait_type": "Super Area",
                    "value": flatSuper
                },
                {
                    "trait_type": "Carpet Area",
                    "value": flatCarpet
                },
                {
                    "trait_type": "Facing",
                    "value": flatFacing
                },
                {
                    "trait_type": "Parking",
                    "value": "Covered",
                }
            ]
        }

        with open(flatOwner+".json", "w") as f:
            json.dump(myData, f, indent=4)

        print("data loaded into json file")
        return redirect("/flat.html")
    else:
        return render_template("/flat.html")

@app.route("/land.html", methods=["POST","GET"])
def landPage():
    if request.method=="POST":
        landDetail = request.form
        landPlot = landDetail["plot"]
        landCountry = landDetail["country"]
        landState = landDetail["state"]
        landMouza = landDetail["mouza"]
        landDag = landDetail["dag"]
        landBuilder = landDetail["builder"]
        landChauhaddi = landDetail["chauhaddi"]
        landCoordinate = landDetail["coordinate"]
        landDeed = landDetail["deed"]
        landRecord = landDetail["record"]
        landOwner = landDetail["owner"]
        landLength = landDetail["length"]
        landBreadth = landDetail["breadth"]
        print(landPlot,landCountry,landState,landMouza,landDag,landBuilder,landChauhaddi,landCoordinate,landDeed,landRecord,landOwner,landLength,landBreadth)
        myData = {
            "description": "Blockchain Bricks",
            "external_url": "https://Blockchain-Bricks.arkodeep12.repl.co/",
            "image": "Image",
            "name": "Arkodeep Chatterjee",
            "attributes": [
                {
                    "trait_type": "Plot Number",
                    "value": landPlot
                },
                {
                    "trait_type": "Country",
                    "value": landCountry
                },
                {
                    "trait_type": "State",
                    "value": landState
                },
                {
                    "trait_type": "Mouza",
                    "value": landMouza
                },
                {
                    "trait_type": "Dag Number",
                    "value": landDag
                },
                {
                    "trait_type": "Builder",
                    "value": landBuilder
                },
                {
                    "trait_type": "Chauhaddi",
                    "value": landChauhaddi
                },
                {
                    "trait_type": "Google Coordinate",
                    "value": landCoordinate
                },
                {
                    "trait_type": "Deed Number",
                    "value": landDeed
                },
                {
                    "trait_type": "Record of Rights",
                    "value": landRecord
                },
                {
                    "trait_type": "Owner Name",
                    "value": landOwner
                },
                {
                    "trait_type": "Length of Land",
                    "value": landLength
                },
                {
                    "trait_type": "Breadth of Land",
                    "value": landBreadth
                }
            ]
        }

        with open(landOwner + ".json", "w") as f:
            json.dump(myData, f, indent=4)

        print("data loaded into json file")
        return redirect("/land.html")
    else:
        return render_template("/land.html")

@app.route("/login.html")
def loginPage():
    return render_template("login.html")

@app.route("/phNo.html")
def phNoPage():
    return render_template("phNo.html")

@app.route("/property.html")
def propertyPage():
    return render_template("property.html")

@app.route("/sell.html")
def sellPage():
    return render_template("sell.html")

@app.route("/sellWhat.html")
def sellWhatPage():
    return render_template("sellWhat.html")

@app.route("/signUp.html")
def signUpPage():
    return render_template("signUp.html")

@app.route("/wallet.html")
def walletPage():
    return render_template("wallet.html")

if __name__=="__main__":
    app.run(debug=True)