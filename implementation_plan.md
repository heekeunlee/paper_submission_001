# Implementation Plan - Massive Content Expansion (3x)

## Goal
Triple the text length of the 2026 paper draft (Sections 1-5) in both Korean and English. Ensure the "Rebuilding Strategy" (High Impact, Anti-OLED, Safety) is maintained while adding deep logical flow and experimental rigor.

## Proposed Strategy per Section

### 1. Introduction
- **Deepen Context**: Elaborate on the "Zero-Layer" UI trend in autonomous cockpits and the conflict between information quantity and driver distraction.
- **Mechanism of Failure**: Explain *physically* why OLED fails (Differential aging of Blue emitter, Junction temperature rise causing ABL).
- **Novelty Assertion**: Explicitly frame the 3-pillar solution (Optics, Circuit, Process) as a necessary "System-Level Optimization" rather than component tweaking.

### 2. Design & Fabrication
- **Optical**: Detail the Monte Carlo simulation boundary conditions. Explain the trade-off curve between "Crosstalk" and "Efficiency" and how the 'Sweet Spot' was found using the derivative of the curve.
- **Circuit**: Explain the Quantum Confined Stark Effect (QCSE) in LEDs to justify PWM over PAM. Describe the LTPS TFT structure (7T1C or similar standard) briefly to show compatibility.
- **Process**: Explain the "Viscoelastic" property of the PDMS stamp used in Kinetic Control.

### 3. Experimental Results
- **Measurement Setup**: Mention specific tools (Eldim EZContrast, CA-410).
- **Reliability Logic**: Contrast the "Bond Dissociation Energy" of Organic materials vs. GaN crystal structure to explain the reliability gap.

### 4. Discussion
- **TCO Model**: Expand on the "Total Cost of Ownership" argument. Initial Yield Cost vs. Field Failure Replacement Cost.
- **Safety**: Link Crosstalk to "Cognitive Tunneling" and accident rates.

### 5. Conclusion
- **Final Verdict**: Frame Micro-LED not just as "Better" but as the "Only Viable Option" for L4+ Autonomous Vehicles.

## Execution Steps
1.  **Update `index.html`**:
    -   Rewrite `<section id="preview-ko">` with the expanded text.
    -   Rewrite `<section id="preview-en">` with the expanded text.
    -   Update highlights to cover new key logical points.
2.  **Update Artifacts**:
    -   Overwrite `03_PAPER_DRAFT_2026.txt` with the new text.
    -   Overwrite `03_PAPER_DRAFT_2026.md` with the new text.
3.  **Deployment**:
    -   Git push.

## Verification
- **Length Check**: Visually verify the preview is much longer.
- **Logic Check**: Read through to ensure the argument flows logically (Problem -> Mechanism -> Solution -> Proof -> Implication).
