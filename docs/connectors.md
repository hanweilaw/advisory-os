# Connectors

The OS works with no connectors. Each one is an upgrade.

| Connector | Used by | Adds |
|---|---|---|
| Google Calendar or Outlook | `/meeting-prep`, `/pipeline` | finds today's client meetings and preps each |
| Gmail or Outlook | `/client-email` | saves drafts straight into your mailbox (never sends) |
| Google Drive or OneDrive | client skills | reads client folders where they already live |
| Notion or a CRM | `/pipeline` | prospects and follow-ups from your CRM |

## Two ways to connect

1. **In the Claude app** (simplest): Settings → Connectors, add Gmail, Google Calendar, Google Drive or Notion. Claude Code sessions signed in to the same account can use them.
2. **In this folder**: copy `.mcp.json.example` to `.mcp.json` (gitignored) and add an MCP server your provider documents. Run `/mcp` in Claude Code to check it's connected.

## Before you connect

- A synced folder on your computer (OneDrive, Google Drive for desktop) needs no connector: set `client_root` to its path.
- Check that your firm allows the service to be used with client data.
- Keep "send" out of every skill. Drafts only.
