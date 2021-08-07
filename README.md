# notion-scripts

This repository simplifies nerve-racking tasks in notion, e. g. creating recurring entries in databases. 

## How To

1. Create an internal notion integration in the [notion developer portal](https://developers.notion.com/).
2. Invite the integration to the page you want it to modify.
3. Clone the repository.
4. Add `NOTION_API_KEY = 'YOUR_INTEGRATION_KEY'` to a file named `secrets.py`.
5. You are ready to go.

## Different Scripts
- `recurring_entries.py` - Adds a recurring entry to a database of your choice. The only difference between the entries are the date properties. Specify the changing dae property, an interval and the number of iterations.
