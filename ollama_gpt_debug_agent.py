
import subprocess
import time
import os
from tools import gpt_fix_rewriter

BOT_SCRIPT = "zillow_scraper_main.py"
LEAD_LOG = "zillow_log.txt"
MAX_ATTEMPTS = 3

def run_bot():
    print("\n🚀 Running the Zillow bot...")
    result = subprocess.run(["python3", BOT_SCRIPT], capture_output=True, text=True)
    print(result.stdout)
    return result.stdout

def found_leads(output):
    return "Scraped 0 total leads" not in output

def fix_scraper():
    print("\n🤖 Calling GPT to fix the scraper...")
    subprocess.run(["python3", "tools/gpt_fix_rewriter.py"])

def replace_scrape_fsbo():
    fix_path = "fix_suggestions/scraper_fix_suggestion.txt"
    target_path = "zillow_scraper_main.py"
    with open(fix_path, "r") as fix_file:
        fix_code = fix_file.read()
    with open(target_path, "r") as f:
        lines = f.readlines()
    start, end = None, None
    for i, line in enumerate(lines):
        if "def scrape_fsbo" in line:
            start = i
        if start and line.strip() == "return results":
            end = i + 1
            break
    if start is not None and end is not None:
        lines[start:end] = [fix_code + "\n"]
        with open(target_path, "w") as f:
            f.writelines(lines)
        print("✅ Patched zillow_scraper_main.py with updated scrape_fsbo()")

def main():
    for attempt in range(MAX_ATTEMPTS):
        print(f"\n⚙️ Attempt {attempt + 1} of {MAX_ATTEMPTS}")
        output = run_bot()
        if found_leads(output):
            print("✅ Leads found, exiting loop.")
            break
        else:
            print("❌ No leads found. Attempting fix...")
            fix_scraper()
            replace_scrape_fsbo()
            time.sleep(2)
    else:
        print("🛑 Max retries reached. Still no leads.")

if __name__ == "__main__":
    main()
