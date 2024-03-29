from cerberus import Validator

body = {
    "data": {
        "elemento1": 123.98,
        "elemento2": "olaMundo",
    }
}


body_Validator = Validator({
    'data': {
        'type':'Dict',
        'schema':{
            'elemento1':{'type':'float','required':True,'empty':False},
            'elemento2':{'type':'string','required':True,'empty':False},
            'elemento3':{'type':'string','required':False,'empty':False}
        }
    }
})
response = body_Validator.validate(body)

if response is False:
    print(body_Validator.errors)
else:
    print('Body OK')