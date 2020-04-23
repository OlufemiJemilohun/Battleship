'''
  API for the application
'''

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/ping')
async def ping():
  '''
    Ping the API to verify it is running
  '''
  
  return {'ping': 'pong'}

if __name__ == '__main__':
  uvicorn.run('app:app', host='127.0.0.1', port=8000, log_level='info')
