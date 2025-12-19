import React from "react";

const QuickQuestions = ({ messages, onQuickQuestion }) => {
  const quickQuestions = [
    "📚 When is the lecture?",
    "📊 What are my grades?",
    "📝 Tell me about assignments",
    "💡 Help me",
  ];

  if (messages.length > 1) return null;

  return (
    <div className="px-6 py-3 border-t border-gray-200 bg-gray-50">
      <p className="text-xs text-gray-500 mb-2 font-medium">Quick Questions:</p>
      <div className="flex flex-wrap gap-2">
        {quickQuestions.map((question, index) => (
          <button
            key={index}
            onClick={() => onQuickQuestion(question)}
            className="px-3 py-1.5 text-xs bg-white border border-indigo-200 text-indigo-700 rounded-full hover:bg-indigo-50 hover:border-indigo-300 transition-all duration-200 shadow-sm hover:shadow"
          >
            {question}
          </button>
        ))}
      </div>
    </div>
  );
};

export default QuickQuestions;
