from cave_serialization_helpers import *


class Serializer:
    def __init__(self, session_data):
        self.session_data = session_data
        self.key_serializers = [
            key_serializer(session_data)
            for key_serializer in TOP_LEVEL_KEY_SERIALIZERS
            if key_serializer.primary_key in session_data
        ]

    def include_required_top_level_keys(self):
        for top_level_key in ["appBar", "dashboards", "maps"]:
            if top_level_key not in self.session_data:
                self.session_data[top_level_key] = {"data": {}}

    def perform(self):
        self.include_required_top_level_keys()
        for key_serializer in self.key_serializers:
            key_serializer.perform()
        return self.session_data


class Deserializer:
    def __init__(self, session_data):
        self.session_data = session_data
        self.key_deserializers = [
            key_deserializer(session_data)
            for key_deserializer in TOP_LEVEL_KEY_DESERIALIZERS
            if key_deserializer.primary_key in session_data
        ]

    def perform(self):
        for key_deserializer in self.key_deserializers:
            key_deserializer.perform()
        return self.session_data
