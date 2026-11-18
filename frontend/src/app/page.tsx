"use client";

import { useState } from "react";

export default function Home() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  

   const sendMessage = async () => {
  try {
   const res = await fetch(
  "http://127.0.0.1:8000/chat",
  {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message: message,
    }),
  }
);

    if (!res.ok) {
      const txt = await res.text();
      setResponse("ERREUR BACKEND : " + txt);
      return;
    }

    const data = await res.json();
    setResponse(data.response);
  } catch (error) {
    setResponse("Erreur de connexion au backend");
    console.error(error);
  }
};

  return (
    <main className="p-8">
      <h1 className="text-4xl font-bold mb-4">
        AI Enterprise OS
      </h1>

      <textarea
        className="border w-full p-2"
        rows={4}
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <button
        onClick={sendMessage}
        className="bg-blue-600 text-white px-4 py-2 mt-4"
      >
        Envoyer
      </button>

      <div className="mt-4 border p-4 min-h-[120px]">
        {response}
      </div>
    </main>
  );
}