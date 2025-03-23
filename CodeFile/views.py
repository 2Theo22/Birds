from flask import Blueprint, render_template, request
from .birdsearch import bird_search  # Importieren Sie die Funktion aus birdsearch.py

views = Blueprint('views', __name__)

# Route to home
@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        search_query = request.form.get('search1')
        success, results = bird_search(search_query)
        if success:
            return render_template("home.html", birds=results, search_query=search_query)
        else:
            return render_template("home.html", error="No results found", search_query=search_query)

    return render_template("home.html")

#@views.route('/parrots')
#def parrots():
#   return render_template("parrot.html")

#@views.route('/species', methods=['GET', 'POST'])
#def species():
#    species = None
#    if request.method == 'POST':
#        species = request.form.get('species')

#    return render_template("species.html", text="Testing", species=species)

# Corrected route decorator
#@views.route('/continent', methods=['GET'])
#def continent():
#    return render_template("continent.html")
