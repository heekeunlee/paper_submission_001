import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.font_manager as fm
import textwrap
import re

def convert_md_to_pdf_mpl(input_file, output_file):
    # Setup Font
    font_path = '/System/Library/Fonts/AppleSDGothicNeo.ttc'
    try:
        # Load the font explicitly
        prop = fm.FontProperties(fname=font_path)
        plt.rcParams['font.family'] = prop.get_name() # Try setting global fam
    except:
        print("Error loading font")
        return

    # Read Content
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Process Lines (Wrap text)
    wrapped_lines = []
    MAX_CHARS = 70 # Reduced slightly for better margins
    
    for line in lines:
        line = line.strip()
        
        # Simple cleanup
        line = line.replace('**', '') 
        
        # Handle headers
        if line.startswith('#'):
            clean_line = line.lstrip('#').strip()
            wrapped_lines.append("") 
            wrapped_lines.append(f"[{clean_line}]")
            wrapped_lines.append("")
        elif line.startswith('---'):
             wrapped_lines.append("-" * 50)
        else:
            # Wrap long lines
            # Check for bullet points
            if line.startswith('- ') or line.startswith('* '):
                prefix = "• "
                content = line[2:]
                wrapped = textwrap.wrap(content, width=MAX_CHARS - 2)
                wrapped_lines.append(prefix + wrapped[0])
                for w in wrapped[1:]:
                     wrapped_lines.append("  " + w)
            else:
                if len(line) > MAX_CHARS:
                    wrapped_lines.extend(textwrap.wrap(line, width=MAX_CHARS))
                else:
                    wrapped_lines.append(line)

    # Render to PDF
    pp = PdfPages(output_file)
    
    LINES_PER_PAGE = 45 # Reduced for readability
    total_pages = (len(wrapped_lines) + LINES_PER_PAGE - 1) // LINES_PER_PAGE
    
    for page_num in range(total_pages):
        fig = plt.figure(figsize=(8.27, 11.69)) # A4 size
        fig.clf()
        plt.axis('off')
        
        start_idx = page_num * LINES_PER_PAGE
        end_idx = min((page_num + 1) * LINES_PER_PAGE, len(wrapped_lines))
        page_content = wrapped_lines[start_idx:end_idx]
        
        # Render each line individually to ensure font prop is applied
        # (Joining them into one big string sometimes causes issues with mixed scripts if not handled right, 
        # but let's try line by line for control)
        
        y_pos = 0.95
        line_height = 0.02
        
        for line_text in page_content:
            # Check if it's a header (heuristic: starts with [ and ends with ])
            fontsize = 10
            if line_text.startswith('[') and line_text.endswith(']'):
                fontsize = 12
                # weight = 'bold' # Matplotlib real bold needs bold font file
            
            plt.text(0.1, y_pos, line_text, transform=fig.transFigure, 
                     ha='left', va='top', fontproperties=prop, fontsize=fontsize)
            y_pos -= line_height
        
        # Footer page number
        plt.text(0.5, 0.05, f"- {page_num + 1} -", transform=fig.transFigure, 
                 ha='center', fontproperties=prop, fontsize=8)

        pp.savefig(fig)
        plt.close()
        
    pp.close()
    print(f"pdf saved to {output_file}")

if __name__ == "__main__":
    convert_md_to_pdf_mpl("03_PAPER_DRAFT_2026.md", "03_PAPER_DRAFT_2026_Final.pdf")
