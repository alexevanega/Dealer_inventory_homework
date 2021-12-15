from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_required

from .forms import addToInventory, removeInventory, updateListingForm

from cd_app.models import Inventory, Reserve

inv  = Blueprint('inventory', __name__, template_folder='inv_templates')

from cd_app.models import db

import requests as r

@inv.route('/inventory')
def inventory_page():
    inventory = Inventory.query.all()
    if inventory == None:
        return render_template('add_to.html')
    return render_template('data_list.html', inventory=inventory, current=current_user.id, title='Inventory Listing')

@inv.route('/inventory/chucknorris_add')
def chuckJokes_add():
    api= r.get('https://api.chucknorris.io/jokes/random')
    the_jokes = api.json()
    jokes = the_jokes['value']
    return render_template('add_chuckjokes.html', jokes=jokes)

@inv.route('/inventory/chucknorris_remove')
def chuckJokes_remove():
    api= r.get('https://api.chucknorris.io/jokes/random')
    the_jokes = api.json()
    jokes = the_jokes['value']
    return render_template('remove_chuckjokes.html', jokes=jokes)

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
            swap = Reserve(image,vin_num,year,make,model,description)
            db.session.add(swap)
            db.session.commit()

            return redirect(url_for('inventory.chuckJokes_add'))
    return render_template('add_to.html',form=add_form, title='Add To Inventory')

@inv.route('/inventory/item_remove', methods = ['GET','POST'])
@login_required
def removeInv():
    remove_form=removeInventory()
    id = remove_form.id.data
    item=Inventory.query.filter_by(id=id).first()


    if request.method == 'POST':
        if remove_form.validate():

            if item.user_id != current_user.id:
                return render_template('remove.html',form=remove_form,title='Remove From Inventory')

            db.session.delete(item)
            db.session.commit()

            return redirect(url_for('inventory.chuckJokes_remove'))
    return render_template('remove.html',form=remove_form,title='Remove From Inventory')

@inv.route('/inventory/retrieve')
@login_required
def retrieveReserve():
    rr=Reserve.query.all()
    return render_template('retrieve.html',rr=rr,title='Reserve Database')

@inv.route('/inventory/reserve_vehicle<int:id>')
@login_required
def vehicleListingPage(id):
    vehicle = Reserve.query.filter_by(id=id).first()
    if vehicle is None:
        return redirect(url_for('inventory.retrieveReserve'))
    return render_template('reserve_vehicle.html', v=vehicle)

@inv.route('/inventory/my_vehicle/<int:id>')
@login_required
def myVehiclePage(id):
    vehicle1 = Inventory.query.filter_by(id=id).first()

    return render_template('my_vehicle.html', v=vehicle1)

@inv.route('/inventory/retrieve/<int:id>', methods=["GET","POST"])
@login_required
def retrieveReserveListing(id):
    listing=Reserve.query.filter_by(id=id).first()

    retrieve=Inventory(listing.image,listing.vin_num,listing.year,listing.make,listing.model,listing.description,current_user.id)

    db.session.add(retrieve)
    db.session.commit()
    return redirect(url_for('inventory.chuckJokes_add'))

@inv.route('/inventory/update/<int:id>', methods=['GET','POST'])
@login_required
def updateListing(id):
    update_form=updateListingForm()
    listing=Inventory.query.filter_by(id=id).first()

    if request.method == 'POST':
        if update_form.validate():

            image = update_form.image.data
            vin_num = update_form.vin_num.data
            year = update_form.year.data
            make = update_form.make.data
            model = update_form.model.data
            description = update_form.description.data

            if not image:
                image=listing.image
            if not vin_num:
                vin_num=listing.vin_num
            if not year:
                year=listing.year
            if not make:
                make=listing.make
            if not model:
                model=listing.model
            if not description:
                description=listing.description
                
            listing.image=image
            listing.vin_num=vin_num
            listing.year=year
            listing.make=make
            listing.model=model
            listing.description=description
            db.session.commit()

            return redirect(url_for('inventory.myVehiclePage', id=id))
    return render_template('update.html', form=update_form, title='Update Listing')




