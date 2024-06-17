from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

point_create_schema = {
    'operation_description': "Create a new point",
    'request_body': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'type': openapi.Schema(type=openapi.TYPE_STRING, example='Point'),
            'coordinates': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_NUMBER), example=[12, 41]),
        },
        required=['type', 'coordinates']
    ),
    'responses': {
        201: openapi.Response(
            description="Point created",
            examples={
                "application/json": {
                    "id": 1,
                    "type": "Point",
                    "coordinates": [12.0, 41.0]
                }
            }
        )
    }
}

linestring_create_schema = {
    'operation_description': "Create a new linestring",
    'request_body': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'type': openapi.Schema(type=openapi.TYPE_STRING, example='LineString'),
            'coordinates': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_NUMBER)), example=[[12, 41], [13, 42]]),
        },
        required=['type', 'coordinates']
    ),
    'responses': {
        201: openapi.Response(
            description="LineString created",
            examples={
                "application/json": {
                    "id": 1,
                    "type": "LineString",
                    "coordinates": [
                        [12.0, 41.0],
                        [13.0, 42.0]
                    ]
                }
            }
        )
    }
}

polygon_create_schema = {
    'operation_description': "Create a new polygon",
    'request_body': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'type': openapi.Schema(type=openapi.TYPE_STRING, example='Polygon'),
            'coordinates': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_NUMBER))), example=[[[12, 41], [13, 42], [14, 43], [12, 41]]]),
        },
        required=['type', 'coordinates']
    ),
    'responses': {
        201: openapi.Response(
            description="Polygon created",
            examples={
                "application/json": {
                    "id": 1,
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [12.0, 41.0],
                            [13.0, 42.0],
                            [14.0, 43.0],
                            [12.0, 41.0]
                        ]
                    ]
                }
            }
        )
    }
}

join_lines_schema = {
    'method': 'post',
    'operation_description': "Join multiple linestrings",
    'request_body': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'lines': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER), example=[1, 2]),
        },
        required=['lines']
    ),
    'responses': {
        201: openapi.Response(
            description="Joined LineString",
            examples={
                "application/json": {
                    "id": 1,
                    "type": "LineString",
                    "coordinates": [
                        [12.0, 41.0],
                        [13.0, 42.0],
                        [14.0, 43.0]
                    ]
                }
            }
        )
    }
}

polygon_intersection_schema = {
    'method': 'post',
    'operation_description': "Check if points intersect with a polygon",
    'request_body': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'points': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER), example=[1, 2]),
        },
        required=['points']
    ),
    'responses': {
        200: openapi.Response(
            description="Intersecting Points",
            examples={
                "application/json": [
                    {
                        "id": 1,
                        "type": "Point",
                        "coordinates": [12.0, 41.0]
                    },
                    {
                        "id": 2,
                        "type": "Point",
                        "coordinates": [13.0, 42.0]
                    }
                ]
            }
        )
    }
}
