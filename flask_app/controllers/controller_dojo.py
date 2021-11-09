from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import model_dojo

@app.route('/dojos')
def index():
    dojos = model_dojo.Dojo.get_all()
    return render_template('dojos.html', dojos = dojos)
# new dojo form page

# @app.route('/dojo/new')
# def new_dojo():
    
#     return render_template('dojo_new.html', )



#add new dojo to database
@app.route('/dojo/create', methods=["post"])
def create_dojo():
    id = model_dojo.Dojo.create(request.form)
    print(id)
    return redirect('/dojos')

# show dojo info
@app.route('/dojo/<int:id>')
def show_dojo(id):
    dojo = model_dojo.Dojo.get_dojo_ninjas({'id': id})
    return render_template('dojo_show.html', dojo = dojo)

# form for edit dojo
# @app.route('/dojo/<int:id>/edit')
# def edit_dojo(id):
#     context = {
#         "dojo" : model_dojo.Dojo.get_one({'id': id})
#     }
    
#     return render_template('dojo_edit.html', **context)

#update the dojo(do the edit)
# @app.route('/dojo/<int:id>/update', methods=["post"])
# def update_dojo(id):
#     data = {
#         **request.form,
#         "id": id
#     }
#     model_dojo.Dojo.update_one(data)
#     return redirect(f"/dojo/{id}")


#delete dojo
@app.route('/dojo/<int:id>/delete')
def delete_dojo(id):
    model_dojo.Dojo.delete_one({'id': id})
    return redirect('/dojos')