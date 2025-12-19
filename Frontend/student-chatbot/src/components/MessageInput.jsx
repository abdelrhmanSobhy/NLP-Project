import React from "react";
import { Send } from "lucide-react";

const MessageInput = ({
  inputMessage,
  setInputMessage,
  onSendMessage,
  isLoading,
  onKeyPress,
}) => {
  return (
    <div className="p-4 bg-white border-t border-gray-200">
      <div className="flex gap-3">
        <input
          type="text"
          value={inputMessage}
          onChange={(e) => setInputMessage(e.target.value)}
          onKeyPress={onKeyPress}
          placeholder="Type your message here..."
          className="flex-1 px-4 py-3 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent text-gray-800 placeholder-gray-400"
          disabled={isLoading}
        />
        <button
          onClick={onSendMessage}
          disabled={isLoading || !inputMessage.trim()}
          className="px-6 py-3 bg-gradient-to-r from-indigo-600 to-purple-600 text-white rounded-xl hover:from-indigo-700 hover:to-purple-700 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 shadow-lg hover:shadow-xl flex items-center gap-2 font-medium"
        >
          <Send className="w-5 h-5" />
          <span className="hidden sm:inline">Send</span>
        </button>
      </div>
    </div>
  );
};

export default MessageInput;
