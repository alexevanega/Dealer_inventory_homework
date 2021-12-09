from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_required

from .forms import addToInventory

from cd_app.models import Inventory

inv  = Blueprint('inventory', __name__, template_folder='inv_templates')

from cd_app.models import db

@inv.route('/inventory')
def inventory_page():
    inventory = Inventory.query.all()
    return render_template('data_list.html')

@inv.route('/inventory/add_to_inventory', methods=['GET','POST'])
def addInv():
    add_form = addToInventory()
    if request.method == 'POST':
        if add_form.validate():

            image = add_form.image.data
            vin_num = add_form.vin_num.data
            year = add_form.year.data
            make = add_form.make.data
            model = add_form.model.data
            description = add_form.description.data

            item = Inventory(image,vin_num,year,make,model,description,current_user.id)
            db.session.add(item)
            db.session.commit()

            return redirect(url_for('homePage'))
    return render_template('add_to.html')