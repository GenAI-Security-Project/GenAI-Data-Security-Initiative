// Fixture Node service — INTENTIONALLY VULNERABLE. Fake values only. Never deploy.
// Covers the JS ecosystem:
//   - DSGAI02: hardcoded fake Slack bot token (caught by P02.9 in PR-11 / gitleaks in PR-10;
//     v0.2 DSGAI globs do not include *.js, so this is a tracked known false negative).
//   - DSGAI20: unauthenticated, unthrottled /chat endpoint (P20.5 without P20.1/P20.2;
//     JS ecosystem coverage lands in PR-15).
const express = require("express");
const app = express();

// DSGAI02 — hardcoded Slack bot token (fake). Assigned to an arbitrary variable name.
const SLACK_BOT_TOKEN = "xoxb-FAKE0000000000-FAKE0000000000-FAKEfake0000000000fake00";

app.post("/chat", (req, res) => {
  // No auth, no rate limit — DSGAI20 FAIL.
  res.json({ reply: "ok" });
});

app.listen(3000);
