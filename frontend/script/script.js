import {
  createNewSessionId,
  getSessionId,
  removeGreeting,
} from "./util/utils.js";
import { fetchSessionChatHistory, initChatHistory } from "./chatHistory.js";
window.createNewChatSession = createNewChatSession;

function initialize() {
  console.log(getSessionId());
  if (getSessionId() == null) {
    createNewChatSession();
    return;
  }

  const webSocket = new WebSocket("ws://localhost:8000/stream");

  webSocket.onopen = () => {
    console.log("WebSocket Connection Established");
  };

  webSocket.onclose = () => {
    console.log("WebSocket Connection Closed");
  };

  let currentMessageElement = null;

  webSocket.onmessage = (ev) => {
    if (ev.data) {
      const messageContainer = document.querySelector(".message-container-js");
      if (!currentMessageElement) {
        currentMessageElement = document.createElement("div");
        currentMessageElement.classList.add("ai-message");
        messageContainer.appendChild(currentMessageElement);
      }

      currentMessageElement.textContent += ev.data;

      scrollToBottom();
    }
  };

  webSocket.onclose = () => {
    console.log("WebSocket Connection Closed");
    currentMessageElement = null;
  };

  initChatHistory();

  const menuToggle = document.getElementById("menuToggle");
  const sidebar = document.getElementById("sidebar");
  const backdrop = document.getElementById("backdrop");
  const sendButton = document.querySelector(".send-button-js");
  const messageInput = document.querySelector(".message-input-js");
  const messageContainer = document.querySelector(".message-container-js");

  menuToggle.addEventListener("click", () => {
    sidebar.classList.toggle("active");
    backdrop.classList.toggle("active");
  });

  backdrop.addEventListener("click", () => {
    sidebar.classList.remove("active");
    backdrop.classList.remove("active");
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth > 768) {
      sidebar.classList.remove("active");
      backdrop.classList.remove("active");
    }
  });

  function sendMessage() {
    const value = messageInput.value;
    if (value.trim() !== "") {
      const userMessageElement = document.createElement("div");
      userMessageElement.classList.add("human-message");
      userMessageElement.textContent = value;
      messageContainer.appendChild(userMessageElement);

      webSocket.send(
        JSON.stringify({ question: value, sessionId: getSessionId() })
      );

      messageInput.value = "";
      currentMessageElement = null;
      removeGreeting();
      scrollToBottom();
    }
  }

  function scrollToBottom() {
    const container = document.querySelector(".message-container-js");
    container.scrollTop = container.scrollHeight;
  }

  sendButton.addEventListener("click", sendMessage);

  messageInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  });

  messageContainer.innerHTML = "";
}

function createNewChatSession() {
  createNewSessionId();
  fetchSessionChatHistory();
}

initialize();
