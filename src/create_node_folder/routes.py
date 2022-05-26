import os

def createRoutes(folder):
  routes = os.path.join(folder, 'routes')
  if os.path.exists(routes):
    routesFile = open(routes + '/index.js', 'w')
    routesFile.write("""require('dotenv').config()
const express = require('express')
const router = express.Router()
    
router.get('/', (req, res) => {
   res.render('index')
  })
    
module.exports = router
  """)
    routesFile.close()
  else:
    os.mkdir(routes)
    routesFile = open(routes + '/index.js', 'w')
    routesFile.write("""require('dotenv').config()
const express = require('express')
const router = express.Router()
    
router.get('/', (req, res) => {
   res.render('index')
  })
    
module.exports = router
  """)
    routesFile.close()