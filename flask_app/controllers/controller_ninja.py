from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import model_ninja, model_dojo


# @app.route('/')
# def index():
#     # ninjas = model_ninja.ninja.get_all()
#     return render_template('index.html')
# # # new ninja form page

@app.route('/ninja/new')
def new_ninja():
    dojos = model_dojo.Dojo.get_all()
    return render_template('ninjas.html', dojos=dojos)

#add new ninja to database
@app.route('/ninja/create', methods=["post"])
def create_ninja():
    id = model_ninja.Ninja.create(request.form)
    print(id)
    return redirect('/dojos')

# show ninja info
# @app.route('/ninja/<int:id>')
# def show_ninja(id):
#     ninja = model_ninja.Ninja.get_one({'id': id})
#     return render_template('ninja_show.html', ninja = ninja)

#form for edit ninja
# @app.route('/ninja/<int:id>/edit')
# def edit_ninja(id):
#     context = {
#         "ninja" : model_ninja.Ninja.get_one({'id': id})
#     }
    
#     return render_template('ninja_edit.html', **context)

#update the ninja(do the edit)
# @app.route('/ninja/<int:id>/update', methods=["post"])
# def update_ninja(id):
#     data = {
#         **request.form,
#         "id": id
#     }
#     model_ninja.Ninja.update_one(data)
#     return redirect(f"/ninja/{id}")


#delete ninja
# @app.route('/ninja/<int:id>/delete')
# def delete_ninja(id):
#     model_ninja.Ninja.delete_one({'id': id})
#     return redirect('/')@app.route('/ninja/<int:id>/update', methods=["post"])

