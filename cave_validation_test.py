from cave_utils.validator import Validator
from cave_serializer import Serializer
import json

if __name__ == "__main__":
    session_data = {
        "settings": {
            "allow_modification": False,
            "send_to_api": False,
            "send_to_client": True,
            "data": {
                "IconUrl": "https://react-icons.mitcave.com/0.0.1",
                "debug": True,
            },
        },
        "geoJsons": {
            "allow_modification": False,
            "send_to_api": False,
            "send_to_client": True,
            "data": {
                "StateGeoJson": "https://geojsons.mitcave.com/world/world-states-provinces-md.json",
                "CountryGeoJson": "https://geojsons.mitcave.com/world/countries-sm.json",
            },
        },
        "categories": {
            "allow_modification": False,
            "data": {
                "Location": {
                    "data": {
                        "loc_US_MI": {
                            "Region": "North America",
                            "Country": "USA",
                            "State": "Michigan",
                        },
                        "loc_US_MA": {
                            "Region": "North America",
                            "Country": "USA",
                            "State": "Massachusetts",
                        },
                        "loc_US_FL": {
                            "Region": "North America",
                            "Country": "USA",
                            "State": "Florida",
                        },
                        "loc_US_IN": {
                            "Region": "North America",
                            "Country": "USA",
                            "State": "Indiana",
                        },
                        "loc_CA_ON": {
                            "Region": "North America",
                            "Country": "Canada",
                            "State": "Ontario",
                        },
                    },
                    "name": "Locations",
                    "nestedStructure": {
                        "Region": {
                            "name": "Regions",
                            "order": 1,
                        },
                        "Country": {
                            "name": "Countries",
                            "ordering": ["USA", "Canada"],
                            "order": 2,
                        },
                        "State": {
                            "name": "States",
                            "order": 3,
                        },
                    },
                    "layoutDirection": "horizontal",
                    "order": 0,
                },
                "Product": {
                    "data": {
                        "prd_abc123": {
                            "Type": "Fruit",
                            "Size": "Big",
                            "Product": "Apple",
                        },
                        "prd_def456": {
                            "Type": "Fruit",
                            "Size": "Small",
                            "Product": "Grape",
                        },
                    },
                    "name": "Products",
                    "nestedStructure": {
                        "Type": {
                            "name": "Types",
                            "order": 1,
                        },
                        "Size": {
                            "name": "Sizing",
                            "ordering": ["Small", "Big"],
                            "order": 2,
                        },
                        "Product": {
                            "name": "Products",
                            "order": 3,
                        },
                    },
                    "layoutDirection": "horizontal",
                    "order": 1,
                },
            },
        },
        "panes": {
            "data": {
                "settings": {
                    "name": "Settings Pane",
                    "props": {
                        "Solver": {
                            "name": "Solver",
                            "type": "selector",
                            "variant": "dropdown",
                            "value": {
                                "Gurobi": True,
                                "Cplex": False,
                                "CoinOR": False,
                            },
                            "enabled": True,
                            "help": "Select a solver type to use",
                            "reinit": True,
                            "order": 1,
                        },
                        "optimality_section": {
                            "name": "Optimality Section",
                            "type": "head",
                            "help": "Some help for the optimality section",
                            "order": 2,
                        },
                        "Pct_Optimal": {
                            "name": "Percent Optimal",
                            "type": "num",
                            "value": 97,
                            "enabled": True,
                            "help": "What percent of optimal would you like to sove to?",
                            "maxValue": 100,
                            "minValue": 0,
                            "order": 3,
                        },
                    },
                    "icon": "BsWrench",
                    "color": {
                        "dark": "rgb(64, 179, 54)",
                        "light": "rgb(24, 73, 20)",
                    },
                    "type": "options",
                    "change": "manual",
                    "teamSync": True,
                    "order": 1,
                },
                "settingsBig": {
                    "name": "Settings Big Pane",
                    "props": {
                        "solver_section": {
                            "name": "Solver Section",
                            "type": "head",
                            "help": "Some help for the solver section",
                            "order": 1,
                            "column": 1,
                        },
                        "Solver": {
                            "name": "Solver",
                            "type": "selector",
                            "variant": "dropdown",
                            "value": {
                                "Gurobi": True,
                                "Cplex": False,
                                "CoinOR": False,
                            },
                            "enabled": True,
                            "help": "Select a solver type to use",
                            "reinit": True,
                            "order": 2,
                            "column": 1,
                        },
                        "optimality_section": {
                            "name": "Optimality Section",
                            "type": "head",
                            "help": "Some help for the optimality section",
                            "order": 1,
                            "column": 2,
                        },
                        "Pct_Optimal": {
                            "name": "Percent Optimal",
                            "type": "num",
                            "value": 97,
                            "enabled": True,
                            "variant": "slider",
                            "help": "What percent of optimal would you like to sove to?",
                            "maxValue": 100,
                            "minValue": 0,
                            "order": 2,
                            "column": 2,
                        },
                        "distance_section": {
                            "name": "Demand Served At Distances",
                            "type": "head",
                            "help": "How much demand do you expect to serve at the following distances?",
                            "order": 1,
                            "column": 3,
                        },
                        "50_miles": {
                            "name": "50 Miles",
                            "type": "num",
                            "value": 45,
                            "enabled": True,
                            "variant": "slider-condensed",
                            "help": "Expected demand filled at 50 miles",
                            "maxValue": 100,
                            "minValue": 0,
                            "order": 2,
                            "column": 3,
                        },
                        "100_miles": {
                            "name": "100 Miles",
                            "type": "num",
                            "value": 35,
                            "enabled": True,
                            "variant": "slider-condensed",
                            "help": "Expected demand filled at 100 miles",
                            "maxValue": 100,
                            "minValue": 0,
                            "order": 3,
                            "column": 3,
                        },
                        "150_miles": {
                            "name": "150 Miles",
                            "type": "num",
                            "value": 25,
                            "enabled": True,
                            "variant": "slider-condensed",
                            "help": "Expected demand filled at 150 miles",
                            "maxValue": 100,
                            "minValue": 0,
                            "order": 4,
                            "column": 3,
                        },
                    },
                    "icon": "BsWrench",
                    "color": {
                        "dark": "rgb(46, 244, 208)",
                        "light": "rgb(17, 79, 68)",
                    },
                    "type": "optionsFull",
                    "change": "automatic",
                    "order": 2,
                },
                "options": {
                    "name": "Options Pane",
                    "props": {
                        "Combine_Materials": {
                            "type": "selector",
                            "value": {"True": True, "False": False},
                            "enabled": True,
                            "help": "Do you want to combine materials and treat them equally when solving?",
                            "variant": "radio",
                            "order": 2,
                        },
                        "Meet_Monthly_Demand": {
                            "type": "selector",
                            "value": {"True": True, "False": False},
                            "enabled": True,
                            "help": "Do you want to force the solver to meet the monthly demand thresholds?",
                            "variant": "radio",
                            "order": 3,
                        },
                    },
                    "icon": "MdSettings",
                    "type": "options",
                    "change": "automatic",
                    "order": 1,
                },
                "context": {
                    "props": {
                        "Demand_Multiplier": {
                            "type": "num",
                            "value": 100,
                            "enabled": True,
                            "help": "Percentage multiplier times the base demand (100%=Given Demand)",
                            "label": "%",
                            "variant": "slider",
                            "maxValue": 500,
                            "minValue": 0,
                            "selectableCategories": ["Location", "Product"],
                        },
                        "Supply_Multiplier": {
                            "type": "num",
                            "value": 100,
                            "enabled": True,
                            "help": "Percentage multiplier times the base supply (100%=Given Supply)",
                            "label": "%",
                            "minValue": 0,
                            "constraint": "int",
                            "selectableCategories": ["Location", "Product"],
                        },
                    },
                    "data": {
                        "context_1": {
                            "prop": "Demand_Multiplier",
                            "value": 110,
                            "applyCategories": {"Location": ["loc_US_MI"]},
                        }
                    },
                    "icon": "BsInboxes",
                    "type": "context",
                    "change": "automatic",
                    "order": 4,
                },
            }
        },
        "arcs": {
            "name": "Arcs",
            "types": {
                "T1": {
                    "name": "Flow Type 1",
                    "colorByOptions": ["Flow Capacity", "Flow"],
                    "colorBy": "Flow",
                    "startGradientColor": {
                        "dark": "rgb(233, 0, 0)",
                        "light": "rgb(52, 52, 236)",
                    },
                    "endGradientColor": {
                        "dark": "rgb(96, 2, 2)",
                        "light": "rgb(23, 23, 126)",
                    },
                    "lineBy": "solid",
                    "sizeByOptions": ["Flow Capacity", "Flow"],
                    "sizeBy": "Flow Capacity",
                    "startSize": "15px",
                    "endSize": "30px",
                    "order": 0,
                },
                "T2": {
                    "name": "Flow Type 2",
                    "colorByOptions": ["Flow Capacity", "Flow"],
                    "colorBy": "Flow",
                    "startGradientColor": {
                        "dark": "rgb(233, 0, 0)",
                        "light": "rgb(52, 52, 236)",
                    },
                    "endGradientColor": {
                        "dark": "rgb(96, 2, 2)",
                        "light": "rgb(23, 23, 126)",
                    },
                    "lineBy": "dotted",
                    "sizeByOptions": ["Flow Capacity", "Flow"],
                    "sizeBy": "Flow Capacity",
                    "startSize": "15px",
                    "endSize": "30px",
                    "order": 1,
                },
            },
            "propDefaults": {
                "Flow Capacity": {
                    "name": "Flow Capacity (test)",
                    "type": "num",
                    "enabled": False,
                    "help": "Flow Capacity",
                    "order": 1,
                    "unit": "units (test)",
                },
            },
            "data": {
                "arc_1": {
                    "startLatitude": 43.78,
                    "startLongitude": -79.63,
                    "endLatitude": 39.82,
                    "endLongitude": -86.18,
                    "startClick": 800,
                    "endClick": 1600,
                    "type": "T1",
                    "category": {
                        "Location": ["loc_CA_ON", "loc_US_IN"],
                        "Product": ["prd_def456", "prd_abc123"],
                    },
                    "props": {
                        "Flow Capacity": {
                            "value": 50,
                        },
                        "Flow": {
                            "name": "Flow (test)",
                            "type": "num",
                            "value": 40,
                            "enabled": False,
                            "help": "Flow",
                            "order": 2,
                            "unit": "units (test)",
                        },
                    },
                },
                "arc_2": {
                    "startLatitude": 39.82,
                    "startLongitude": -86.18,
                    "endLatitude": 42.89,
                    "endLongitude": -85.68,
                    "startClick": 1600,
                    "endClick": 2000,
                    "type": "T2",
                    "category": {
                        "Location": ["loc_US_MI", "loc_US_IN"],
                        "Product": ["prd_def456", "prd_abc123"],
                    },
                    "props": {
                        "Flow Capacity": {
                            "value": 30,
                        },
                        "Flow": {
                            "type": "num",
                            "value": 20,
                            "enabled": False,
                            "help": "Flow",
                            "order": 2,
                        },
                    },
                },
                "arc_3": {
                    "startLatitude": 39.82,
                    "startLongitude": -86.18,
                    "endLatitude": 28.49,
                    "endLongitude": -81.56,
                    "startClick": 1600,
                    "endClick": 2000,
                    "type": "T2",
                    "category": {
                        "Location": ["loc_US_FL", "loc_US_IN"],
                        "Product": ["prd_def456", "prd_abc123"],
                    },
                    "props": {
                        "Flow Capacity": {
                            "value": 30,
                        },
                        "Flow": {
                            "type": "num",
                            "value": 14,
                            "enabled": False,
                            "help": "Flow",
                            "order": 2,
                        },
                    },
                },
                "arc_4": {
                    "startLatitude": 39.82,
                    "startLongitude": -86.18,
                    "endLatitude": 42.361176,
                    "endLongitude": -71.084707,
                    "startClick": 1600,
                    "endClick": 2000,
                    "type": "T2",
                    "category": {
                        "Location": ["loc_US_MA", "loc_US_IN"],
                        "Product": ["prd_def456", "prd_abc123"],
                    },
                    "props": {
                        "Flow Capacity": {
                            "type": "num",
                            "value": 30,
                            "enabled": False,
                            "help": "Flow Capacity",
                            "order": 1,
                        },
                        "Flow": {
                            "type": "num",
                            "value": 6,
                            "enabled": False,
                            "help": "Flow",
                            "order": 2,
                        },
                    },
                },
            },
        },
        "nodes": {
            "name": "Nodes",
            "types": {
                "DC": {
                    "name": "DCs",
                    "colorByOptions": ["Size", "Capacity"],
                    "colorBy": "Size",
                    "minColorRange": 0,
                    "startGradientColor": {
                        "dark": "rgb(233, 0, 0)",
                        "light": "rgb(52, 52, 236)",
                    },
                    "endGradientColor": {
                        "dark": "rgb(96, 2, 2)",
                        "light": "rgb(23, 23, 126)",
                    },
                    "minSizeRange": 0,
                    "sizeByOptions": ["Size", "Capacity"],
                    "sizeBy": "Capacity",
                    "startSize": "30px",
                    "endSize": "45px",
                    "icon": "MdStore",
                    "checkXBy": "Active",
                    "order": 1,
                },
                "Store": {
                    "name": "Stores",
                    "colorByOptions": ["Size", "Capacity"],
                    "colorBy": "Size",
                    "startGradientColor": {
                        "dark": "rgb(233, 0, 0)",
                        "light": "rgb(52, 52, 236)",
                    },
                    "endGradientColor": {
                        "dark": "rgb(96, 2, 2)",
                        "light": "rgb(23, 23, 126)",
                    },
                    "sizeByOptions": ["Size", "Capacity"],
                    "sizeBy": "Capacity",
                    "startSize": "30px",
                    "endSize": "45px",
                    "icon": "BsBuilding",
                    "checkXBy": "Active",
                    "order": 0,
                },
            },
            "propDefaults": {
                "Size": {
                    "type": "num",
                    "enabled": True,
                    "help": "The Size in SQ Meters",
                    "unit": "Sq Meters",
                    "column": 2,
                },
            },
            "data": {
                "node_1": {
                    "latitude": 43.78,
                    "longitude": -79.63,
                    "type": "DC",
                    "category": {
                        "Location": ["loc_CA_ON"],
                        "Product": ["prd_def456", "prd_abc123"],
                    },
                    "props": {
                        "Size": {
                            "value": 100,
                        },
                        "Capacity": {
                            "type": "num",
                            "value": 50,
                            "enabled": False,
                            "help": "The capacity in units",
                        },
                        "Active": {
                            "type": "toggle",
                            "value": True,
                            "enabled": True,
                            "help": "The active status of this location",
                        },
                    },
                },
                "node_2": {
                    "latitude": 39.82,
                    "longitude": -86.18,
                    "type": "DC",
                    "category": {
                        "Location": ["loc_US_IN"],
                        "Product": ["prd_def456", "prd_abc123"],
                    },
                    "props": {
                        "Size": {
                            "value": 80,
                        },
                        "Capacity": {
                            "type": "num",
                            "value": 40,
                            "enabled": False,
                            "help": "The capacity in units",
                        },
                        "Active": {
                            "type": "toggle",
                            "value": True,
                            "enabled": False,
                            "help": "The active status of this location",
                        },
                    },
                },
                "node_3": {
                    "latitude": 42.89,
                    "longitude": -85.68,
                    "type": "Store",
                    "category": {
                        "Location": ["loc_US_MI"],
                        "Product": ["prd_def456", "prd_abc123"],
                    },
                    "props": {
                        "Size": {
                            "value": 1000,
                        },
                        "Capacity": {
                            "type": "num",
                            "value": 250,
                            "enabled": False,
                            "help": "The capacity in units",
                        },
                        "Active": {
                            "type": "toggle",
                            "value": True,
                            "enabled": False,
                            "help": "The active status of this location",
                        },
                    },
                },
                "node_4": {
                    "latitude": 28.49,
                    "longitude": -81.56,
                    "type": "Store",
                    "category": {
                        "Location": ["loc_US_FL"],
                        "Product": ["prd_def456", "prd_abc123"],
                    },
                    "props": {
                        "Size": {
                            "value": 1000,
                        },
                        "Capacity": {
                            "type": "num",
                            "value": 250,
                            "enabled": False,
                            "help": "The capacity in units",
                        },
                        "Active": {
                            "type": "toggle",
                            "value": True,
                            "enabled": False,
                            "help": "The active status of this location",
                        },
                    },
                },
                "node_5": {
                    "latitude": 42.361176,
                    "longitude": -71.084707,
                    "type": "Store",
                    "category": {
                        "Location": ["loc_US_MA"],
                        "Product": ["prd_def456", "prd_abc123"],
                    },
                    "props": {
                        "Size": {
                            "value": 1000,
                        },
                        "Capacity": {
                            "type": "num",
                            "value": 250,
                            "enabled": False,
                            "help": "The capacity in units",
                        },
                        "Active": {
                            "type": "toggle",
                            "value": True,
                            "enabled": False,
                            "help": "The active status of this location",
                        },
                    },
                },
            },
        },
        "geos": {
            "name": "Geographies",
            "types": {
                "state": {
                    "name": "State",
                    "colorByOptions": ["Demand"],
                    "colorBy": "Demand",
                    "geoJson": {
                        "geoJsonLayer": "StateGeoJson",
                        "geoJsonProp": "code_hasc",
                    },
                    "startGradientColor": {
                        "dark": "rgb(100, 100, 100)",
                        "light": "rgb(200, 200, 200)",
                    },
                    "endGradientColor": {
                        "dark": "rgb(20, 205, 20)",
                        "light": "rgb(10, 100, 10)",
                    },
                    "icon": "BsHexagon",
                },
                "country": {
                    "name": "Country",
                    "colorByOptions": ["Demand"],
                    "colorBy": "Demand",
                    "geoJson": {
                        "geoJsonLayer": "CountryGeoJson",
                        "geoJsonProp": "FIPS_10",
                    },
                    "startGradientColor": {
                        "dark": "rgb(100, 100, 100)",
                        "light": "rgb(200, 200, 200)",
                    },
                    "endGradientColor": {
                        "dark": "rgb(20, 205, 20)",
                        "light": "rgb(10, 100, 10)",
                    },
                    "icon": "BsHexagon",
                },
            },
            "propDefaults": {
                "Demand": {
                    "type": "num",
                    "enabled": True,
                    "help": "The Demand of this Geography",
                    "unit": "Units",
                },
            },
            "data": {
                "geo_1": {
                    "name": "Ontario, Canada",
                    "geoJsonValue": "CA.ON",
                    "type": "state",
                    "category": {"Location": ["loc_CA_ON"]},
                    "props": {
                        "Demand": {
                            "value": 50,
                        }
                    },
                },
                "geo_2": {
                    "name": "Michigan, USA",
                    "geoJsonValue": "US.MI",
                    "type": "state",
                    "category": {"Location": ["loc_US_MI"]},
                    "props": {
                        "Demand": {
                            "value": 300,
                        }
                    },
                },
                "geo_3": {
                    "name": "Massachusetts, USA",
                    "geoJsonValue": "US.MA",
                    "type": "state",
                    "category": {"Location": ["loc_US_MI"]},
                    "props": {
                        "Demand": {
                            "value": 250,
                        }
                    },
                },
                "geo_4": {
                    "name": "Florida, USA",
                    "geoJsonValue": "US.FL",
                    "type": "state",
                    "category": {"Location": ["loc_US_MI"]},
                    "props": {
                        "Demand": {
                            "value": 100,
                        }
                    },
                },
                "geo_5": {
                    "name": "Indiana, USA",
                    "geoJsonValue": "US.FL",
                    "type": "state",
                    "category": {"Location": ["loc_US_MI"]},
                    "props": {
                        "Demand": {
                            "value": 200,
                        }
                    },
                },
                "geo_c_1": {
                    "name": "Canada",
                    "geoJsonValue": "CA",
                    "type": "country",
                    "category": {"Location": ["loc_CA_ON"]},
                    "props": {
                        "Demand": {
                            "value": 50,
                        }
                    },
                },
                "geo_c_2": {
                    "name": "USA",
                    "geoJsonValue": "US",
                    "type": "country",
                    "category": {
                        "Location": [
                            "loc_US_FL",
                            "loc_US_MA",
                            "loc_US_IN",
                            "loc_US_MI",
                        ]
                    },
                    "props": {
                        "Demand": {
                            "value": 800,
                        }
                    },
                },
            },
        },
        "stats": {
            "name": "Statistics",
            "types": {
                "demand_met": {
                    "name": "Demand Met",
                    "calculation": "demand_met",
                    "unit": "units",
                    "order": 1,
                },
                "demand_tot": {
                    "name": "Demand Total",
                    "calculation": "demand_tot",
                    "unit": "units",
                    "order": 2,
                },
                "demand_pct": {
                    "name": "Demand Percentage",
                    "calculation": "demand_met / demand_tot",
                    "unit": "%",
                    "order": 3,
                },
            },
            "data": {
                "d1": {
                    "category": {
                        "Location": ["loc_CA_ON"],
                        "Product": ["prd_abc123"],
                    },
                    "values": {"demand_met": 5, "demand_tot": 10},
                },
                "d2": {
                    "category": {
                        "Location": ["loc_CA_ON"],
                        "Product": ["prd_def456"],
                    },
                    "values": {"demand_met": 4, "demand_tot": 5},
                },
                "d3": {
                    "category": {
                        "Location": ["loc_US_MI"],
                        "Product": ["prd_abc123"],
                    },
                    "values": {"demand_met": 6, "demand_tot": 7},
                },
                "d4": {
                    "category": {
                        "Location": ["loc_US_MI"],
                        "Product": ["prd_def456"],
                    },
                    "values": {"demand_met": 3, "demand_tot": 5},
                },
            },
        },
        "keys": {
            "data": {
                "key_1": {
                    "name": "Global Demand Met",
                    "unit": "units",
                    "value": 18,
                    "icon": "BsInboxes",
                    "order": 1,
                },
                "key_2": {
                    "name": "Customer Happiness",
                    "unit": "smiles",
                    "value": 16,
                    "icon": "BsFillEmojiSmileFill",
                    "order": 2,
                },
            },
        },
        "kpis": {
            "data": {
                "demand_header": {
                    "name": "Demand Section",
                    "unit": "units",
                    "icon": "BsInboxes",
                    "order": 0,
                    "column": 1,
                },
                "demand": {
                    "name": "Global Demand",
                    "unit": "units",
                    "icon": "BsInboxes",
                    "order": 1,
                    "column": 1,
                    "value": 100,
                    "sum": 100,
                    "max": 10,
                    "pct75": 7,
                    "med": 5,
                    "pct25": 3,
                    "min": 1,
                    "avg": 6,
                },
                "supply_header": {
                    "name": "Supply Section",
                    "unit": "units",
                    "icon": "BsTruck",
                    "order": 0,
                    "column": 2,
                },
                "big_number": {
                    "name": "Big Number",
                    "unit": "units",
                    "icon": "BsTruck",
                    "order": 1,
                    "column": 2,
                    "value": 10000000000000,
                    "sum": 100,
                    "max": 10,
                    "pct75": 7,
                    "med": 5,
                    "pct25": 3,
                    "min": 1,
                    "avg": 6,
                },
                "supply": {
                    "name": "Really Big Number",
                    "unit": "units",
                    "icon": "BsTruck",
                    "order": 1,
                    "column": 2,
                    "value": 100000000000000000000000000,
                    "sum": 100,
                    "max": 10,
                    "pct75": 7,
                    "med": 5,
                    "pct25": 3,
                    "min": 1,
                    "avg": 6,
                },
            },
        },
        "localDefaults": {
            "allow_modification": False,
            "data": {
                "panes": {
                    "open": None,
                    "secondaryOpen": None,
                    "panes": {},
                    "filtered": {},
                },
                "map": {
                    "icon": "MdExplore",
                    "color": {
                        "dark": "rgb(224, 224, 224)",
                        "light": "rgb(32, 32, 32)",
                    },
                    "mapControls": {
                        "viewport": {
                            "longitude": -85,
                            "latitude": 38,
                            "zoom": 6,
                            "pitch": 0,
                            "bearing": 0,
                            "height": 1983,
                            "altitude": 1.5,
                            "maxZoom": 12,
                            "minZoom": 1.5,
                        },
                        "optionalViewports": {
                            "ov1": {
                                "name": "Optional Viewport One",
                                "icon": "FaGlobe",
                                "order": 1,
                                "longitude": -79,
                                "latitude": 38,
                                "zoom": 5,
                                "minZoom": 0,
                                "maxZoom": 12,
                                "pitch": 0,
                                "bearing": 0,
                            }
                        },
                    },
                    "mapLayers": {
                        "geography": {
                            "stat": "Select Statistic",
                            "type": "Select Type",
                            "enabled": True,
                        },
                        "enabledNodes": [],
                        "enabledArcs": [],
                    },
                    "mapLegend": {
                        "isOpen": True,
                    },
                    "order": 1,
                },
                "dashboards": {
                    "data": {
                        "dash_1": {
                            "icon": "BsCircleFill",
                            "name": "Dashboard 1",
                            "type": "stats",
                            "color": {
                                "dark": "rgb(178, 179, 55)",
                                "light": "rgb(79, 79, 24)",
                            },
                            "order": 1,
                            "layout": [
                                {
                                    "chart": "Bar",
                                    "grouping": "Average",
                                    "statistic": "demand_met",
                                },
                                {
                                    "chart": "Line",
                                    "grouping": "Sum",
                                    "statistic": "demand_pct",
                                },
                                {
                                    "chart": "Bar",
                                    "level": "Size",
                                    "category": "Product",
                                    "grouping": "Sum",
                                    "statistic": "demand_met",
                                },
                                {
                                    "chart": "Bar",
                                    "grouping": "Minimum",
                                    "type": "kpis",
                                    "sessions": [],
                                    "kpi": "Really Big Number",
                                },
                            ],
                            "lockedLayout": False,
                        },
                        "dash_2": {
                            "icon": "BsSquareFill",
                            "name": "Dashboard 2",
                            "type": "kpis",
                            "color": {
                                "dark": "rgb(57, 201, 176)",
                                "light": "rgb(22, 77, 67)",
                            },
                            "order": 2,
                            "layout": [
                                {
                                    "chart": "Bar",
                                    "grouping": "Average",
                                    "statistic": "demand_met",
                                    "category": None,
                                    "level": None,
                                },
                                {
                                    "chart": "Line",
                                    "grouping": "Sum",
                                    "statistic": "demand_pct",
                                },
                                {
                                    "chart": "Bar",
                                    "level": "Size",
                                    "category": "Product",
                                    "grouping": "Sum",
                                    "statistic": "demand_met",
                                },
                                {
                                    "chart": "Bar",
                                    "level": "Size",
                                    "category": "Product",
                                    "grouping": "Average",
                                    "statistic": "demand_met",
                                },
                            ],
                            "lockedLayout": False,
                        },
                    },
                    "dashboardId": "dash_1",
                    "order": 2,
                },
                "kpi": {
                    "icon": "MdSpeed",
                    "color": {
                        "dark": "rgb(224, 224, 224)",
                        "light": "rgb(32, 32, 32)",
                    },
                    "order": 3,
                },
                "settings": {"theme": "dark", "view": "map"},
            },
        },
    }

    serializer = Serializer(session_data)
    serialized_data = serializer.perform()

    x = Validator(serialized_data)
    x.log.print_logs(level="error")

    with open("result.json", "w") as fp:
        json.dump(serialized_data, fp, indent=4)
