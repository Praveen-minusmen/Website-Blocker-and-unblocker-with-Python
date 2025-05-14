# Website-Blocker-and-unblocker-with-Python

A simple Python script to block distracting websites by modifying your system's hosts file. This tool helps you stay focused by redirecting specified websites to your local machine (127.0.0.1), effectively preventing access to them.

## Features

- Blocks a customizable list of popular distracting websites.
- Works on both Windows and Linux.
- Easy to use and modify.

## How It Works

The script edits your system's `hosts` file to redirect specified websites to `127.0.0.1` (localhost). When you try to visit a blocked website, your browser will be unable to load it.

## Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/website-blocker.git
   cd website-blocker
   ```

2. **Edit the list of websites:**
   - Open `website_blocker.py` in a text editor.
   - Modify the `websites` list to include or remove sites as needed.

3. **Run the script as administrator:**
   - **Windows:** Right-click your terminal and select "Run as administrator".
   - **Linux:** Use `sudo` to run the script.

   ```bash
   python website_blocker.py
   ```

## Important Notes

- **Administrator/root privileges are required** to modify the hosts file.
- Changes take effect immediately, but you may need to clear your browser cache or restart your browser.
- To unblock the websites, manually remove the corresponding lines from your hosts file.

## Disclaimer

Use this script responsibly. Modifying system files can affect your computer's behavior. Always back up your hosts file before making changes.

## License

This project is licensed under the MIT License.
