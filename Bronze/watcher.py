import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class MarkdownHandler(FileSystemEventHandler):
    """
    Handles file system events for markdown files
    """
    def on_created(self, event):
        # Check if the created file is a markdown file
        if not event.is_directory and event.src_path.endswith('.md'):
            print(f"New markdown file detected: {event.src_path}")
            
            # Convert to absolute path to ensure we can read the file
            abs_path = os.path.abspath(event.src_path)
            print(f"Absolute path: {abs_path}")
            
            # Multiple attempts to read the file with delays to handle race conditions
            content = ""
            max_retries = 5
            retry_count = 0
            
            while retry_count < max_retries:
                try:
                    with open(abs_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        print(f"Attempt {retry_count + 1}: File content length: {len(content)}")
                        
                        # If we got content, break out of the loop
                        if len(content) > 0:
                            print(f"Content preview: {content[:100]}...")
                            break
                        else:
                            print(f"Attempt {retry_count + 1}: File is empty, retrying...")
                            retry_count += 1
                            time.sleep(1)
                            
                except FileNotFoundError:
                    print(f"Attempt {retry_count + 1}: File not found: {abs_path}")
                    retry_count += 1
                    time.sleep(1)
                except Exception as e:
                    print(f"Attempt {retry_count + 1}: Error reading file: {str(e)}")
                    retry_count += 1
                    time.sleep(1)
            
            # If we still have no content after retries, note it
            if len(content) == 0:
                content = "ERROR: Could not read file content after multiple attempts"
                print("Failed to read content after all retries")
            
            # Generate a response based on the content
            response_title = f"Response to: {os.path.basename(event.src_path)}"
            response_summary = f"This is an automated response to the document '{os.path.basename(event.src_path)}'.\n\nOriginal content:\n{content}\n\nAI Summary: This document has been processed and requires action."
            
            # Create the response file in Needs_Action folder
            response_filename = f"response_{os.path.basename(event.src_path)}"
            response_path = os.path.join("vault", "Needs_Action", response_filename)
            
            with open(response_path, 'w', encoding='utf-8') as response_file:
                response_file.write(f"# {response_title}\n\n")
                response_file.write(f"## Summary\n{response_summary}\n\n")
                response_file.write(f"## Action Items\n- Review the original document\n- Determine next steps\n- Move to Done when completed\n")
            
            print(f"Response created: {response_path}")
            
            # Move the original file to the Done folder after processing
            import shutil
            done_folder = os.path.join("vault", "Done")
            done_path = os.path.join(done_folder, os.path.basename(event.src_path))
            shutil.move(event.src_path, done_path)
            print(f"Original file moved to Done: {done_path}")

def start_watching():
    """
    Starts watching the vault/Inbox directory for new markdown files
    """
    # Define the directory to watch
    watch_directory = os.path.join("vault", "Inbox")
    
    # Create the event handler and observer
    event_handler = MarkdownHandler()
    observer = Observer()
    observer.schedule(event_handler, watch_directory, recursive=False)
    
    # Start the observer
    observer.start()
    print(f"Started watching {watch_directory} for new markdown files...")
    
    try:
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Stop the observer when interrupted
        observer.stop()
        print("\nStopped watching.")
    
    observer.join()

if __name__ == "__main__":
    # Ensure the target directories exist
    os.makedirs(os.path.join("vault", "Inbox"), exist_ok=True)
    os.makedirs(os.path.join("vault", "Needs_Action"), exist_ok=True)
    os.makedirs(os.path.join("vault", "Done"), exist_ok=True)
    
    start_watching()