import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.font_manager as fm
import textwrap

def convert_md_to_pdf_mpl(input_file, output_file):
    # Setup Font
    font_path = '/System/Library/Fonts/AppleSDGothicNeo.ttc'
    try:
        prop = fm.FontProperties(fname=font_path)
        prop.set_size(10)
    except:
        print("Error loading font")
        return

    # Read Content
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Process Lines (Wrap text)
    wrapped_lines = []
    MAX_CHARS = 75 # Approximate chars per line for A4 portrait
    
    for line in lines:
        line = line.strip()
        # Remove bold markers
        line = line.replace('**', '')
        # Remove headers hashes for cleaner look
        if line.startswith('#'):
            line = line.lstrip('#').strip()
            # Add some spacing/emphasis could be simulated by empty lines
            wrapped_lines.append("") 
            wrapped_lines.append(f"[{line}]") # Mark headers with brackets or just caps?
            wrapped_lines.append("")
        elif line.startswith('---'):
             wrapped_lines.append("-" * 50)
        else:
            # Wrap long lines
            if len(line) > MAX_CHARS:
                wrapped_lines.extend(textwrap.wrap(line, width=MAX_CHARS))
            else:
                wrapped_lines.append(line)

    # Render to PDF
    pp = PdfPages(output_file)
    
    LINES_PER_PAGE = 50
    total_pages = (len(wrapped_lines) + LINES_PER_PAGE - 1) // LINES_PER_PAGE
    
    for page_num in range(total_pages):
        fig = plt.figure(figsize=(8.27, 11.69)) # A4 size in inches
        fig.clf()
        
        # Disable axis
        plt.axis('off')
        
        start_idx = page_num * LINES_PER_PAGE
        end_idx = min((page_num + 1) * LINES_PER_PAGE, len(wrapped_lines))
        page_content = wrapped_lines[start_idx:end_idx]
        
        # Join with newlines
        text_content = "\n".join(page_content)
        
        # Add text
        plt.text(0.1, 0.9, text_content, transform=fig.transFigure, ha='left', va='top', fontproperties=prop, wrap=True)
        
        pp.savefig(fig)
        plt.close()
        
    pp.close()
    print(f"pdf saved to {output_file}")

if __name__ == "__main__":
    convert_md_to_pdf_mpl("03_PAPER_DRAFT_2026.md", "03_PAPER_DRAFT_2026_Final.pdf")
