import os
import sys
from dotenv import load_dotenv

load_dotenv()
# DON\'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory
from flask_cors import CORS
from src.models.user import db
from src.models.memory import db as memory_db, ElizaMemory, ConversationHistory, MemoryAssociation
from src.utils.memory_manager import memory_manager
from src.routes.user import user_bp
from src.routes.blockchain import blockchain_bp
from src.routes.eliza import eliza_bp
from src.routes.ai_agents import ai_agents_bp
from src.routes.storage import storage_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))

# Security: SECRET_KEY must be provided via environment variable
# Do NOT hardcode secrets - this will raise an error in production if unset
secret_key = os.environ.get('SECRET_KEY')
if not secret_key:
    import secrets
    secret_key = secrets.token_hex(32)
    print("WARNING: SECRET_KEY not set in environment. Using a temporary random key. Sessions will not persist across restarts.")
app.config['SECRET_KEY'] = secret_key

# Enable CORS with restrictions - allow all only in development
# In production, set ALLOWED_ORIGINS to specific domains
cors_origins = os.environ.get('ALLOWED_ORIGINS', '*')
if cors_origins != '*':
    cors_origins = [origin.strip() for origin in cors_origins.split(',')]
CORS(app, origins=cors_origins)

# Register blueprints
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(blockchain_bp, url_prefix='/api/blockchain')
app.register_blueprint(eliza_bp, url_prefix='/api/eliza')
app.register_blueprint(ai_agents_bp, url_prefix='/api/ai-agents')
app.register_blueprint(storage_bp, url_prefix='/api/storage')

# Initialize memory manager
from src.utils.supabase_memory_manager import supabase_memory_manager
supabase_memory_manager.init_app(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
            return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404


if __name__ == '__main__':
    # debug mode only when explicitly enabled via environment
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)
