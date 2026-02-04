#!/usr/bin/env python3
"""Generate favicon with red background and lobster emoji."""
import subprocess, os

# Create SVG favicon
svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">
  <rect width="48" height="48" rx="10" fill="#dc2626"/>
  <text x="24" y="34" font-size="28" text-anchor="middle">🦞</text>
</svg>'''

svg_path = os.path.join(os.path.dirname(__file__), 'favicon.svg')
ico_path = os.path.join(os.path.dirname(__file__), 'favicon.ico')
png_path = os.path.join(os.path.dirname(__file__), 'icon.png')
apple_path = os.path.join(os.path.dirname(__file__), 'apple-icon.png')

with open(svg_path, 'w') as f:
    f.write(svg)

# Try to convert with sips (macOS built-in) or just keep SVG
try:
    # Create a 180x180 PNG for apple-touch-icon using html canvas approach
    # Use sips to convert if possible
    print(f"SVG favicon saved to {svg_path}")
    print("Use the SVG directly or convert with an image tool")
except Exception as e:
    print(f"Note: {e}")

print("Done!")
