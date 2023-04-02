from flask_restful import reqparse

def status_parser():
    parser=reqparse.RequestParser()
    parser.add_argument('name', type=str, help='Name parameter is required')
    parser.add_argument('temp', type=float, help='Name parameter is required')
    return parser



def checkout_parser():
    parser=reqparse.RequestParser()
    parser.add_argument('name', type=str, help='Name parameter is required')
    parser.add_argument('checkout', type=bool, help='checkout parameter is required')
    return parser
