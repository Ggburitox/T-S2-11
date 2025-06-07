import boto3
import json
import base64

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        bucket = body['bucket']
        directorio = body['directorio']
        nombre_archivo = body['nombre_archivo']
        contenido_base64 = body['archivo']  # contenido codificado en base64
    except (KeyError, json.JSONDecodeError):
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Se requieren "bucket", "directorio", "nombre_archivo" y "archivo"'})
        }

    # Decodificar el archivo
    try:
        contenido_binario = base64.b64decode(contenido_base64)
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Archivo inválido (base64): ' + str(e)})
        }

    s3 = boto3.client('s3')
    clave_objeto = directorio.strip('/') + '/' + nombre_archivo

    try:
        s3.put_object(Bucket=bucket, Key=clave_objeto, Body=contenido_binario)
        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'Archivo "{nombre_archivo}" subido a "{clave_objeto}" en el bucket "{bucket}".'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
