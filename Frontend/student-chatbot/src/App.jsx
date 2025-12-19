import React, { useState, useEffect } from "react";
import Header from "./components/Header";
import MessageList from "./components/MessageList";
import QuickQuestions from "./components/QuickQuestions";
import MessageInput from "./components/MessageInput";
import Footer from "./components/Footer";

const API_BASE_URL = "http://localhost:5000/api";

export default function ChatbotApp() {
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [greeting, setGreeting] = useState("");
  const [stats, setStats] = useState(null);

  useEffect(() => {
    fetchGreeting();
    fetchStats();
  }, []);

  const fetchGreeting = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/greeting`);
      const data = await response.json();
      if (data.success) {
        setGreeting(data.greeting);
        setMessages([
          {
            type: "bot",
            text: data.greeting,
            intent: "greeting",
            timestamp: new Date().toISOString(),
          },
        ]);
      }
    } catch (error) {
      console.error("Error fetching greeting:", error);
      setGreeting("Welcome to Student Assistant Chatbot! 🎓");
    }
  };

  const fetchStats = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/stats`);
      const data = await response.json();
      if (data.success) {
        setStats(data.stats);
      }
    } catch (error) {
      console.error("Error fetching stats:", error);
    }
  };

  const sendMessage = async () => {
    if (!inputMessage.trim()) return;

    const userMessage = {
      type: "user",
      text: inputMessage,
      timestamp: new Date().toISOString(),
    };

    setMessages((prev) => [...prev, userMessage]);
    const messageToSend = inputMessage;
    setInputMessage("");
    setIsLoading(true);

    try {
      const response = await fetch(`${API_BASE_URL}/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: messageToSend }),
      });

      const data = await response.json();

      if (data.success) {
        const botMessage = {
          type: "bot",
          text: data.bot_response,
          intent: data.intent,
          confidence: data.confidence,
          timestamp: data.timestamp,
        };
        setMessages((prev) => [...prev, botMessage]);
      } else {
        throw new Error(data.error);
      }
    } catch (error) {
      const errorMessage = {
        type: "bot",
        text: "❌ Sorry, I encountered an error. Please make sure the API server is running on http://localhost:5000",
        intent: "error",
        timestamp: new Date().toISOString(),
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const handleQuickQuestion = (question) => {
    setInputMessage(question);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 p-4">
      <div className="max-w-5xl mx-auto">
        <Header stats={stats} />

        {/* Main Chat Container */}
        <div
          className="bg-white rounded-2xl shadow-lg border border-indigo-100 overflow-hidden flex flex-col"
          style={{ height: "600px" }}
        >
          <MessageList messages={messages} isLoading={isLoading} />
          <QuickQuestions
            messages={messages}
            onQuickQuestion={handleQuickQuestion}
          />
          <MessageInput
            inputMessage={inputMessage}
            setInputMessage={setInputMessage}
            onSendMessage={sendMessage}
            isLoading={isLoading}
            onKeyPress={handleKeyPress}
          />
        </div>

        <Footer />
      </div>
    </div>
  );
}
