---
name: Sentinel Protocol
colors:
  surface: '#0f131d'
  surface-dim: '#0f131d'
  surface-bright: '#353944'
  surface-container-lowest: '#0a0e18'
  surface-container-low: '#171b26'
  surface-container: '#1c1f2a'
  surface-container-high: '#262a35'
  surface-container-highest: '#313540'
  on-surface: '#dfe2f1'
  on-surface-variant: '#bacbb9'
  inverse-surface: '#dfe2f1'
  inverse-on-surface: '#2c303b'
  outline: '#859585'
  outline-variant: '#3b4a3d'
  surface-tint: '#00e475'
  primary: '#75ff9e'
  on-primary: '#003918'
  primary-container: '#00e676'
  on-primary-container: '#00612e'
  inverse-primary: '#006d35'
  secondary: '#ffb3ae'
  on-secondary: '#68000c'
  secondary-container: '#a00118'
  on-secondary-container: '#ffa8a3'
  tertiary: '#ffe387'
  on-tertiary: '#3b2f00'
  tertiary-container: '#ecc52e'
  on-tertiary-container: '#655200'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#62ff96'
  primary-fixed-dim: '#00e475'
  on-primary-fixed: '#00210b'
  on-primary-fixed-variant: '#005226'
  secondary-fixed: '#ffdad7'
  secondary-fixed-dim: '#ffb3ae'
  on-secondary-fixed: '#410004'
  on-secondary-fixed-variant: '#930015'
  tertiary-fixed: '#ffe17b'
  tertiary-fixed-dim: '#eac32b'
  on-tertiary-fixed: '#231b00'
  on-tertiary-fixed-variant: '#564500'
  background: '#0f131d'
  on-background: '#dfe2f1'
  surface-variant: '#313540'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: 0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-sm:
    fontFamily: Space Grotesk
    fontSize: 11px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.08em
  mono-data:
    fontFamily: monospace
    fontSize: 13px
    fontWeight: '400'
    lineHeight: '1.4'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  container-padding: 20px
  grid-gap: 12px
---

## Brand & Style

The design system is engineered to evoke a sense of absolute surveillance, technical precision, and rapid response. It caters to security analysts and system administrators who require a "Command Center" atmosphere. The aesthetic is a fusion of **Glassmorphism** and **Technical Minimalism**, utilizing translucent layers to suggest depth in a data-dense environment.

The visual narrative focuses on "The Void"—a deep charcoal canvas where critical information is illuminated by high-intensity neon signals. This creates a high-contrast environment that minimizes eye strain during long monitoring shifts while ensuring that system alerts are impossible to miss.

## Colors

The palette is strictly functional. The primary background is a near-black charcoal, providing a non-reflective base. 

- **Primary (Neon Green):** Used exclusively for "Safe," "Active," and "Online" statuses.
- **Secondary (Neon Red):** Reserved for "Critical," "Attack," and "High Risk" indicators.
- **Tertiary (Neon Yellow):** Indicates "Warning," "Medium Risk," or "System Latency."
- **Neutrals:** A range of cool grays and semi-transparent whites are used for secondary data and UI borders to maintain a sophisticated, layered look without cluttering the visual field.

## Typography

This design system utilizes **Space Grotesk** for headlines and interactive labels to provide a technical, futuristic edge. Its geometric construction mirrors the precision of code. For sustained reading and complex data tables, **Inter** is employed for its exceptional legibility at small sizes.

Uppercase styling is used for section headers and status labels to simulate military-grade instrumentation. A monospace fallback is recommended for IP addresses, timestamps, and log entries to ensure character alignment in vertical stacks.

## Layout & Spacing

The layout follows a **Fluid Monitoring Grid** philosophy. Content is organized into modular "blades" or "tiles" that occupy a 12-column system. 

- **Density:** High. The system prioritizes information density over whitespace to allow analysts to see the maximum amount of telemetry on a single screen.
- **Grid:** Use a 12px gap between cards to maintain a tight, integrated feel.
- **Alignment:** All elements must align to a 4px baseline grid to maintain the "engineered" aesthetic.

## Elevation & Depth

Depth in this design system is achieved through **Tonal Translucency** rather than traditional drop shadows. 

1.  **Level 0 (Canvas):** Pure `#05070A` background.
2.  **Level 1 (Panels):** Semi-transparent `#0B0F19` at 70% opacity with a `10px` backdrop blur.
3.  **Level 2 (Modals/Popovers):** Solid `#161B26` with a thin `1px` inner border of `#FFFFFF15`.

Shadows, when used, are "Neon Glows"—low-spread, high-intensity blurs using the primary or secondary color to indicate an active or alerted state on a component.

## Shapes

The shape language is "Tactical Sharp." While most elements maintain a crisp, professional edge, a subtle `4px` (soft) radius is applied to containers to prevent the UI from feeling dated or overly aggressive. 

Interactive elements like buttons and input fields use the same `rounded-sm` (4px) logic. Status pips and small iconography may use circular (pill) shapes to provide a visual break from the rigid grid.

## Components

### Buttons & Inputs
Buttons are strictly rectangular with 4px rounding. "Action" buttons use a solid primary fill with black text. Secondary actions use "Ghost" styles with a 1px border and no fill. Input fields are dark with a 1px bottom border that glows when focused.

### Monitoring Cards
Cards must feature a translucent background (`backdrop-filter: blur(10px)`) and a subtle 1px border. Headers within cards should be set in uppercase `Space Grotesk` with a small status indicator (dot) in the top right.

### Data Visualization
Charts should use thin line weights (1px to 1.5px). Avoid solid fills in area charts; instead, use vertical linear gradients that fade to 0% opacity. All grid lines in charts should be `rgba(255, 255, 255, 0.05)`.

### Status Chips
Small, high-contrast badges used for risk levels (Low, Medium, High). They should utilize a background tint of the accent color at 15% opacity with 100% opacity text for maximum legibility against the dark background.

### Monitoring Grids
Use Zebra-striping on tables with `rgba(255, 255, 255, 0.02)` for even rows to help the eye track across dense data sets.