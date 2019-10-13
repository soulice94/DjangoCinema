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

    def need_json_body(method):
        return ((method == constants.POST_METHOD) | (method == constants.PUT_METHOD))
