from models import Delivery, DeliverySchema, Shippment, ShippmentSchema
from main import db, app
from flask import request, jsonify, render_template
from datetime import datetime

delivery_schema = DeliverySchema()
deliveries_schema = DeliverySchema(many=True)

shippment_schema = ShippmentSchema()
shippments_schema = ShippmentSchema(many=True)

# Main landing page
@app.route("/")
def homepage():
    """
    Render the homepage template on the / route
    """
    try:
        return render_template('index.html', title="Welcome")
    except:
        return 'Cannot load file specified'

# endpoint to create new delivery entry
@app.route("/delivery", methods=["POST"])
def add_delivery():
    businesstype = request.json['businesstype']
    clientname = request.json['clientname']
    order_ID = request.json['order_ID']
    comment = request.json['comment']

    new_delivery = Delivery(businesstype, clientname, order_ID, comment)

    db.session.add(new_delivery)
    db.session.commit()

    # return jsonify(new_delivery)
    return '{}'.format(new_delivery)
    # return 'user added ' + name

# endpoint to show all delivery entries
@app.route("/delivery", methods=["GET"])
def get_delivery():
    all_delivery = Delivery.query.all()
    print(all_delivery)
    # # May use the following to return other JSON format structure
    # results = {}
    # for delivery in all_delivery:
    #     results.update({
    #         delivery.id:{
    #             'name': delivery.name,
    #             'description': delivery.description
    #             }
    #         }
    #     )
    # return jsonify(results)
    result = deliveries_schema.dump(all_delivery)
    return jsonify(result.data)

# endpoint to get delivery entry detail by order id
@app.route("/delivery/<id>", methods=["GET"])
def delivery_detail(id):
    delivery = Delivery.query.filter_by(order_ID=id).first()
    return delivery_schema.jsonify(delivery)

# endpoint to update delivery entry by order id for businesstype, clientname, and comment
@app.route("/delivery/<id>", methods=["PUT", "POST"])
def delivery_update(id):
    delivery = Delivery.query.filter_by(order_ID=id).first()
    try:
        businesstype = request.json['businesstype']
        delivery.businesstype = businesstype
    except:
        pass
    try:
        clientname = request.json['clientname']
        delivery.clientname = clientname    
    except:
        pass
    try:
        comment = '\ new comment' + request.json['comment']
        delivery.comment += comment
    except:
        pass
    delivery.updated_at = datetime.utcnow()
    
    db.session.commit()
    return delivery_schema.jsonify(delivery)

# endpoint to delete delivery entry by order id
@app.route("/delivery/<id>", methods=["DELETE"])
def delivery_delete(id):
    delivery = Delivery.query.filter_by(order_ID=id).first()
    db.session.delete(delivery)
    db.session.commit()

    return delivery_schema.jsonify(delivery)

# endpoint to create new shippment entry
@app.route("/shippment", methods=["POST"])
def add_shippment():
    ship_ID = request.json['ship_ID']
    contact_info = request.json['contact_info']
    ship_area = request.json['ship_area']
    ship_district = request.json['ship_district']
    driver = request.json['driver']
    car_type = request.json['car_type']
    car_ID = request.json['car_ID']
    is_elevator = request.json['is_elevator']
    floors_byhand = request.json['floors_byhand']
    amount_collect = request.json['amount_collect']
    comment = request.json['comment']

    print(ship_ID, contact_info, ship_area, ship_district, driver, car_type, car_ID, is_elevator, floors_byhand, amount_collect, comment)
    new_shippment = Shippment(ship_ID, contact_info, ship_area, ship_district, driver, car_type, car_ID, is_elevator, floors_byhand, amount_collect, comment)

    db.session.add(new_shippment)
    db.session.commit()

    # return jsonify(new_delivery)
    return '{}'.format(new_shippment)
    # return 'user added ' + name

# endpoint to show all shippment entries
@app.route("/shippment", methods=["GET"])
def get_shippment():
    all_shippments = Shippment.query.all()
    print(all_shippments)
    result = shippments_schema.dump(all_shippments)
    return jsonify(result.data)

# endpoint to get shippment entry detail by ship id
@app.route("/shippment/<id>", methods=["GET"])
def shippment_detail(id):
    shippment = Shippment.query.filter_by(ship_ID=id).first()
    return shippment_schema.jsonify(shippment)

# endpoint to update shippment entry by order id
@app.route("/shippment/<id>", methods=["PUT", "POST"])
def shippment_update(id):
    shippment = Shippment.query.filter_by(ship_ID=id).first()

    try:
        contact_info = request.json['contact_info']
        shippment.contact_info = contact_info
    except:
        pass

    try:
        ship_area = request.json['ship_area']
        shippment.ship_area = ship_area
    except:
        pass

    try:
        ship_district = request.json['ship_district']
        shippment.ship_district = ship_district
    except:
        pass

    try:
        driver = request.json['driver']
        shippment.driver = driver
    except:
        pass

    try:
        car_type = request.json['car_type']
        shippment.car_type = car_type
    except:
        pass

    try:
        car_ID = request.json['car_ID']
        shippment.car_ID = car_ID
    except:
        pass

    try:
        is_elevator = request.json['is_elevator']
        shippment.is_elevator = is_elevator
    except:
        pass

    try:
        floors_byhand = request.json['floors_byhand']
        shippment.floors_byhand = floors_byhand
    except:
        pass

    try:
        amount_collect = request.json['amount_collect']
        shippment.amount_collect = amount_collect
    except:
        pass

    try:
        comment = '/ Comment: ' + request.json['comment']
        shippment.comment += comment
    except:
        pass

    db.session.commit()
    return shippment_schema.jsonify(shippment)

# endpoint to delete delivery entry by order id
@app.route("/shippment/<id>", methods=["DELETE"])
def shippment_delete(id):
    shippment = Shippment.query.filter_by(ship_ID=id).first()
    db.session.delete(shippment)
    db.session.commit()

    return shippment_schema.jsonify(shippment)
