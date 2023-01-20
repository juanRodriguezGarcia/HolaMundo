import json
import boto3
import base64

s3 = boto3.resource('s3')
   
def lambda_handler(event, context):
     print ("Evento entrada:", event)
     return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps('Hello from Lambda! Juanito ...')
    }





Access-Control-Allow-Headers	  
Access-Control-Allow-Methods	  
Access-Control-Allow-Origin	  
X-Requested-With


Has been blocked by CORS policy: 
No 'Access-Control-Allow-Origin'  header is present on the requested resource. 
If on opaque response server your needs,  set the request's mode to 'no-cors'  to fetch the resource with CORs disabled 