# Connectors

The OS works with no connectors. Each one is an optional upgrade, and none of them ever holds client files.

| Connector | Used by | Adds | Client data allowed |
|---|---|---|---|
| Google Calendar or Outlook | `/meeting-prep`, `/pipeline` | finds today's client meetings and preps each | meeting title and time only |
| Gmail or Outlook | `/client-email` | saves drafts straight into your mailbox (never sends) | the email text; no attachments from the client folder, no ID, account or medical details |

**Not for client data:** cloud storage (OneDrive, Google Drive, Dropbox, iCloud, Box) and note or CRM tools (Notion and similar). Client folders stay on your computer; that's the local-only rule in `CLAUDE.md` and `knowledge/markets/singapore/pdpa.md`. If you use a CRM, keep only what your firm approves there and don't connect it to client documents.

## Two ways to connect

1. **In the Claude app** (simplest): Settings → Connectors, add Google Calendar or Gmail. Claude Code sessions signed in to the same account can use them.
2. **In this folder**: copy `.mcp.json.example` to `.mcp.json` (gitignored) and add an MCP server your provider documents. Run `/mcp` in Claude Code to check it's connected.

## Before you connect

- Check that your firm allows the service to be used with client information.
- Keep "send" out of every skill. Drafts only.
