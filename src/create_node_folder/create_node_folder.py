import subprocess, os
from pathlib import Path
from connection import createConnection
from model import createModel
from routes import createRoutes
from views import createViews
import fileinput



def createServer(folder):
  serverFile = open(folder + '/server.js', 'w')
  serverFile.write("""const express = require('express')
const path  = require('path')
const app = express()
const connectDB = require('./connection/db')
const PORT = process.env.PORT || 3000
const indexRouter = require('./routes/index')
  
  
connectDB()
  
app.set('view engine', 'ejs')
  
app.use(express.urlencoded({extended: true}))
  
app.use(express.static(path.join(__dirname, 'public')))
  
app.use('/', indexRouter)
  
app.listen(PORT, () => console.log('server has started'))""")
  serverFile.close()
  
def effect(folder):
  os.chdir(folder)
  subprocess.call(["npm", "init", "-y"])
  subprocess.call(["npm", "i", "ejs", "mongoose", "express","dotenv"])
  subprocess.call(["npm", "i", "nodemon","-D"])
  fin = open(folder + '/package.json', "rt")
  data = fin.read()
  data = data.replace('node ','nodemon ')
  fin.close()
  fin = open(folder + '/package.json', "wt")
  fin.write(data)
  fin.close()
  
  
  
def create_node_folder():
  print('What is the name of the folder')
  folder = input()
  homeFolder = os.path.join(Path.home(), 'nodeProjects')
  try:
    if os.path.exists(homeFolder):
      folder = os.path.join(homeFolder,folder)
      if os.path.exists(folder):
        createConnection(folder)
        createModel(folder)
        createRoutes(folder)
        createViews(folder)
        createServer(folder)
        envFile = open(folder + '/.env', 'w')
        envFile.write("""NODE_ENV=development
PORT=8080
MONGO_URI=""")
        envFile.close()
        effect(folder)
        
      else:
        os.mkdir(folder)
        createConnection(folder)
        createModel(folder)
        createRoutes(folder)
        createViews(folder)
        createServer(folder)
        envFile = open(folder + '/.env', 'w')
        envFile.write("""NODE_ENV=development
PORT=8080
MONGO_URI=""")
        envFile.close()
        effect(folder)
    else:
      os.mkdir(homeFolder)
      folder = os.path.join(homeFolder,folder)
      if os.path.exists(folder):
        createConnection(folder)
        createModel(folder)
        createRoutes(folder)
        createViews(folder)
        createServer(folder)
        envFile = open(folder + '/.env', 'w')
        envFile.write("""NODE_ENV=development
PORT=8080
MONGO_URI=""")
        envFile.close() 
        effect(folder)
      else:
        os.mkdir(folder)
        createConnection(folder)
        createModel(folder)
        createRoutes(folder)
        createViews(folder)
        createServer(folder)
        envFile = open(folder + '/.env', 'w')
        envFile.write("""NODE_ENV=development
PORT=8080
MONGO_URI=""")
        envFile.close() 
        effect(folder)
  except Exception as e:
    print(e)
    
    
create_node_folder()