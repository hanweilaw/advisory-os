---
name: organize-client
description: Use when a client folder is messy and the adviser says "organise", "tidy", "clean up", "sort" or "restructure" a client folder, or "/organize-client". Proposes a move plan into the 00-09 slots, applies it after approval, renames with date prefixes, and verifies nothing was lost.
argument-hint: "\"Client name\" or <folder path>"
---

# Organise a client folder

## Step 1: Inventory (read-only)

List every file with size and modified date. Count them. Flag exact duplicates (same size and content hash) and near-duplicates (same name with "copy", "(1)", "final final").

## Step 2: Plan

Create any missing slots from `clients/_TEMPLATE/`. For each file, propose a slot and a new name `YYYY-MM-DD_Description.ext` (date from the document if visible, else the file's modified date, marked `~`). Superseded versions go to `09_Review History/Superseded/`. Show the plan as a table: current path → new path, reason. Do not move anything yet.

## Step 3: Apply on approval

Move (never delete) files. Duplicates go to `09_Review History/Superseded/Duplicates/` rather than the bin. Keep a move log at `00_Admin and Meeting Notes/YYYY-MM-DD_Reorganisation log.md`.

## Step 4: Verify

Re-count files: total after must equal total before. List any file that is unaccounted for. Report counts per slot.
