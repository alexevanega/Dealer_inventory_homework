from flask import Blueprint
from flask import render_template

inv  = Blueprint('inventory', __name__, template_folder='inv_templates')

@inv.route('/inventory')
def inventory_page():
    return render_template('data_list.html')