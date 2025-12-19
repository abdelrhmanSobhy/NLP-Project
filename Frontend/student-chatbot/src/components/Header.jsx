import React from "react";
import { Bot, Sparkles, TrendingUp } from "lucide-react";

const Header = ({ stats }) => {
  return (
    <div className="bg-white rounded-2xl shadow-lg p-6 mb-6 border border-indigo-100">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="bg-gradient-to-br from-indigo-500 to-purple-600 p-3 rounded-xl">
            <Bot className="w-8 h-8 text-white" />
          </div>
          <div>
            <h1 className="text-2xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">
              Student Assistant AI
            </h1>
            <p className="text-sm text-gray-600">Powered by Machine Learning</p>
          </div>
        </div>

        {stats && (
          <div className="hidden md:flex items-center gap-4 text-sm">
            <div className="flex items-center gap-2 bg-indigo-50 px-3 py-2 rounded-lg">
              <Sparkles className="w-4 h-4 text-indigo-600" />
              <span className="text-gray-700">
                {stats.total_intents} Intents
              </span>
            </div>
            <div className="flex items-center gap-2 bg-purple-50 px-3 py-2 rounded-lg">
              <TrendingUp className="w-4 h-4 text-purple-600" />
              <span className="text-gray-700">{stats.model_type}</span>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Header;
