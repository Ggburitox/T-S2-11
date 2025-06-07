import boto3
import json

def lambda_handler(event, context):
    body = json.loads(event['body'])
    bucket = body['bucket']
    directorio = body['directorio']
    s3 = boto3.client('s3')   
    clave_directorio = directorio.strip('/') + '/' 
    s3.put_object(Bucket=bucket, Key=clave_directorio)
    return {
            'statusCode': 200,
            'body': json.dumps({'message': f'Directorio "{clave_directorio}" creado en el bucket "{bucket}".'})
    }