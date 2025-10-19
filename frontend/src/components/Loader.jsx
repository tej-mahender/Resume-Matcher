import React from "react";

export default function Loader() {
  return (
    <div className="flex flex-col items-center mt-4">
      <svg
        className="w-10 h-10 animate-spin text-slate-600"
        viewBox="0 0 24 24"
      >
        <circle
          cx="12"
          cy="12"
          r="10"
          stroke="currentColor"
          strokeWidth="4"
          fill="none"
        />
      </svg>
      <span className="mt-2 text-slate-600 text-sm">Processing...</span>
    </div>
  );
}
