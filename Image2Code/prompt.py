PROMPT = """
Generate a responsive HTML and CSS design based on the given layout data.

- Use modern semantic HTML tags (e.g., <section>, <article>, <nav>, <header>, <footer>).
- Implement a CSS flexbox/grid-based layout to approximate the provided positions.
- Ensure font sizes and placements align with the given text positions.
- Use <ul> and <li> for menu-like structures and buttons for actionable elements.
- Ensure responsiveness without using absolute positioning.
- Output only the HTML and CSS source code without any explanations.

Layout Data: {layout}
"""