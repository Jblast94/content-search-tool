import tkinter as tk
from tkinter import messagebox
import logging
from typing import Dict, List
from dataclasses import dataclass
from search_tool import search_data as actual_search_data

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Custom exceptions
class SearchError(Exception):
    pass

class UIError(Exception):
    pass

@dataclass
class SearchResult:
    text: str
    source: str

def validate_query(query: str) -> bool:
    """Validate search query parameters"""
    MAX_QUERY_LENGTH = 100
    return bool(query and len(query.strip()) <= MAX_QUERY_LENGTH)

def search_data(query: str) -> Dict[str, List[SearchResult]]:
    """Implement actual search functionality"""
    try:
        raw_results = actual_search_data(query)
        search_results = {}
        for source, results in raw_results.items():
            search_results[source] = [SearchResult(text=result.text, source=source) for result in results]
        return search_results
    except Exception as e:
        logger.error(f"Search failed: {str(e)}")
        raise SearchError(f"Search operation failed: {str(e)}")

def create_result_window(parent: tk.Tk) -> tk.Toplevel:
    """Create and configure result window with error handling"""
    try:
        window = tk.Toplevel(parent)
        window.title("Search Results")
        window.minsize(300, 200)
        return window
    except Exception as e:
        logger.error(f"Failed to create result window: {str(e)}")
        raise UIError("Could not create results window")

def clear_results(window: tk.Toplevel):
    """Clear previous search results from the result window"""
    for widget in window.winfo_children():
        widget.destroy()

def search_data_ui():
    """Main search UI handler with comprehensive error handling"""
    try:
        query = entry.get().strip()
        
        if not validate_query(query):
            messagebox.showwarning(
                "Invalid Input",
                "Please enter a valid search query (1-100 characters)."
            )
            return

        search_results = search_data(query)
        
        if not search_results:
            messagebox.showinfo("No Results", "No matches found for your search.")
            return
            
        result_window = create_result_window(root)
        clear_results(result_window)  # Clear previous results
        
        for source, results in search_results.items():
            try:
                source_label = tk.Label(
                    result_window, 
                    text=source, 
                    font=("Arial", 14, "bold")
                )
                source_label.pack(pady=10)
                
                for result in results[:100]:  # Limit results display
                    result_label = tk.Label(
                        result_window,
                        text=result.text,
                        wraplength=400,
                        justify="left"
                    )
                    result_label.pack()
                    
            except Exception as e:
                logger.error(f"Error displaying result: {str(e)}")
                messagebox.showerror(
                    "Display Error",
                    "Error displaying some results. Please try again."
                )

    except SearchError as se:
        logger.error(f"Search error: {str(se)}")
        messagebox.showerror("Search Error", str(se))
    except UIError as ue:
        logger.error(f"UI error: {str(ue)}")
        messagebox.showerror("Interface Error", str(ue))
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        messagebox.showerror(
            "Error",
            "An unexpected error occurred. Please try again."
        )

# Create the main window
try:
    root = tk.Tk()
    root.title("Comprehensive Search Tool")
    root.geometry("600x400")
    root.minsize(400, 300)

    # Create the search entry field
    entry = tk.Entry(root, width=40)
    entry.pack(pady=20)

    # Create search button
    search_button = tk.Button(root, text="Search", command=search_data_ui)
    search_button.pack(pady=10)

    root.mainloop()

except Exception as e:
    logger.critical(f"Failed to initialize application: {str(e)}")
    raise SystemExit("Failed to start application")