from cave_serializer_utils import *


class TopLevelKeySerializer:
    def __init__(self, json):
        self.json = json

    def perform(self):
        pass


class ArcsNodesGeosSerializer(TopLevelKeySerializer):
    def convert_color_by_options(self):
        for type_data in self.json["types"].values():
            color_by_options = type_data.pop("colorByOptions")
            start_gradient_color = type_data.pop("startGradientColor")
            end_gradient_color = type_data.pop("endGradientColor")
            type_data["colorByOptions"] = {
                option: {
                    "min": 0,
                    "max": 0,  # TODO
                    "startGradientColor": start_gradient_color,
                    "endGradientColor": end_gradient_color,
                }
                for option in color_by_options
            }

    def convert_size_by_options(self):
        for type_data in self.json["types"].values():
            size_by_options = type_data.pop("sizeByOptions")
            start_size = type_data.pop("startSize")
            end_size = type_data.pop("endSize")
            type_data["sizeByOptions"] = {
                option: {
                    "min": pixel_value_to_num(start_size),
                    "max": pixel_value_to_num(end_size),
                }
                for option in size_by_options
            }

    def include_data_props_name(self):
        for data_entry in self.json["data"].values():
            if "props" in data_entry:
                for prop_key, prop_entry in data_entry["props"].items():
                    prop_entry["name"] = prop_key

    def include_data_props_type(self):
        for data_entry in self.json["data"].values():
            if "props" in data_entry:
                for prop_entry in data_entry["props"].values():
                    prop_entry["type"] = infer_prop_type(prop_entry)

    def perform(self):
        self.convert_color_by_options()
        self.convert_size_by_options()
        self.include_data_props_name()
        self.include_data_props_type()


class Arcs(ArcsNodesGeosSerializer):
    pass


class Nodes(ArcsNodesGeosSerializer):
    pass


class Geos(ArcsNodesGeosSerializer):
    def perform(self):
        self.convert_color_by_options()
        self.include_data_props_name()
        self.include_data_props_type()


class Kpis(TopLevelKeySerializer):
    def perform(self):
        for kpi_entry in self.json["data"].values():
            if "value" not in kpi_entry:
                kpi_entry["type"] = "head"


class Panes(TopLevelKeySerializer):
    def perform(self):
        for pane_key, pane_entry in self.json["data"].items():
            if "name" not in pane_entry:
                pane_entry["name"] = pane_key + " Pane"


class Settings(TopLevelKeySerializer):
    def perform(self):
        icon_url = self.json["data"].pop("IconUrl")
        self.json["data"]["iconUrl"] = icon_url


TOP_LEVEL_KEY_SERIALIZERS = {
    "kpis": Kpis,
    "arcs": Arcs,
    "nodes": Nodes,
    "geos": Geos,
    "panes": Panes,
    "settings": Settings,
}
