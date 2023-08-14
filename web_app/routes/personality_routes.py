# this is the "web_app/routes/personality_routes.py" file ...
from flask import Blueprint, request, render_template, redirect, flash
from app.personality import get_activities

personality_routes = Blueprint("personality_routes", __name__)
@personality_routes.route("/personality/form")
def personality_form():
    print("PERSONALITY FORM...")
    return render_template("personality_form.html")
@personality_routes.route("/personality/dashboard", methods=["GET", "POST"])
def personality_dashboard():
    print("PERSONALITY DASHBOARD...")
    request_data = dict(request.form)
    print("FORM DATA:", request_data)
    type1 = request_data.get("type1")
    type2 = request_data.get("type2")
    try:
        results = get_activities(type1,type2)
        #flash("Fetched Real-time Market Data!", "success")
        return render_template("personality_dashboard.html", results=results)
    except Exception as err:
        print('OOPS', err)
        #flash("Market Data Error. Please check your symbol and try again!", "danger")
        return redirect("/personality/form")







