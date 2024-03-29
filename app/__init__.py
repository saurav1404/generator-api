# app/__init__.py
import subprocess 

from flask_api import FlaskAPI
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from instance.settings import APP_SETTINGS
# local import
from instance.config import app_config
from flask import request, jsonify, abort

# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name = None):
    from app.models import Config, Workflow, Rules, Menu, Swagger
    
    app = FlaskAPI(__name__, instance_relative_config=True)
    CORS(app)
    if config_name is None:
        app.config.from_object(app_config[APP_SETTINGS])
    else:
        app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/api/config/', methods=['POST', 'GET'])
    @cross_origin()
    def configlist():
        if request.method == "POST":
            id = str(request.data.get('id', ''))
            if id:
                config = Config(id= id, 
                                title = request.data.get("title"), 
                                columns = request.data.get("columns"), 
                                properties = request.data.get("properties"))
                config.save()
                response = jsonify({
                    'id': config.id,
                    'title': config.title,
                    'columns': config.columns,
                    'properties': config.properties,
                    'date_created': config.date_created,
                    'date_modified': config.date_modified
                })
                response.status_code = 201
                return response
        else:
            # GET
            configs = Config.get_all()
            results = []

            for config in configs:
                obj = {
                    'count': config.count,
                    'id': config.id,
                    'title': config.title,
                    'columns': config.columns,
                    'properties': config.properties,
                    'date_created': config.date_created,
                    'date_modified': config.date_modified
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response
        
    @app.route('/api/config/<string:id>', methods=['GET', 'PUT', 'DELETE'])
    @cross_origin()
    def configlist_manipulation(id, **kwargs):
        # retrieve a config using it's ID
        config = Config.query.filter_by(id=id).first()
        if not config:
            # Raise an HTTPException with a 404 not found status code
            abort(404)

        if request.method == 'DELETE':
            config.delete()
            return {
            "message": "config {} deleted successfully".format(config.id) 
         }, 200

        elif request.method == 'PUT':
            id = str(request.data.get('id', ''))
            config.id = id
            config.title = request.data.get("title")
            config.columns = request.data.get("columns")
            config.properties = request.data.get("properties")
            config.save()
            response = jsonify({
                'id': config.id,
                'title': config.title,
                'columns': config.columns,
                'properties': config.properties,
                'date_created': config.date_created,
                'date_modified': config.date_modified
            })
            response.status_code = 200
            return response
        else:
            # GET
            response = jsonify({
                'count': config.count,
                'id': config.id,
                'title': config.title,
                'columns': config.columns,
                'properties': config.properties,
                'date_created': config.date_created,
                'date_modified': config.date_modified
            })
            response.status_code = 200
            return response
        
    @app.route('/api/workflow/', methods=['POST', 'GET'])
    @cross_origin()
    def workflowlist():
        if request.method == "POST":
            RelId = str(request.data.get('RelId', ''))
            if RelId:
                workflow = Workflow(RelId = request.data.get("RelId"), 
                                    EntityType = request.data.get("EntityType"), 
                                    DseDsCode = request.data.get("DseDsCode"),
                                    OdsStatus = request.data.get("OdsStatus"),
                                    GplStatus = request.data.get("GplStatus"),
                                    GblStatus = request.data.get("GblStatus"),
                                    GrlStatus = request.data.get("GrlStatus"),
                                    DetStatus = request.data.get("DetStatus"),
                                    GckStatus = request.data.get("GckStatus"))
                workflow.save()
                response = jsonify({
                    'RelId': workflow.RelId,
                    'EntityType': workflow.EntityType,
                    'DseDsCode': workflow.DseDsCode,
                    'OdsStatus': workflow.OdsStatus,
                    'GplStatus': workflow.GplStatus,
                    'GblStatus': workflow.GblStatus,
                    'GrlStatus': workflow.GrlStatus,
                    'DetStatus': workflow.DetStatus,
                    'GckStatus': workflow.GckStatus,
                    'date_created': workflow.date_created,
                    'date_modified': workflow.date_modified
                })
                response.status_code = 201
                return response
        else:
            # GET
            workflows = Workflow.get_all()
            results = []

            for workflow in workflows:
                obj = {
                    'Id': workflow.Id,
                    'RelId': workflow.RelId,
                    'EntityType': workflow.EntityType,
                    'DseDsCode': workflow.DseDsCode,
                    'OdsStatus': workflow.OdsStatus,
                    'GplStatus': workflow.GplStatus,
                    'GblStatus': workflow.GblStatus,
                    'GrlStatus': workflow.GrlStatus,
                    'DetStatus': workflow.DetStatus,
                    'GckStatus': workflow.GckStatus,
                    'date_created': workflow.date_created,
                    'date_modified': workflow.date_modified
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response
        
    @app.route('/api/workflow/<int:Id>', methods=['GET', 'PUT', 'DELETE'])
    @cross_origin()
    def workflowlist_manipulation(Id, **kwargs):
        # retrieve a workflow using it's ID
        workflow = Workflow.query.filter_by(Id=Id).first()
        if not workflow:
            # Raise an HTTPException with a 404 not found status code
            abort(404)

        if request.method == 'DELETE':
            workflow.delete()
            return {
            "message": "workflow {} deleted successfully".format(workflow.RelId) 
         }, 200

        elif request.method == 'PUT':
            Id = str(request.data.get('Id', ''))
            workflow.Id = Id
            workflow.RelId = request.data.get("RelId")
            workflow.EntityType = request.data.get("EntityType")
            workflow.DseDsCode = request.data.get("DseDsCode")
            workflow.OdsStatus = request.data.get("OdsStatus")
            workflow.GplStatus = request.data.get("GplStatus")
            workflow.GblStatus = request.data.get("GblStatus")
            workflow.GrlStatus = request.data.get("GrlStatus")
            workflow.DetStatus = request.data.get("DetStatus")
            workflow.GckStatus = request.data.get("GckStatus")
            workflow.save()
            response = jsonify({
                'Id': workflow.Id,
                'RelId': workflow.RelId,
                'EntityType': workflow.EntityType,
                'DseDsCode': workflow.DseDsCode,
                'OdsStatus': workflow.OdsStatus,
                'GplStatus': workflow.GplStatus,
                'GblStatus': workflow.GblStatus,
                'GrlStatus': workflow.GrlStatus,
                'DetStatus': workflow.DetStatus,
                'GckStatus': workflow.GckStatus,
                'date_created': workflow.date_created,
                'date_modified': workflow.date_modified
            })
            response.status_code = 200
            return response
        else:
            # GET
            response = jsonify({
                'Id': workflow.Id,
                'RelId': workflow.RelId,
                'EntityType': workflow.EntityType,
                'DseDsCode': workflow.DseDsCode,
                'OdsStatus': workflow.OdsStatus,
                'GplStatus': workflow.GplStatus,
                'GblStatus': workflow.GblStatus,
                'GrlStatus': workflow.GrlStatus,
                'DetStatus': workflow.DetStatus,
                'GckStatus': workflow.GckStatus,
                'date_created': workflow.date_created,
                'date_modified': workflow.date_modified
            })
            response.status_code = 200
            return response
        
    @app.route('/rules/', methods=['POST', 'GET'])
    @cross_origin()
    def ruleslist():
        if request.method == "POST":
            Name = str(request.data.get('Name', ''))
            if Name:
                rule = Rules(Name = request.data.get("Name"), 
                             Type = request.data.get("Type"), 
                             Salary = request.data.get("Salary"), 
                             Age = request.data.get("Age"))
                rule.save()
                response = jsonify({
                    'Name': rule.Name,
                    'Type': rule.Type,
                    'Salary': rule.Salary,
                    'Age': rule.Age,
                    'date_created': rule.date_created,
                    'date_modified': rule.date_modified
                })
                response.status_code = 201
                return response
        else:
            # GET
            rules = Rules.get_all()
            results = []

            for rule in rules:
                obj = {
                    'Name': rule.Name,
                    'Type': rule.Type,
                    'Salary': rule.Salary,
                    'Age': rule.Age,
                    'date_created': rule.date_created,
                    'date_modified': rule.date_modified
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response
        
    @app.route('/rules/<string:Name>', methods=['GET', 'PUT', 'DELETE'])
    @cross_origin()
    def ruleslist_manipulation(Name, **kwargs):
        # retrieve a rules using it's ID
        rule = Rules.query.filter_by(Name=Name).first()
        if not rule:
            # Raise an HTTPException with a 404 not found status code
            abort(404)

        if request.method == 'DELETE':
            rule.delete()
            return {
            "message": "rule {} deleted successfully".format(rule.Name) 
         }, 200

        elif request.method == 'PUT':
            Name = str(request.data.get('Name', ''))
            rule.Name = Name
            rule.save()
            response = jsonify({
                'Name': rule.Name,
                'Type': rule.Type,
                'Salary': rule.Salary,
                'Age': rule.Age,
                'date_created': rule.date_created,
                'date_modified': rule.date_modified
            })
            response.status_code = 200
            return response
        else:
            # GET
            response = jsonify({
                'Name': rule.Name,
                'Type': rule.Type,
                'Salary': rule.Salary,
                'Age': rule.Age,
                'date_created': rule.date_created,
                'date_modified': rule.date_modified
            })
            response.status_code = 200
            return response
        
    @app.route('/api/menu/', methods=['POST', 'GET'])
    @cross_origin()
    def menulist():
        if request.method == "POST":
            id = str(request.data.get('id', ''))
            if id:
                menu = Menu(id= id, 
                                title = request.data.get("title"), 
                                nodes = request.data.get("nodes"), 
                                label = request.data.get("label"))
                menu.save()
                response = jsonify({
                    'id': menu.id,
                    'title': menu.title,
                    'nodes': menu.nodes,
                    'label': menu.label,
                    'date_created': menu.date_created,
                    'date_modified': menu.date_modified
                })
                response.status_code = 201
                return response
        else:
            # GET
            menus = Menu.get_all()
            results = []

            for menu in menus:
                obj = {
                    'count': menu.count,
                    'id': menu.id,
                    'title': menu.title,
                    'nodes': menu.nodes,
                    'label': menu.label,
                    'date_created': menu.date_created,
                    'date_modified': menu.date_modified
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response
        
    @app.route('/api/menu/<string:id>', methods=['GET', 'PUT', 'DELETE'])
    @cross_origin()
    def menulist_manipulation(id, **kwargs):
        # retrieve a menu using it's ID
        menu = Menu.query.filter_by(id=id).first()
        if not menu:
            # Raise an HTTPException with a 404 not found status code
            abort(404)

        if request.method == 'DELETE':
            menu.delete()
            return {
            "message": "menu {} deleted successfully".format(menu.id) 
         }, 200

        elif request.method == 'PUT':
            id = str(request.data.get('id', ''))
            menu.id = id
            menu.title = request.data.get("title")
            menu.nodes = request.data.get("nodes")
            menu.label = request.data.get("label")
            menu.save()
            response = jsonify({
                'id': menu.id,
                'title': menu.title,
                'nodes': menu.nodes,
                'label': menu.label,
                'date_created': menu.date_created,
                'date_modified': menu.date_modified
            })
            response.status_code = 200
            return response
        else:
            # GET
            response = jsonify({
                'count': menu.count,
                'id': menu.id,
                'title': menu.title,
                'nodes': menu.nodes,
                'label': menu.label,
                'date_created': menu.date_created,
                'date_modified': menu.date_modified
            })
            response.status_code = 200
            return response
        
    @app.route('/api/swagger/', methods=['POST', 'GET'])
    @cross_origin()
    def swaggerlist():
        if request.method == "POST":
            swagger = str(request.data.get('swagger', ''))
            if swagger:
                swagger = Swagger(swagger= swagger, 
                                info = request.data.get("info"), 
                                host = request.data.get("host"), 
                                basePath = request.data.get("basePath"),
                                schemes = request.data.get("schemes"), 
                                paths = request.data.get("paths"), 
                                definitions = request.data.get("definitions"))
                                
                swagger.save()
                response = jsonify({
                    'swagger': swagger.swagger,
                    'info': swagger.info,
                    'host': swagger.host,
                    'basePath': swagger.basePath,
                    'schemes': swagger.schemes,
                    'paths': swagger.paths,
                    'definitions': swagger.definitions,
                    'date_created': swagger.date_created,
                    'date_modified': swagger.date_modified
                })
                response.status_code = 201
                return response
        else:
            # GET
            swaggers = Swagger.get_all()
            swagger = swaggers[0];
            obj = {
                'swagger': swagger.swagger,
                'info': swagger.info,
                'host': swagger.host,
                'basePath': swagger.basePath,
                'schemes': swagger.schemes,
                'paths': swagger.paths,
                'definitions': swagger.definitions,
                'date_created': swagger.date_created,
                'date_modified': swagger.date_modified
            }
            response = jsonify(obj)
            response.status_code = 200
            return response
        
    @app.route('/api/swagger/<string:swagger>', methods=['GET', 'PUT', 'DELETE'])
    @cross_origin()
    def swaggerlist_manipulation(swagger, **kwargs):
        # retrieve a menu using it's ID
        swagger = Swagger.query.filter_by(swagger=swagger).first()
        if not swagger:
            # Raise an HTTPException with a 404 not found status code
            abort(404)

        if request.method == 'DELETE':
            swagger.delete()
            return {
            "message": "swagger {} deleted successfully".format(swagger.swagger) 
         }, 200

        elif request.method == 'PUT':
            swagger = str(request.data.get('swagger', ''))
            swagger.swagger = swagger
            swagger.info = request.data.get("info")
            swagger.host = request.data.get("host")
            swagger.basePath = request.data.get("basePath")
            swagger.schemes = request.data.get("schemes")
            swagger.paths = request.data.get("paths")
            swagger.definitions = request.data.get("definitions")
            swagger.save()
            response = jsonify({
                'swagger': swagger.swagger,
                'info': swagger.info,
                'host': swagger.host,
                'basePath': swagger.basePath,
                'schemes': swagger.schemes,
                'paths': swagger.paths,
                'definitions': swagger.definitions,
                'date_created': swagger.date_created,
                'date_modified': swagger.date_modified
            })
            response.status_code = 200
            return response
        else:
            # GET
            response = jsonify({
                'swagger': swagger.swagger,
                'info': swagger.info,
                'host': swagger.host,
                'basePath': swagger.basePath,
                'schemes': swagger.schemes,
                'paths': swagger.paths,
                'definitions': swagger.definitions,
                'date_created': swagger.date_created,
                'date_modified': swagger.date_modified
            })
            response.status_code = 200
            return response
     
    @app.route('/api/command/', methods=['POST'])
    @cross_origin()
    def runcommand():
        commands = request.data.get("commands")
        if commands:
            for command in commands:
                subprocess.call(command, shell=True)
            response = jsonify()
            response.status_code = 201
            return response
           
    return app