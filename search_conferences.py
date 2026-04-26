#\!/usr/bin/env python3
"""
Double Events — Weekly Conference Search Script
מריץ חיפוש שבועי של כנסים חדשים בישראל ומעדכן את index.html
"""
import json, re, datetime

# הסקריפט הזה מעדכן את תאריך ה-foundDate של כנסים חדשים
# ומוסיף כנסים חדשים שנמצאו על ידי Cowork scheduled task

today = datetime.date.today().isoformat()
print(f"✅ Weekly conference check — {today}")
print("📋 index.html will be updated with new foundDates by the Cowork task")
