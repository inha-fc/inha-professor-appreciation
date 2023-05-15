from professor_appreciation import app
from professor_appreciation.routes import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
