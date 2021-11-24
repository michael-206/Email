from app import app, db
from app.models import User, Email, Documents, Questions

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Email': Email, 'Documents': Documents, 'Questions': Questions}