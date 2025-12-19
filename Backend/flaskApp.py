from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import StudentChatbot
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__)

# Configure CORS for React/Vue frontend
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:3000", "http://localhost:5173"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# Initialize chatbot instance
print("🤖 Initializing Student Chatbot...")
chatbot = StudentChatbot()
print(f"✅ Chatbot initialized with {len(chatbot.training_questions)} training examples")
print(f"✅ Ready to serve requests!\n")


# ==================== API Routes ====================

@app.route('/', methods=['GET'])
def home():
    """Root endpoint with API information"""
    return jsonify({
        "success": True,
        "message": "Student Chatbot API",
        "version": "2.0",
        "endpoints": {
            "health": "/api/health",
            "greeting": "/api/greeting",
            "chat": "/api/chat (POST)",
            "intents": "/api/intents",
            "stats": "/api/stats"
        }
    }), 200


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "success": True,
        "status": "healthy",
        "message": "Student Chatbot API is running",
        "timestamp": datetime.now().isoformat()
    }), 200


@app.route('/api/greeting', methods=['GET'])
def get_greeting():
    """Get time-based greeting"""
    try:
        greeting = chatbot.get_greeting()
        return jsonify({
            "success": True,
            "greeting": greeting,
            "timestamp": datetime.now().isoformat()
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route('/api/chat', methods=['POST'])
def chat():
    """Main chat endpoint - receives user message and returns bot response"""
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate input
        if not data:
            return jsonify({
                "success": False,
                "error": "No JSON data provided"
            }), 400
        
        if 'message' not in data:
            return jsonify({
                "success": False,
                "error": "Missing 'message' field in request"
            }), 400
        
        user_message = data['message']
        
        # Validate message is not empty
        if not user_message or not user_message.strip():
            return jsonify({
                "success": False,
                "error": "Message cannot be empty"
            }), 400
        
        # Get chatbot response
        result = chatbot.get_response(user_message)
        
        return jsonify({
            "success": True,
            "user_message": user_message,
            "bot_response": result['response'],
            "intent": result['intent'],
            "timestamp": datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Internal server error: {str(e)}"
        }), 500


@app.route('/api/intents', methods=['GET'])
def get_intents():
    """Get available intents and their descriptions"""
    try:
        intents_info = chatbot.get_available_intents()
        
        return jsonify({
            "success": True,
            "intents": intents_info,
            "total_intents": len(intents_info)
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get chatbot statistics and model information"""
    try:
        stats = chatbot.get_statistics()
        
        return jsonify({
            "success": True,
            "stats": {
                "total_training_examples": stats['training_examples'],
                "total_intents": stats['total_intents'],
                "conversation_count": stats['conversation_count'],
                "intent_statistics": stats['intent_stats'],
                "model_type": "KNN with TF-IDF"
            }
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# ==================== Error Handlers ====================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        "success": False,
        "error": "Endpoint not found",
        "status_code": 404
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 errors"""
    return jsonify({
        "success": False,
        "error": "Method not allowed",
        "status_code": 405
    }), 405


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        "success": False,
        "error": "Internal server error",
        "status_code": 500
    }), 500


# ==================== Main Execution ====================

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    
    print("=" * 60)
    print("🚀 Starting Student Chatbot API Server")
    print("=" * 60)
    print(f"📍 Server running on: http://localhost:{port}")
    print(f"📚 Training Examples: {len(chatbot.training_questions)}")
    print(f"🎯 Total Intents: {len(set(chatbot.intents))}")
    print("=" * 60)
    print("\n💡 Available endpoints:")
    print(f"   - GET  /api/health")
    print(f"   - GET  /api/greeting")
    print(f"   - POST /api/chat")
    print(f"   - GET  /api/intents")
    print(f"   - GET  /api/stats")
    print("\n🛑 Press CTRL+C to stop the server\n")
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=True
    )