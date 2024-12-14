PROMPT="""
Create an HTML and CSS design for a handwriting-style website based on the given layout data, which includes text elements and their coordinates. Follow these guidelines:

1. Use semantic and modern HTML tags to structure the page effectively.
2. Ensure the CSS positions elements based on relative layout principles rather than absolute coordinates.
3. Adjust font sizes and element placement to approximate the provided coordinates while adhering to responsive design principles.
4. Use <ul> and <li> tags for elements resembling menus or lists.
5. Incorporate interactive tags like <button> or <input> if elements appear to function as such.
6. Infuse creativity to enhance the layout by leveraging common web design principles while maintaining alignment with the provided data.
7. Do not include any absolute coordinate values in the source code.
8. Output the HTML and CSS source code only, without any additional explanation or comments.

Input Layout: {layout}
"""