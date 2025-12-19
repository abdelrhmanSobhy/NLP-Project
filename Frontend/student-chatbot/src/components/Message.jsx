import React from "react";
import { Bot, User, Clock } from "lucide-react";

const Message = ({ message }) => {
  return (
    <div
      className={`flex gap-3 ${
        message.type === "user" ? "justify-end" : "justify-start"
      }`}
    >
      {message.type === "bot" && (
        <div className="flex-shrink-0">
          <div className="w-10 h-10 rounded-full bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center">
            <Bot className="w-6 h-6 text-white" />
          </div>
        </div>
      )}

      <div className={`max-w-md ${message.type === "user" ? "order-1" : ""}`}>
        <div
          className={`px-4 py-3 rounded-2xl shadow-sm ${
            message.type === "user"
              ? "bg-gradient-to-r from-indigo-600 to-purple-600 text-white rounded-tr-sm"
              : "bg-white border border-gray-200 text-gray-800 rounded-tl-sm"
          }`}
        >
          <p className="text-sm leading-relaxed whitespace-pre-line">
            {message.text}
          </p>

          {message.type === "bot" &&
            message.intent &&
            message.intent !== "error" && (
              <div className="mt-2 pt-2 border-t border-gray-100 flex items-center gap-2 text-xs text-gray-500">
                <span className="px-2 py-1 bg-indigo-50 text-indigo-600 rounded-full font-medium">
                  {message.intent}
                </span>
                {message.confidence && (
                  <span className="text-gray-400">
                    {(message.confidence * 100).toFixed(0)}% confidence
                  </span>
                )}
              </div>
            )}
        </div>

        <div
          className={`flex items-center gap-1 mt-1 text-xs text-gray-400 ${
            message.type === "user" ? "justify-end" : ""
          }`}
        >
          <Clock className="w-3 h-3" />
          <span>{new Date(message.timestamp).toLocaleTimeString()}</span>
        </div>
      </div>

      {message.type === "user" && (
        <div className="shrink-0">
          <div className="w-10 h-10 rounded-full bg-linear-to-br from-gray-600 to-gray-800 flex items-center justify-center">
            <User className="w-6 h-6 text-white" />
          </div>
        </div>
      )}
    </div>
  );
};

export default Message;
