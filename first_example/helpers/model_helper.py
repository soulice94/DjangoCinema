from django.forms.models import model_to_dict
import constants

class ModelHelper:
    @staticmethod
    def from_query_to_list(model_data):
        records = []
        for record in model_data:
            records.append(record)
        return records

    @staticmethod
    def retrieve_all(model):
        response = {
            'records': ModelHelper.from_query_to_list(model.objects.all().values())
        }
        return response

    @staticmethod
    def need_json_body(method):
        return ((method == constants.POST_METHOD) | (method == constants.PUT_METHOD))

    @staticmethod
    def movie_serializer(movie):
        actors=ModelHelper.from_query_to_list(movie.actors.all().values())
        return {
            'name': movie.name,
            'genre': model_to_dict(movie.genre),
            'actors': actors
        }
    
    @staticmethod
    def retrieve_all_movies(Model):
        movies = Model.objects.all()
        records = []
        for movie in movies:
            records.append(ModelHelper.movie_serializer(movie))
        return { 'records': records }
