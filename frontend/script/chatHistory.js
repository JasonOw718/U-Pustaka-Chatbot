import { addWelcomeText, getSessionId, removeGreeting, truncateString } from "./util/utils.js";


async function fetchAllChatHistory() {
  try {
    const response = await fetch("http://localhost:8000/chat-history");
    const data = await response.json();
    const historyContainer = document.querySelector(".history-container-js");
    let html = ``;
    for (const sessionId in data.all_chat_history) {
      html += `
    <button 
      class="history-item" 
      onclick="window.location.href='?sessionId=${encodeURIComponent(
        sessionId
      )}'">
      Session Id: ${truncateString(sessionId,18)}
    </button>`;
    }

    historyContainer.innerHTML = html;
  } catch (err) {
    console.log(err.message);
  }
}

export async function fetchSessionChatHistory() {
  try {
    
    const response = await fetch(
      `http://localhost:8000/chat-history/${getSessionId()}`
    );
    const data = await response.json();
    const messageContainer = document.querySelector(".message-container-js");
    removeGreeting();

    let html = ``;
    for (const content of data.chat_history) {
      if (content.type === "ai")
        html += `<div class="ai-message">${content.content}</div>`;
      else html += `<div class="human-message">${content.content}</div>`;
    }

    if (html) messageContainer.innerHTML = html;
    else {
      addWelcomeText();
    }
  } catch (err) {
    console.log(err.message);
  }
}

export function initChatHistory() {
  fetchAllChatHistory();
  fetchSessionChatHistory();
}
