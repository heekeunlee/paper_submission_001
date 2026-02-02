# Implementation Plan - Expand 2026 Draft with 2025 Technical Details

## Goal
Significantly increase the length and technical depth of the 2026 paper draft by integrating specific data from the 2025 submission, while maintaining the "Winning Strategy" (high-impact, anti-OLED) tone.

## Proposed Changes

### [MODIFY] [index.html](file:///Users/dasepa/paper_submission_001/index.html)

#### 1. Abstract Expansion
- **Add**: Specific panel specs (326 PPI, 320x390, 2.1-inch proof-of-concept for 12.3-inch validation).
- **Add**: Specific environmental range (-30°C to +85°C).

#### 2. Introduction Expansion -> "1.1 The Paradigm Shift"
- **Add**: Definitions of **FID (Front Information Display)**, **PID (Passenger Information Display)**, and **CID (Central Information Display)** to clearly define the application scope.

#### 3. Design & Fabrication Expansion -> "2.1 Optical Architecture"
- **Add**: **Equations (1), (2), (3)** from 2025 script (Viewing Angle, Crosstalk, Efficiency).
- **Format**: Use HTML subscripts/superscripts for professional appearance.
- **Add**: Simulation parameters (BM1 +8um, OC 6um, BM2 +3.5um) as explicit "Design Rules".

#### 4. Design & Fabrication Expansion -> "2.2 Device Structure" (New Sub-section)
- **Add**: Micro-LED chip dimensions (R: 15x30um, G/B: 13x28um).
- **Add**: Pixel layout description (RGB Stripe, Odd/Even domain separation).

#### 5. Experimental Results Expansion
- **Add**: "AOI (Automated Optical Inspection)" verification mentions.
- **Add**: Comparison details with BOE (referencing the "prior work" but dismissing it as LCD-limited).

#### 6. Highlighter & Annotations
- **Update**: Apply `<span class="highlight" data-note="...">` to the new technical sections to explain *why* these details win points (e.g., "Defining variables mathematically shows rigor").

## Verification Plan
- **Visual Check**: Ensure the preview sections in `index.html` look significantly longer and deeper.
- **Content Check**: Verify equations render correctly.
- **Functionality**: Check that new highlights have working tooltips.
