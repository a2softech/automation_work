# 🚀 Daily File Automation (`automation_work`)

This repository contains a GitHub Actions workflow that automatically generates a daily log file without requiring any manual intervention. 

## 📌 What does it do?
- Automatically runs a scheduled job every day at 12:00 AM UTC (5:30 AM IST).
- Creates a new text file formatted as `file_DD-MM-YYYY.txt` (e.g., `file_24-04-2026.txt`).
- Writes the content `Today date is DD-MM-YYYY` inside the file.
- Uses a **Zero-Warning API approach** to ensure clean and fast execution.

## 🛠️ How it works
This project uses **GitHub Actions** located in `.github/workflows/`. 

Instead of traditional `actions/checkout` and Git commands (which can cause Node.js deprecation warnings), this workflow uses a direct `curl` request to the **GitHub REST API** to create the file. 

**Benefits of this approach:**
1. **Zero Warnings:** Completely bypasses Node.js runner deprecation warnings.
2. **Lightning Fast:** Skips repository cloning and Git overhead.
3. **100% Free:** Uses standard GitHub Actions compute which easily fits in the free tier.

## ⚙️ Important Setup (Permissions)
For this workflow to run successfully, it needs permission to write to the repository. 

If replicating this project, make sure to enable these settings:
1. Go to your repository's **Settings**.
2. On the left sidebar, click on **Actions** > **General**.
3. Scroll down to **Workflow permissions**.
4. Select **"Read and write permissions"**.
5. Click **Save**.

---
*Automated securely using GitHub Actions and GitHub REST API.*
