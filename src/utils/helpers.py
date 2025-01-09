def is_valid_url(url : str):
    """Check if a URL is valid."""
    return url.startswith("https://github.com/")


def is_valid_file(file_path : str):
    """Check if a file path is valid."""
    valid_extensions = [
        '.py', '.java', '.c', '.cpp', '.cs', '.js', '.ts', '.rb', '.go', '.rs', '.php', '.html', '.css', '.xml', 
        '.json', '.yaml', '.yml', '.md', '.txt', '.sh', '.bat', '.pl', '.swift', '.kt', '.scala', '.r', '.m', 
        '.vb', '.vbs', '.lua', '.sql', '.asm', '.s', '.dart', '.erl', '.ex', '.exs', '.hs', '.jl', '.lisp', 
        '.clj', '.cljs', '.groovy', '.f', '.f90', '.f95', '.ada', '.d', '.pas', '.pro', '.tcl', '.v', '.sv', 
        '.vhdl', '.hdl', '.m', '.mat', '.sas', '.r', '.rmd', '.tex', '.bib', '.rst', '.org', '.ipynb', '.tsx', 
        '.jsx', '.tsx', '.vue', '.scss', '.less', '.coffee', '.h', '.hpp', '.hh', '.hxx', '.ino', '.pde', '.ino', 
        '.pde', '.rkt', '.scm', '.ss', '.cl', '.ml', '.mli', '.mll', '.mly', '.sml', '.sig', '.fun']
    return any(file_path.lower().endswith(ext) for ext in valid_extensions)

def remove_special_chars(text : str):
    """Remove special characters from a string."""
    return ''.join(e for e in text if e.isalnum() or e.isspace() or e in ['/', '\\', '-', '_', '.'])