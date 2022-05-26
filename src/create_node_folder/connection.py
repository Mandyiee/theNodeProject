import os

def createConnection(folder):
  connection = os.path.join(folder, 'connection')
  if os.path.exists(connection):
    connectionFile = open(connection + '/db.js', 'w')
    connectionFile.write("""
const mongoose = require('mongoose')
require('dotenv').config()

async function connectDB () {
mongoose.connect(process.env.MONGO_URI, {useNewUrlParser: true,useUnifiedTopology: true})

mongoose.connection.once('open', function () {
    console.log('connection has been mande')
}).on('error', function(error) {
    console.log('connection error', error)
})
}

module.exports = connectDB""")
    connectionFile.close()
  else:
    os.mkdir(connection)
    connectionFile = open(connection + '/db.js', 'w')
    connectionFile.write("""
const mongoose = require('mongoose')
require('dotenv').config()

async function connectDB () {
mongoose.connect(process.env.MONGO_URI, {useNewUrlParser: true,useUnifiedTopology: true})

mongoose.connection.once('open', function () {
    console.log('connection has been mande')
}).on('error', function(error) {
    console.log('connection error', error)
})
}

module.exports = connectDB""")
    connectionFile.close()