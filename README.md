# notion-scripts

This repository simplifies nerve-racking tasks in notion, e. g. creating recurring entries in databases. 

## How To

1. Create an internal notion integration in the [notion developer portal](https://developers.notion.com/).
2. Invite the integration to the page you want it to modify.
3. Clone the repository.
4. Add `NOTION_API_KEY = 'YOUR_INTEGRATION_KEY'` to a file named `secrets.py`.
5. You are ready to go.

## Different Scripts
- `recurring_events.py` - Adds a recurring event to a database of your choice. You choose the interval and how often the event recurs.
