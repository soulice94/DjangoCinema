class ModelHelper:
    @staticmethod
    def fromQueryToList(model_data):
        records = []
        for record in model_data:
            records.append(record)
        return records

    @staticmethod
    def retrieveAll(model):
        response = {
            'records': ModelHelper.fromQueryToList(model.objects.all().values())
        }
        return response
