import os

def createViews(folder):
  views = os.path.join(folder, 'views')
  if os.path.exists(views):
    viewsFile = open(views + '/index.ejs', 'w')
    viewsFile.write("""<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <title>document</title>
    
  </head>
  <body>
      
  </body>
</html>""")
    viewsFile.close()
  else:
    os.mkdir(views)
    viewsFile = open(views + '/index.ejs', 'w')
    viewsFile.write("""<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <title>document</title>
    
  </head>
  <body>
      
  </body>
</html>""")
    viewsFile.close()