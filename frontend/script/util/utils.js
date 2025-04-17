import { v4 as uuidv4 } from "https://cdn.jsdelivr.net/npm/uuid@9.0.0/dist/esm-browser/index.js";

export function removeGreeting() {
  const welcomeText = document.querySelector(".welcome-text-js");
  if (welcomeText) {
    welcomeText.style.display = "none";
  }
}

export function addWelcomeText() {
    const welcomeText = document.querySelector(".welcome-text-js");
    if (welcomeText) {
        welcomeText.textContent = "What can I help with?";
        welcomeText.style.display = "block";
    }
}

export function getSessionId() {
    const searchParam = new URLSearchParams(window.location.search);
    return searchParam.get("sessionId");
}


export function createNewSessionId() {
    const newSessionId = uuidv4();
    window.location.href = `?sessionId=${encodeURIComponent(newSessionId)}`;
}

export function truncateString(str, maxLength) {
    if (str.length > maxLength) {
        return str.slice(0, maxLength) + "...";
    }
    console.log(str);
    return str;
}