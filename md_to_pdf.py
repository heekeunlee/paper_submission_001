import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER

# Register Korean CID Font
# HYGoThic-Medium is a standard Korean font available in Adobe Reader and many viewers.
FONT_NAME = 'HYGoThic-Medium' 
try:
    pdfmetrics.registerFont(UnicodeCIDFont(FONT_NAME))
    print(f"Successfully registered CID font: {FONT_NAME}")
except Exception as e:
    print(f"Error registering CID font: {e}")
    # Fallback to HeiseiMin-W3 (Japanese) if Korean fails? Unlikely to help.
    # We'll see.

def process_text(text):
    # Remove markdown bold markers
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    return text

def convert_md_to_pdf(input_file, output_file):
    doc = SimpleDocTemplate(output_file, pagesize=A4,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=72)
    
    styles = getSampleStyleSheet()
    
    # Define styles using the CID font
    styles.add(ParagraphStyle(name='KoreanTitle', fontName=FONT_NAME, fontSize=24, leading=30, alignment=TA_CENTER, spaceAfter=20))
    styles.add(ParagraphStyle(name='KoreanH1', fontName=FONT_NAME, fontSize=18, leading=22, spaceBefore=15, spaceAfter=10))
    styles.add(ParagraphStyle(name='KoreanH2', fontName=FONT_NAME, fontSize=14, leading=18, spaceBefore=10, spaceAfter=5))
    styles.add(ParagraphStyle(name='KoreanBody', fontName=FONT_NAME, fontSize=10, leading=16, alignment=TA_JUSTIFY))
    styles.add(ParagraphStyle(name='KoreanQuote', fontName=FONT_NAME, fontSize=10, leading=16, leftIndent=20, textColor='grey'))
    
    story = []
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except:
         with open(input_file, 'r', encoding='euc-kr') as f: # Fallback
            lines = f.readlines()
        
    for line in lines:
        line = line.strip()
        if not line:
            story.append(Spacer(1, 6))
            continue
            
        line_content = process_text(line)
        
        # Escape XML characters that might confuse ReportLab
        # ReportLab paragraph text is XML-like.
        line_content = line_content.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        
        if line.startswith('# '):
            text = line_content[2:]
            story.append(Paragraph(text, styles['KoreanTitle']))
        elif line.startswith('## '):
            text = line_content[3:]
            story.append(Paragraph(text, styles['KoreanH1']))
        elif line.startswith('### '):
            text = line_content[4:]
            story.append(Paragraph(text, styles['KoreanH2']))
        elif line.startswith('> '):
            text = line_content[2:]
            story.append(Paragraph(text, styles['KoreanQuote']))
        elif line.startswith('---'):
            story.append(PageBreak())
        elif line.startswith('- ') or line.startswith('* '):
            text = line_content[2:]
            story.append(Paragraph(f'• {text}', styles['KoreanBody']))
        elif re.match(r'^\d+\.', line):
            text = line_content
            story.append(Paragraph(text, styles['KoreanBody']))
        else:
            story.append(Paragraph(line_content, styles['KoreanBody']))
            
    doc.build(story)
    print(f"Successfully generated {output_file}")

if __name__ == "__main__":
    input_md = "03_PAPER_DRAFT_2026.md"
    output_pdf = "03_PAPER_DRAFT_2026_Final.pdf"
    convert_md_to_pdf(input_md, output_pdf)
