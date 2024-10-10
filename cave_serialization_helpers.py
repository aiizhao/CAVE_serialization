def infer_prop_type(prop_entry):
    if "value" not in prop_entry:
        return "head"
    elif isinstance(prop_entry["value"], str):
        return "text"
    elif isinstance(prop_entry["value"], bool):
        return "toggle"
    elif isinstance(prop_entry["value"], dict):
        return "selector"
    return "num"


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
    def __init__(self, session_data):
        super().__init__(session_data)
        self.props_min_values = dict()
        self.props_max_values = dict()
        self.get_data_props_min_and_max()

    def get_data_props_min_and_max(self):
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

    def include_data_props_name_and_type(self):
        for data_entry in self.json["data"].values():
            for prop_key, prop_entry in data_entry["props"].items():
                prop_entry.setdefault("name", prop_key)
                prop_entry.setdefault("type", infer_prop_type(prop_entry))

    def convert_color_by_options(self):
        for type_entry in self.json["types"].values():
            color_by_options = type_entry["colorByOptions"]
            if isinstance(color_by_options, list):
                type_entry["colorByOptions"] = {
                    prop: {
                        "min": self.props_min_values[prop],
                        "max": self.props_max_values[prop],
                        "startGradientColor": type_entry["startGradientColor"],
                        "endGradientColor": type_entry["endGradientColor"],
                    }
                    for prop in color_by_options
                }

    def convert_size_by_options(self):
        for type_entry in self.json["types"].values():
            size_by_options = type_entry["sizeByOptions"]
            if isinstance(size_by_options, list):
                type_entry["sizeByOptions"] = {
                    prop: {
                        "min": self.props_min_values[prop],
                        "max": self.props_max_values[prop],
                    }
                    for prop in size_by_options
                }

    def perform(self):
        self.include_data_props_name_and_type()
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
        icon_url = self.json["data"]["IconUrl"]
        self.json["data"]["iconUrl"] = icon_url


TOP_LEVEL_KEY_SERIALIZERS = [
    Arcs,
    Nodes,
    Geos,
    Kpis,
    Panes,
    Settings,
]


class ArcsNodesGeosDeserializer(TopLevelKeySerializer):
    def convert_color_by_options(self):
        for type_entry in self.json["types"].values():
            type_entry["colorByOptions"] = list(type_entry["colorByOptions"].keys())

    def convert_size_by_options(self):
        for type_entry in self.json["types"].values():
            type_entry["sizeByOptions"] = list(type_entry["sizeByOptions"].keys())

    def perform(self):
        self.convert_color_by_options()
        self.convert_size_by_options()


class Arcs(ArcsNodesGeosDeserializer):
    primary_key = "arcs"


class Nodes(ArcsNodesGeosDeserializer):
    primary_key = "nodes"


class Geos(ArcsNodesGeosDeserializer):
    primary_key = "geos"
    additional_keys = frozenset(["geoJsons"])

    def perform(self):
        self.convert_color_by_options()

        # revert 'geoJsonLayer' values to layer names instead of urls
        for geo_entry in self.json["types"].values():
            geo_json_url = geo_entry["geoJson"]["geoJsonLayer"]
            for layer_key, layer_value in self.additional_data["geoJsons"][
                "data"
            ].items():
                if layer_value == geo_json_url:
                    geo_entry["geoJson"]["geoJsonLayer"] = layer_key
                    break


TOP_LEVEL_KEY_DESERIALIZERS = [
    Arcs,
    Nodes,
    Geos,
]
