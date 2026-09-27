Run reminders setup

1. Add the following repository secrets:
   - RUN_REMINDERS_URL: full URL to the endpoint, e.g. https://your-host/api/notifications/internal/run-reminders
   - RUN_REMINDERS_TOKEN: a bearer token with admin privileges to call the internal endpoint

2. Test locally with curl:

curl -X POST "$RUN_REMINDERS_URL" -H "Authorization: Bearer $RUN_REMINDERS_TOKEN"

3. The workflow runs daily at 08:00 UTC and can be triggered manually via "Run workflow" in Actions.
