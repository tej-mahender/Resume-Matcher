import React from "react";

export default function UploadResume({ file, setFile }) {
  return (
    <div>
      <label className="block text-sm font-medium text-slate-700">
        Resume File
      </label>
      <input
        type="file"
        accept=".pdf,.doc,.docx,.txt"
        className="mt-2 block w-full"
        onChange={(e) => setFile(e.target.files[0] || null)}
      />
      {file && (
        <div className="mt-2 text-sm text-slate-600">
          Selected file: {file.name}
        </div>
      )}
    </div>
  );
}
