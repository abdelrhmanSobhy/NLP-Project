from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from datetime import datetime
import numpy as np


class StudentChatbot:
    
    def __init__(self):
        # Expanded training data with more examples (176 total)
        self.training_questions = [
            # Lecture queries (20 examples)
            "when is the lecture", "what time is class", "class schedule",
            "when do we study", "lecture timing", "what time do we have class",
            "when is our next class", "tell me about lecture", "class time please",
            "when does class start", "lecture information", "next lecture",
            "what time does the class begin", "schedule for lectures",
            "when are classes held", "class timings", "lecture days",
            "what day is the lecture", "lecture room number", "where is the class",
            
            # Grade queries (20 examples)
            "grades", "my marks", "results", "what is my score",
            "check grades", "how are my grades", "when will results come",
            "show me grades", "my result", "exam results",
            "grade status", "check my marks", "what did i score",
            "how did i do", "my exam performance", "score report",
            "result announcement", "when grades release", "grade inquiry",
            "marks obtained",
            
            # Greetings (21 examples) - ADDED "hay"
            "hello", "hi", "hey", "good morning", "good afternoon",
            "good evening", "how are you", "whats up", "greetings",
            "hi there", "hey there", "hello bot", "howdy",
            "yo", "hiya", "good day", "nice to meet you",
            "hey bot", "hello there", "hi bot", "hay",
            
            # Farewells (15 examples)
            "bye", "goodbye", "see you", "exit", "quit",
            "see you later", "take care", "have a nice day",
            "gotta go", "later", "farewell", "catch you later",
            "bye bye", "see ya", "until next time",
            
            # Assignment queries (20 examples)
            "assignment", "homework", "what is the assignment", "any homework",
            "project deadline", "when is assignment due", "homework details",
            "tell me about assignment", "assignment info", "project due date",
            "what homework do we have", "assignment submission", "homework deadline",
            "project information", "assignment requirements", "homework status",
            "what is due", "pending assignments", "assignment list",
            "homework for today",
            
            # Help queries (15 examples)
            "help", "what can you do", "how can you help me",
            "help me", "what do you know", "show me options",
            "commands", "features", "what are your capabilities",
            "how do you work", "assist me", "what can i ask",
            "show commands", "available options", "help menu",
            
            # Office hours queries (15 examples)
            "office hours", "when can i meet", "meeting time", "meet professor",
            "consultation hours", "when is professor available", "meet teacher",
            "instructor availability", "meeting schedule", "professor timings",
            "when can i see the professor", "office visit", "consultation time",
            "meeting with instructor", "professor meeting",
            
            # Exam queries (20 examples)
            "exam", "test", "when is exam", "exam schedule", "test date",
            "exam time", "midterm", "final exam", "quiz", "examination",
            "test schedule", "when is the test", "exam dates",
            "midterm exam", "final examination", "quiz schedule",
            "upcoming exams", "exam information", "test timings",
            "examination schedule",
            
            # Course material queries (15 examples)
            "course material", "study material", "books", "textbook",
            "lecture notes", "slides", "presentation", "reading material",
            "course resources", "reference books", "study guide",
            "course content", "materials needed", "required books",
            "lecture slides",
            
            # Attendance queries (15 examples)
            "attendance", "my attendance", "attendance percentage",
            "how many classes did i miss", "attendance record",
            "check attendance", "attendance status", "present or absent",
            "class attendance", "attendance policy", "minimum attendance",
            "attendance requirement", "absences", "attendance check",
            "how much attendance do i have"
        ]
        
        # Corresponding intents (must match training_questions length)
        self.intents = [
            # Lecture intents (20)
            "lecture", "lecture", "lecture", "lecture", "lecture",
            "lecture", "lecture", "lecture", "lecture", "lecture",
            "lecture", "lecture", "lecture", "lecture", "lecture",
            "lecture", "lecture", "lecture", "lecture", "lecture",
            
            # Grade intents (20)
            "grades", "grades", "grades", "grades", "grades",
            "grades", "grades", "grades", "grades", "grades",
            "grades", "grades", "grades", "grades", "grades",
            "grades", "grades", "grades", "grades", "grades",
            
            # Greeting intents (21)
            "greeting", "greeting", "greeting", "greeting", "greeting",
            "greeting", "greeting", "greeting", "greeting", "greeting",
            "greeting", "greeting", "greeting", "greeting", "greeting",
            "greeting", "greeting", "greeting", "greeting", "greeting",
            "greeting",
            
            # Farewell intents (15)
            "farewell", "farewell", "farewell", "farewell", "farewell",
            "farewell", "farewell", "farewell", "farewell", "farewell",
            "farewell", "farewell", "farewell", "farewell", "farewell",
            
            # Assignment intents (20)
            "assignment", "assignment", "assignment", "assignment", "assignment",
            "assignment", "assignment", "assignment", "assignment", "assignment",
            "assignment", "assignment", "assignment", "assignment", "assignment",
            "assignment", "assignment", "assignment", "assignment", "assignment",
            
            # Help intents (15)
            "help", "help", "help", "help", "help",
            "help", "help", "help", "help", "help",
            "help", "help", "help", "help", "help",
            
            # Office hours intents (15)
            "office_hours", "office_hours", "office_hours", "office_hours", "office_hours",
            "office_hours", "office_hours", "office_hours", "office_hours", "office_hours",
            "office_hours", "office_hours", "office_hours", "office_hours", "office_hours",
            
            # Exam intents (20)
            "exam", "exam", "exam", "exam", "exam",
            "exam", "exam", "exam", "exam", "exam",
            "exam", "exam", "exam", "exam", "exam",
            "exam", "exam", "exam", "exam", "exam",
            
            # Course material intents (15)
            "course_material", "course_material", "course_material", "course_material", "course_material",
            "course_material", "course_material", "course_material", "course_material", "course_material",
            "course_material", "course_material", "course_material", "course_material", "course_material",
            
            # Attendance intents (15)
            "attendance", "attendance", "attendance", "attendance", "attendance",
            "attendance", "attendance", "attendance", "attendance", "attendance",
            "attendance", "attendance", "attendance", "attendance", "attendance"
        ]
        
        # Multiple response variations for each intent
        self.responses = {
            "lecture": [
                "📚 The lecture is scheduled every Monday at 10:00 AM in Room 101.",
                "📚 Classes are held on Mondays at 10:00 AM. See you in Room 101!",
                "📚 Your next lecture: Monday, 10:00 AM, Room 101."
            ],
            "grades": [
                "📊 Your grades will be released next week. Check the student portal!",
                "📊 Results coming next week! Keep an eye on your student portal.",
                "📊 Grades will be posted soon. Check back next week on the portal."
            ],
            "greeting": [
                "👋 Hello! I'm your AI assistant. How can I help you today?",
                "👋 Hi there! Ready to assist with your questions!",
                "👋 Hello! Ask me about lectures, grades, exams, or assignments!"
            ],
            "farewell": [
                "👋 Goodbye! Have a wonderful day ahead!",
                "👋 Take care! See you next time!",
                "👋 Bye! Good luck with your studies!"
            ],
            "assignment": [
                "📝 Assignment due: Friday at 11:59 PM. Submit via the online portal.",
                "📝 Don't forget! Homework deadline is this Friday at 11:59 PM.",
                "📝 Your assignment is due Friday night. Submit it through the portal!"
            ],
            "help": [
                "💡 I can assist you with:\n   ✓ Lecture schedules\n   ✓ Grade information\n   ✓ Assignment deadlines\n   ✓ Exam schedules\n   ✓ Office hours\n   ✓ Course materials\n   ✓ Attendance records\n   \n   Just ask me anything!"
            ],
            "office_hours": [
                "🏢 Office hours: Tuesday & Thursday, 2:00 PM - 4:00 PM in Office 205.",
                "🏢 Professor available: Tue/Thu from 2-4 PM. Office 205.",
                "🏢 You can meet the instructor on Tuesday or Thursday, 2-4 PM, Office 205."
            ],
            "exam": [
                "📝 Midterm exam: December 20th at 9:00 AM. Final exam: January 15th.",
                "📝 Upcoming exams: Midterm on Dec 20 (9 AM), Final on Jan 15.",
                "📝 Exam schedule: Midterm - December 20, Final - January 15. Good luck!"
            ],
            "course_material": [
                "📖 Course materials are available on the learning portal under 'Resources'.",
                "📖 You can find lecture slides and notes in the course portal.",
                "📖 All study materials are uploaded weekly to the online platform."
            ],
            "attendance": [
                "✅ Your attendance is 85%. You need minimum 75% to appear in exams.",
                "✅ Check your attendance record on the student portal.",
                "✅ Attendance policy: Minimum 75% required. Check portal for details."
            ]
        }
        
        # Conversation statistics
        self.conversation_count = 0
        self.intent_stats = {}
        
        # Train the model and get accuracy
        self.model_accuracy = self._train_model()
    
    def _train_model(self):
        """Train the TF-IDF vectorizer and KNN classifier with accuracy measurement"""
        # Configure TF-IDF with optimized parameters
        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 3),  # Increased to capture more context
            max_features=300,     # Increased features
            min_df=1,
            max_df=0.9
        )
        
        # Transform training data
        X = self.vectorizer.fit_transform(self.training_questions)
        y = self.intents
        
        # Split data for accuracy testing
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Train KNN model with better parameters
        self.model = KNeighborsClassifier(
            n_neighbors=5,        # Increased neighbors for better generalization
            weights='distance',
            metric='cosine'
        )
        self.model.fit(X_train, y_train)
        
        # Calculate accuracy
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        return accuracy
    
    def get_response(self, user_input):
        """Predict intent and return appropriate response with confidence checking"""
        if not user_input or not user_input.strip():
            return {
                "response": "⚠️ Please type a valid question!",
                "intent": "error",
                "confidence": 0.0
            }
        
        # Check if input is too short or meaningless
        if len(user_input.strip()) < 2:
            return {
                "response": "🤔 Please ask a complete question!",
                "intent": "unknown",
                "confidence": 0.0
            }
        
        # Check if input is only special characters or numbers
        if not any(c.isalpha() for c in user_input):
            return {
                "response": "🤔 Please type a valid question with words!",
                "intent": "unknown",
                "confidence": 0.0
            }
        
        # Transform user input
        user_vector = self.vectorizer.transform([user_input.lower()])
        
        # Get distances to nearest neighbors
        distances, indices = self.model.kneighbors(user_vector)
        
        # Calculate confidence (inverse of average distance)
        avg_distance = np.mean(distances[0])
        confidence = max(0, 1 - avg_distance)
        
        # Set confidence threshold - LOWERED for better accuracy
        CONFIDENCE_THRESHOLD = 0.15
        
        if confidence < CONFIDENCE_THRESHOLD:
            return {
                "response": "🤔 I'm not sure I understand. Could you rephrase your question? Try asking about lectures, grades, exams, assignments, office hours, course materials, or attendance.",
                "intent": "unknown",
                "confidence": float(confidence)
            }
        
        # Predict intent
        predicted_intent = self.model.predict(user_vector)[0]
        
        # Update statistics
        self.conversation_count += 1
        self.intent_stats[predicted_intent] = self.intent_stats.get(predicted_intent, 0) + 1
        
        # Get response (random selection from multiple variations)
        import random
        if predicted_intent in self.responses:
            response_text = random.choice(self.responses[predicted_intent])
        else:
            response_text = "🤔 I'm not sure about that. Try asking about lectures, grades, exams, or assignments!"
        
        return {
            "response": response_text,
            "intent": predicted_intent,
            "confidence": float(confidence)
        }
    
    def get_greeting(self):
        """Return time-based greeting"""
        hour = datetime.now().hour
        if 5 <= hour < 12:
            time_greeting = "Good morning"
        elif 12 <= hour < 18:
            time_greeting = "Good afternoon"
        else:
            time_greeting = "Good evening"
        
        return f"{time_greeting}! Welcome to the Student Assistant Chatbot! 🎓"
    
    def get_statistics(self):
        """Get chatbot statistics"""
        return {
            "conversation_count": self.conversation_count,
            "model_accuracy": float(self.model_accuracy),
            "training_examples": len(self.training_questions),
            "total_intents": len(set(self.intents)),
            "intent_stats": self.intent_stats
        }
    
    def get_available_intents(self):
        """Get list of available intents with descriptions"""
        return {
            "lecture": "Information about lecture schedules and timings",
            "grades": "Information about grades and results",
            "greeting": "Greeting and welcome messages",
            "farewell": "Goodbye and farewell messages",
            "assignment": "Information about assignments and deadlines",
            "help": "Help and available commands",
            "office_hours": "Information about office hours and meetings",
            "exam": "Information about exams and tests",
            "course_material": "Information about study materials and resources",
            "attendance": "Information about attendance records and policies"
        }
    
    def show_statistics(self):
        """Display conversation statistics in terminal"""
        print("\n" + "=" * 65)
        print("📊 CONVERSATION STATISTICS")
        print("=" * 65)
        print(f"Total questions asked: {self.conversation_count}")
        print(f"Training data size: {len(self.training_questions)} examples")
        
        if self.intent_stats:
            print("\n📈 Topics discussed:")
            sorted_stats = sorted(self.intent_stats.items(), key=lambda x: x[1], reverse=True)
            for intent, count in sorted_stats:
                print(f"   • {intent.capitalize()}: {count} question(s)")
        
        print("=" * 65)
    
    def run_cli(self):
        """Run chatbot in command line interface mode"""
        print("=" * 65)
        print("🤖 INTELLIGENT STUDENT ASSISTANT - ML POWERED CHATBOT")
        print("=" * 65)
        print(self.get_greeting())
        print(f"\n📚 Training Examples: {len(self.training_questions)}")
        print(f"🎓 Total Intents: {len(set(self.intents))}")
        print("\n💬 Commands: 'stats' for statistics | 'bye' to exit")
        print("=" * 65 + "\n")
        
        while True:
            try:
                # Get user input
                user_input = input("You: ").strip()
                
                # Handle empty input
                if not user_input:
                    print("Bot: Please type something! 😊\n")
                    continue
                
                # Check for statistics command
                if user_input.lower() == "stats":
                    self.show_statistics()
                    print()
                    continue
                
                # Get bot response
                result = self.get_response(user_input)
                print(f"Bot: {result['response']}\n")
                
                # Exit condition
                if user_input.lower() in ["bye", "goodbye", "exit", "quit", "see you"]:
                    self.show_statistics()
                    break
                    
            except KeyboardInterrupt:
                print("\n\nBot: 👋 Goodbye! Have a great day!")
                self.show_statistics()
                break
            except Exception as e:
                print(f"Bot: ⚠️ An error occurred: {str(e)}\n")
        
        print("\n" + "=" * 65)
        print("Thank you for using the Student Assistant Chatbot! 🎓")
        print("=" * 65)


# ==================== Main Execution ====================

if __name__ == "__main__":
    # When run directly, start CLI mode
    print("\n🚀 Initializing Student Chatbot...\n")
    chatbot = StudentChatbot()
    print("✅ Chatbot ready!\n")
    chatbot.run_cli()