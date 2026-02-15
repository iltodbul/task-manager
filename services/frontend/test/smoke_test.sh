#!/bin/bash
echo "🔍 Starting Frontend Smoke Test..."

# Allow overriding host/port via env: HOST (default localhost), PORT (default 80)
HOST=${HOST:-localhost}
PORT=${PORT:-80}

# 1. Check if Nginx is serving the page
STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://$HOST:$PORT)
if [ "$STATUS" -eq 200 ]; then
    echo "✅ [PASS] Nginx is up."
else
    echo "❌ [FAIL] Nginx is down (Status: $STATUS)"
    exit 1
fi

# 2. Check if the Task List container exists in the HTML
if curl -s http://$HOST:$PORT | grep -q 'id="task-list"'; then
    echo "✅ [PASS] Task List container found in DOM."
else
    echo "❌ [FAIL] Missing #task-list element. UI will not render tasks."
    exit 1
fi

# 3. Check page title is present
if curl -s http://$HOST:$PORT | grep -q '<h1>Microservice Task Tracker</h1>'; then
    echo "✅ [PASS] Page title found."
else
    echo "❌ [FAIL] Missing page title 'Microservice Task Tracker'."
    exit 1
fi

# 4. Check for Add Task form inputs (title, priority, date)
HTML=$(curl -s http://$HOST:$PORT)
if echo "$HTML" | grep -q 'id="title"' && echo "$HTML" | grep -q 'id="priority"' && echo "$HTML" | grep -q 'id="date"'; then
    echo "✅ [PASS] Add Task inputs found (title, priority, date)."
else
    echo "❌ [FAIL] One or more Add Task inputs missing (#title, #priority, #date)."
    exit 1
fi
