# Implementation Plan - Paper Draft Enhancements

## User Review Required
> [!IMPORTANT]
> The .docx format will be simulated using a Markdown file (`.md`) labeled as a document, or a `.txt` file, as I cannot generate binary Word documents. I will label them clearly.

## Proposed Changes

### File Generation
#### [NEW] [03_PAPER_DRAFT_2026.txt](file:///Users/dasepa/paper_submission_001/03_PAPER_DRAFT_2026.txt)
- Exact copy of the markdown draft but in plain text format.

### Web Interface Updates
#### [MODIFY] [index.html](file:///Users/dasepa/paper_submission_001/index.html)
- **Hero Section**: Replace single 2026 download button with two buttons:
    - `[TXT 다운로드]` pointing to `.txt` file.
    - `[DOCX (Markdown) 다운로드]` pointing to `.md` file (or re-purposed text file).
- **New Section**: Add `<section id="preview">` containing the full draft text.
    - Wrap key "winning point" sentences in `<span class="highlight" data-note="...">`.
    - This allows for "highlighter" visual effect with marginalia notes.

#### [MODIFY] [styles.css](file:///Users/dasepa/paper_submission_001/styles.css)
- Add styles for `.btn-group` to hold multiple buttons.
- Add styles for `.paper-preview` container (white background, typewriter font?).
- Add `.highlight` class with yellow background.
- Add `.note-bubble` for the annotations.

## Verification Plan
### Automated Tests
- None.

### Manual Verification
- **Download Check**: Click both buttons to ensure they download the correct files.
- **Visual Check**: Verify the "Preview" section appears below the hero.
- **Annotation Check**: Hover/See the highlighted text and ensure the "notes" explain the strategy changes (e.g., "Attack OLED Weakness").
