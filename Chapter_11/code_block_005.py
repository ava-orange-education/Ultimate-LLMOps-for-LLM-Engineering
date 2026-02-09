def fetch_critical_prompts_on_startup():
    try:
        langfuse.get_prompt("text-summarizer")
        print("Successfully pre-fetched 'text-summarizer' prompt.")
    except Exception as e:
        print(f"ERROR: Failed to fetch critical prompt on startup: {e}")
        sys.exit(1) # Exit if critical prompt cannot be fetched