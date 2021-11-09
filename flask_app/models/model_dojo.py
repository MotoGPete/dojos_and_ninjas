# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask_app.models import model_ninja
DATABASE = "dojod_and_ninjas"

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def get_dojo_ninjas( cls , data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojos_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db( query , data )

        dojo = cls( results[0] )
        for row in results:

            ninja_data = {
                "id" : row["ninjas.id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "dojos_id"  : row["dojos_id"],
                "created_at"   : row["ninjas.created_at"],
                "updated_at"   : row["ninjas.updated_at"]
            }
            dojo.ninjas.append(model_ninja.Ninja( ninja_data ) )
        return dojo

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def create(cls, data ):
        query = 'INSERT INTO dojos ( name , created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );'
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def get_one(cls, data:dict):
        query = 'SELECT * FROM dojos WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    @classmethod
    def update_one(cls, data):
        query = "UPDATE dojos SET name = %(name)s  WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)



    @classmethod
    def delete_one(cls, data:dict):
        query = 'DELETE FROM dojos WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)
