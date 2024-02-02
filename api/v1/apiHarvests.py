# DESCRIPTION
# api routes for database harvests data

from flask import request, Blueprint
import json

apiHarvests = Blueprint('apiHarvests', __name__, url_prefix='/api/v1/harvests')

@apiHarvests.route('/get_total_bales/<int:farm_id>', methods=['GET'])
def get_total_bales(farm_id):
    from model.db import DBConfig

    connection = DBConfig()
    connection.init()

    connection.cursor.execute(f"""
    select
        f.name as farm
    ,	sum(h.bale_amount) as Bales_Total
    from harvest h 
    join field fd
    on h.field_id = fd.field_id 
    join farm f 
    on fd.farm_id = f.farm_id
    where f.farm_id = {farm_id}
    group by f.farm_id;
    """)

    results = connection.cursor.fetchall()

    return json.dumps(results, indent=4, sort_keys=True, default=str), 200, {'content-type': 'application/json'}

@apiHarvests.route('/get_field_production/<int:farm_id>')
def get_field_production(farm_id):
    from model.db import DBConfig

    connection = DBConfig()
    connection.init()

    connection.cursor.execute(f"""
    select 
        fd.name as field
    ,	sum(h.bale_amount) as bales_total
    from harvest h
    join field fd
    on h.field_id = fd.field_id 
    join farm f
    on fd.farm_id = f.farm_id
    where f.farm_id = {farm_id}
    group by fd.field_id;
    """)

    results = connection.cursor.fetchall()

    return json.dumps(results, indent=4, sort_keys=True, default=str), 200, {'content-type': 'application/json'}
