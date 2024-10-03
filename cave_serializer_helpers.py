from cave_serializer_utils import *


class TopLevelKeySerializer:
    primary_key = None
    additional_keys = frozenset()

    def __init__(self, session_data):
        self.json = session_data.get(self.primary_key, dict())
        self.additional_data = {
            additional_key: session_data.get(additional_key, dict())
            for additional_key in self.additional_keys
        }

    def perform(self):
        pass


class ArcsNodesGeosSerializer(TopLevelKeySerializer):
    def include_data_props_name_and_type(self):
        for data_entry in self.json["data"].values():
            for prop_key, prop_entry in data_entry["props"].items():
                prop_entry.setdefault("name", prop_key)
                prop_entry.setdefault("type", infer_prop_type(prop_entry))

    def get_data_props_min_and_max(self):
        self.props_min_values = dict()
        self.props_max_values = dict()
        for data_entry in self.json["data"].values():
            for prop_key, prop_entry in data_entry["props"].items():
                self.props_min_values[prop_key] = min(
                    prop_entry["value"],
                    self.props_min_values.get(prop_key, float("inf")),
                )
                self.props_max_values[prop_key] = max(
                    prop_entry["value"],
                    self.props_max_values.get(prop_key, float("-inf")),
                )

    def convert_color_by_options(self):
        for type_entry in self.json["types"].values():
            color_by_options = type_entry.pop("colorByOptions")
            start_gradient_color = type_entry.pop("startGradientColor")
            end_gradient_color = type_entry.pop("endGradientColor")
            type_entry["colorByOptions"] = {
                prop: {
                    "min": self.props_min_values[prop],
                    "max": self.props_max_values[prop],
                    "startGradientColor": start_gradient_color,
                    "endGradientColor": end_gradient_color,
                }
                for prop in color_by_options
            }

    def convert_size_by_options(self):
        for type_entry in self.json["types"].values():
            size_by_options = type_entry.pop("sizeByOptions")
            type_entry["sizeByOptions"] = {
                prop: {
                    "min": self.props_min_values[prop],
                    "max": self.props_max_values[prop],
                }
                for prop in size_by_options
            }

    def perform(self):
        self.include_data_props_name_and_type()
        self.get_data_props_min_and_max()
        self.convert_color_by_options()
        self.convert_size_by_options()


class Arcs(ArcsNodesGeosSerializer):
    primary_key = "arcs"


class Nodes(ArcsNodesGeosSerializer):
    primary_key = "nodes"


class Geos(ArcsNodesGeosSerializer):
    primary_key = "geos"
    additional_keys = frozenset(["geoJsons"])

    def perform(self):
        self.include_data_props_name_and_type()
        self.get_data_props_min_and_max()
        self.convert_color_by_options()

        # move urls under 'geoJsons' into 'geos' types
        for geo_entry in self.json["types"].values():
            geo_json_layer = geo_entry["geoJson"]["geoJsonLayer"]
            geo_json_url = self.additional_data["geoJsons"]["data"][geo_json_layer]
            geo_entry["geoJson"]["geoJsonLayer"] = geo_json_url


class Kpis(TopLevelKeySerializer):
    primary_key = "kpis"

    def perform(self):
        # explicitly specify headers as 'head' type
        for kpi_entry in self.json["data"].values():
            if "value" not in kpi_entry:
                kpi_entry["type"] = "head"


class Panes(TopLevelKeySerializer):
    primary_key = "panes"

    def perform(self):
        # ensure all panes are named
        for pane_key, pane_entry in self.json["data"].items():
            if "name" not in pane_entry:
                pane_entry["name"] = pane_key + " Pane"


class Settings(TopLevelKeySerializer):
    primary_key = "settings"

    def perform(self):
        # 1.6.3 uses 'iconUrl' instead of 'IconUrl'
        icon_url = self.json["data"].pop("IconUrl")
        self.json["data"]["iconUrl"] = icon_url


TOP_LEVEL_KEY_SERIALIZERS = [
    Arcs,
    Nodes,
    Geos,
    Kpis,
    Panes,
    Settings,
]
