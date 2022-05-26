import os

def createModel(folder):
  model = os.path.join(folder, 'model')
  if os.path.exists(model):
    modelFile = open(model + '/model.js', 'w')
    modelFile.write("""const mongoose = require('mongoose')
      
module.exports = mongoose.model('',)
      """)
    modelFile.close()
  else:
    os.mkdir(model)
    modelFile = open(model + '/model.js', 'w')
    modelFile.write("""const mongoose = require('mongoose')
      
module.exports = mongoose.model('',)
      """)
    modelFile.close()